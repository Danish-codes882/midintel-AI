"""
MedIntel AI - Health Intelligence Platform
Backend API Server with Intelligent Scraping Engine
"""

from flask import Flask, render_template, request, jsonify, send_from_directory
import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime, timedelta
from collections import defaultdict
import json
import logging
from urllib.parse import quote_plus
import hashlib

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'medintel-health-intelligence-2025'

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ==================== CACHING LAYER ====================
query_cache = {}
scrape_cache = {}
CACHE_DURATION = timedelta(hours=6)

# ==================== RATE LIMITING ====================
rate_limit_store = defaultdict(list)
MAX_REQUESTS_PER_MINUTE = 20

def check_rate_limit(ip_address):
    """Check if IP has exceeded rate limit"""
    current_time = time.time()
    # Clean old requests
    rate_limit_store[ip_address] = [
        req_time for req_time in rate_limit_store[ip_address]
        if current_time - req_time < 60
    ]
    
    if len(rate_limit_store[ip_address]) >= MAX_REQUESTS_PER_MINUTE:
        return False
    
    rate_limit_store[ip_address].append(current_time)
    return True

# ==================== KNOWLEDGE BASE ====================
KNOWLEDGE_BASE = {
    "emergency_keywords": [
        "chest pain", "heart attack", "stroke", "unconscious", "seizure",
        "severe bleeding", "difficulty breathing", "choking", "severe burns",
        "poisoning", "overdose", "severe allergic reaction", "anaphylaxis",
        "suicide", "severe head injury", "paralysis", "confusion severe"
    ],
    "symptom_synonyms": {
        "fever": ["high temperature", "pyrexia", "hot", "burning up"],
        "headache": ["head pain", "migraine", "head ache"],
        "cough": ["coughing", "hacking"],
        "chest pain": ["tight chest", "chest pressure", "angina"],
        "nausea": ["sick", "queasy", "feeling sick"],
        "vomiting": ["throwing up", "being sick", "puking"],
        "dizziness": ["dizzy", "lightheaded", "vertigo"],
        "fatigue": ["tired", "exhausted", "weakness", "weak"],
        "shortness of breath": ["breathless", "difficulty breathing", "dyspnea"],
        "sweating": ["perspiration", "sweaty", "night sweats"],
        "abdominal pain": ["stomach pain", "belly ache", "tummy pain"],
        "diarrhea": ["loose stools", "runs"],
        "constipation": ["blocked", "difficulty passing stool"],
        "rash": ["skin rash", "hives", "spots"],
        "sore throat": ["throat pain", "painful throat"],
        "joint pain": ["arthralgia", "aching joints"],
        "muscle pain": ["myalgia", "muscle ache"],
        "confusion": ["disorientation", "confused", "mental fog"],
        "back pain": ["backache", "spine pain"]
    },
    "conditions_data": {
        "Heart Attack": {
            "symptoms": ["chest pain", "shortness of breath", "sweating", "nausea", "dizziness"],
            "weights": {"chest pain": 10, "shortness of breath": 8, "sweating": 6, "nausea": 4, "dizziness": 5},
            "risk_factors": ["smoking", "high blood pressure", "diabetes", "family history", "obesity"],
            "emergency": True,
            "prevention": ["healthy diet", "regular exercise", "quit smoking", "manage stress"],
            "recommendations": ["Call 911 immediately", "Chew aspirin if not allergic", "Stay calm", "Loosen tight clothing"]
        },
        "Stroke": {
            "symptoms": ["facial drooping", "arm weakness", "speech difficulty", "confusion", "severe headache", "dizziness", "vision problems"],
            "weights": {"facial drooping": 10, "arm weakness": 10, "speech difficulty": 9, "confusion": 8, "severe headache": 7},
            "risk_factors": ["high blood pressure", "smoking", "diabetes", "atrial fibrillation", "high cholesterol"],
            "emergency": True,
            "prevention": ["control blood pressure", "healthy diet", "exercise", "limit alcohol"],
            "recommendations": ["Call 911 immediately", "Note time symptoms started", "Do not give food or drink", "Keep person comfortable"]
        },
        "Common Cold": {
            "symptoms": ["cough", "sore throat", "runny nose", "sneezing", "mild fever", "fatigue"],
            "weights": {"cough": 5, "sore throat": 5, "runny nose": 5, "sneezing": 4, "mild fever": 3, "fatigue": 3},
            "risk_factors": ["close contact with infected person", "weakened immune system", "stress"],
            "emergency": False,
            "prevention": ["wash hands frequently", "avoid close contact with sick people", "healthy lifestyle"],
            "recommendations": ["Rest", "Stay hydrated", "Use over-the-counter medications", "See doctor if symptoms worsen"]
        },
        "Influenza (Flu)": {
            "symptoms": ["high fever", "cough", "sore throat", "muscle pain", "fatigue", "headache", "chills"],
            "weights": {"high fever": 7, "cough": 6, "muscle pain": 6, "fatigue": 5, "headache": 5, "chills": 6},
            "risk_factors": ["weak immune system", "chronic conditions", "pregnancy", "young or elderly age"],
            "emergency": False,
            "prevention": ["annual flu vaccine", "hand hygiene", "avoid sick contacts"],
            "recommendations": ["Rest", "Fluids", "Antiviral medications (if prescribed)", "Monitor for complications"]
        },
        "Migraine": {
            "symptoms": ["severe headache", "nausea", "vomiting", "sensitivity to light", "visual disturbances"],
            "weights": {"severe headache": 9, "nausea": 6, "vomiting": 5, "sensitivity to light": 7, "visual disturbances": 7},
            "risk_factors": ["family history", "hormonal changes", "stress", "certain foods", "lack of sleep"],
            "emergency": False,
            "prevention": ["identify triggers", "maintain regular sleep", "stress management", "regular meals"],
            "recommendations": ["Dark quiet room", "Pain medication", "Cold compress", "Consult neurologist if frequent"]
        },
        "Gastroenteritis": {
            "symptoms": ["diarrhea", "vomiting", "nausea", "abdominal pain", "fever", "dehydration"],
            "weights": {"diarrhea": 8, "vomiting": 7, "nausea": 6, "abdominal pain": 7, "fever": 5},
            "risk_factors": ["contaminated food/water", "poor hygiene", "close contact with infected person"],
            "emergency": False,
            "prevention": ["hand washing", "food safety", "clean water", "avoid contaminated sources"],
            "recommendations": ["Hydration", "Oral rehydration salts", "Bland diet", "Rest", "See doctor if severe"]
        },
        "Pneumonia": {
            "symptoms": ["cough", "fever", "shortness of breath", "chest pain", "fatigue", "chills"],
            "weights": {"cough": 7, "fever": 7, "shortness of breath": 8, "chest pain": 7, "fatigue": 5, "chills": 6},
            "risk_factors": ["smoking", "chronic lung disease", "weakened immune system", "age over 65"],
            "emergency": False,
            "prevention": ["vaccination", "hand hygiene", "healthy lifestyle", "avoid smoking"],
            "recommendations": ["See doctor", "Antibiotics if bacterial", "Rest", "Fluids", "Monitor breathing"]
        },
        "Allergic Reaction": {
            "symptoms": ["rash", "itching", "swelling", "difficulty breathing", "hives"],
            "weights": {"rash": 5, "itching": 4, "swelling": 7, "difficulty breathing": 10, "hives": 6},
            "risk_factors": ["known allergies", "family history", "asthma"],
            "emergency": False,
            "prevention": ["avoid allergens", "carry epinephrine if severe allergies", "read food labels"],
            "recommendations": ["Antihistamines", "Avoid allergen", "Call 911 if anaphylaxis", "See allergist"]
        },
        "Anxiety Disorder": {
            "symptoms": ["excessive worry", "restlessness", "fatigue", "difficulty concentrating", "muscle tension", "sleep problems"],
            "weights": {"excessive worry": 8, "restlessness": 6, "fatigue": 5, "difficulty concentrating": 6, "muscle tension": 5},
            "risk_factors": ["stress", "trauma", "family history", "personality", "chronic illness"],
            "emergency": False,
            "prevention": ["stress management", "regular exercise", "adequate sleep", "limit caffeine"],
            "recommendations": ["Therapy", "Relaxation techniques", "Exercise", "Consult mental health professional"]
        },
        "Urinary Tract Infection": {
            "symptoms": ["frequent urination", "burning sensation", "cloudy urine", "pelvic pain", "fever"],
            "weights": {"frequent urination": 7, "burning sensation": 8, "cloudy urine": 6, "pelvic pain": 7, "fever": 5},
            "risk_factors": ["female gender", "sexual activity", "certain contraceptives", "urinary tract abnormalities"],
            "emergency": False,
            "prevention": ["adequate hydration", "urinate after intercourse", "wipe front to back", "avoid irritating products"],
            "recommendations": ["See doctor", "Antibiotics", "Increase fluids", "Pain relief medication"]
        }
    }
}

# ==================== MEDICAL SOURCES ====================
MEDICAL_SOURCES = {
    "mayoclinic": {
        "base_url": "https://www.mayoclinic.org",
        "search_url": "https://www.mayoclinic.org/search/search-results?q=",
        "priority": 9,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    },
    "webmd": {
        "base_url": "https://www.webmd.com",
        "search_url": "https://www.webmd.com/search/search_results/default.aspx?query=",
        "priority": 7,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    },
    "nhs": {
        "base_url": "https://www.nhs.uk",
        "search_url": "https://www.nhs.uk/search/?q=",
        "priority": 10,
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }
}

# ==================== INPUT VALIDATION ====================
def sanitize_input(text):
    """Clean and validate user input"""
    if not text or not isinstance(text, str):
        return ""
    
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Remove scripts
    text = re.sub(r'<script.*?</script>', '', text, flags=re.DOTALL)
    
    # Limit length
    text = text[:500]
    
    # Remove special characters except basic punctuation
    text = re.sub(r'[^\w\s,.-]', '', text)
    
    return text.strip()

# ==================== SYMPTOM PROCESSING ====================
def process_symptoms(input_text):
    """Process and normalize symptom input"""
    input_text = input_text.lower()
    
    # Remove stop words
    stop_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'is', 'am', 'are', 'was', 'were', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'should', 'could', 'may', 'might', 'must', 'can', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'very', 'so', 'lot'}
    
    words = input_text.split()
    filtered_words = [w for w in words if w not in stop_words]
    processed_text = ' '.join(filtered_words)
    
    # Extract symptoms
    detected_symptoms = set()
    
    # Check for exact matches and synonyms
    for symptom, synonyms in KNOWLEDGE_BASE["symptom_synonyms"].items():
        if symptom in processed_text:
            detected_symptoms.add(symptom)
        for syn in synonyms:
            if syn in processed_text:
                detected_symptoms.add(symptom)
    
    # Check for emergency keywords
    emergency_detected = False
    for keyword in KNOWLEDGE_BASE["emergency_keywords"]:
        if keyword in input_text:
            emergency_detected = True
            break
    
    return list(detected_symptoms), emergency_detected

# ==================== RISK SCORING ENGINE ====================
def calculate_risk_score(symptoms, condition_data):
    """Calculate risk score for a condition based on symptoms"""
    if not symptoms:
        return 0
    
    total_score = 0
    max_possible = sum(condition_data["weights"].values())
    
    for symptom in symptoms:
        if symptom in condition_data["weights"]:
            total_score += condition_data["weights"][symptom]
    
    # Normalize to 0-100
    if max_possible > 0:
        normalized_score = (total_score / max_possible) * 100
    else:
        normalized_score = 0
    
    return round(normalized_score, 1)

def get_severity_level(score):
    """Convert numeric score to severity level"""
    if score >= 76:
        return "Critical"
    elif score >= 51:
        return "High"
    elif score >= 26:
        return "Moderate"
    else:
        return "Low"

# ==================== WEB SCRAPING ENGINE ====================
def scrape_medical_info(query, max_sources=3):
    """Scrape medical information from trusted sources"""
    cache_key = hashlib.md5(query.encode()).hexdigest()
    
    # Check cache
    if cache_key in scrape_cache:
        cache_entry = scrape_cache[cache_key]
        if datetime.now() - cache_entry['timestamp'] < CACHE_DURATION:
            logger.info(f"Cache hit for query: {query}")
            return cache_entry['data']
    
    scraped_data = []
    
    for source_name, source_config in list(MEDICAL_SOURCES.items())[:max_sources]:
        try:
            # Build search URL
            search_url = source_config["search_url"] + quote_plus(query)
            
            # Set headers
            headers = {
                'User-Agent': source_config["user_agent"],
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            }
            
            # Make request with timeout
            response = requests.get(search_url, headers=headers, timeout=5)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove ads and scripts
            for element in soup(['script', 'style', 'iframe', 'nav', 'footer', 'aside']):
                element.decompose()
            
            # Extract clean text
            paragraphs = soup.find_all('p', limit=10)
            clean_text = []
            
            for p in paragraphs:
                text = p.get_text().strip()
                # Filter out short or irrelevant paragraphs
                if len(text) > 50 and not re.search(r'cookie|privacy|advertisement', text, re.IGNORECASE):
                    clean_text.append(text)
            
            if clean_text:
                scraped_data.append({
                    "source": source_name.upper(),
                    "priority": source_config["priority"],
                    "content": clean_text[:5],  # Top 5 paragraphs
                    "url": search_url
                })
                
            logger.info(f"Successfully scraped {source_name}")
            
            # Rate limiting
            time.sleep(0.5)
            
        except requests.Timeout:
            logger.warning(f"Timeout scraping {source_name}")
        except requests.RequestException as e:
            logger.warning(f"Error scraping {source_name}: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error scraping {source_name}: {str(e)}")
    
    # Sort by priority
    scraped_data.sort(key=lambda x: x['priority'], reverse=True)
    
    # Cache results
    scrape_cache[cache_key] = {
        'timestamp': datetime.now(),
        'data': scraped_data
    }
    
    return scraped_data

# ==================== AI INSIGHT GENERATOR ====================
def generate_insights(symptoms, conditions_ranked, emergency_flag, scraped_data):
    """Generate intelligent medical insights"""
    
    if emergency_flag:
        summary = "⚠️ EMERGENCY DETECTED - Based on your symptoms, this could be a medical emergency. Seek immediate medical attention."
    elif not conditions_ranked:
        summary = "Based on the information provided, we couldn't match specific conditions. Please consult a healthcare provider for accurate assessment."
    else:
        top_condition = conditions_ranked[0]
        summary = f"Based on your symptoms, {top_condition['name']} shows a {top_condition['match_percentage']}% match. "
        summary += f"Severity assessment: {top_condition['severity']}. "
        
        if top_condition['severity'] in ['High', 'Critical']:
            summary += "Consider seeking medical attention soon."
        else:
            summary += "Monitor your symptoms and consult a healthcare provider if they worsen."
    
    # Build recommendations
    recommendations = []
    
    if emergency_flag:
        recommendations = [
            "Call emergency services (911) immediately",
            "Do not drive yourself to the hospital",
            "Stay calm and in a safe position",
            "If possible, have someone stay with you"
        ]
    elif conditions_ranked:
        top_condition = conditions_ranked[0]
        condition_data = KNOWLEDGE_BASE["conditions_data"][top_condition['name']]
        recommendations = condition_data.get("recommendations", [])[:4]
    
    # Add prevention tips
    prevention_tips = []
    if conditions_ranked and not emergency_flag:
        top_condition = conditions_ranked[0]
        condition_data = KNOWLEDGE_BASE["conditions_data"][top_condition['name']]
        prevention_tips = condition_data.get("prevention", [])[:3]
    
    # Format scraped sources
    sources = []
    for data in scraped_data:
        sources.append({
            "name": data["source"],
            "url": data["url"],
            "credibility": data["priority"]
        })
    
    return {
        "summary": summary,
        "recommendations": recommendations,
        "prevention": prevention_tips,
        "sources": sources[:3]  # Top 3 sources
    }

# ==================== API ROUTES ====================
@app.route('/')
def index():
    """Serve main application page"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Main API endpoint for symptom analysis"""
    try:
        # Get client IP for rate limiting
        client_ip = request.remote_addr
        
        # Check rate limit
        if not check_rate_limit(client_ip):
            logger.warning(f"Rate limit exceeded for IP: {client_ip}")
            return jsonify({
                "error": "Rate limit exceeded. Please try again in a minute."
            }), 429
        
        # Get input
        data = request.get_json()
        if not data or 'symptoms' not in data:
            return jsonify({"error": "Invalid request. 'symptoms' field required."}), 400
        
        raw_input = data.get('symptoms', '')
        
        # Validate and sanitize
        clean_input = sanitize_input(raw_input)
        if not clean_input:
            return jsonify({"error": "Invalid input provided."}), 400
        
        logger.info(f"Processing query: {clean_input[:50]}...")
        
        # Check cache for exact query
        cache_key = hashlib.md5(clean_input.encode()).hexdigest()
        if cache_key in query_cache:
            cache_entry = query_cache[cache_key]
            if datetime.now() - cache_entry['timestamp'] < CACHE_DURATION:
                logger.info("Returning cached response")
                return jsonify(cache_entry['response'])
        
        # Process symptoms
        detected_symptoms, emergency_flag = process_symptoms(clean_input)
        
        # Match conditions
        conditions_ranked = []
        for condition_name, condition_data in KNOWLEDGE_BASE["conditions_data"].items():
            score = calculate_risk_score(detected_symptoms, condition_data)
            
            if score > 0:
                conditions_ranked.append({
                    "name": condition_name,
                    "match_percentage": score,
                    "severity": get_severity_level(score),
                    "symptoms": condition_data["symptoms"],
                    "risk_factors": condition_data["risk_factors"],
                    "is_emergency": condition_data["emergency"]
                })
        
        # Sort by match percentage
        conditions_ranked.sort(key=lambda x: x['match_percentage'], reverse=True)
        
        # Override emergency if condition flagged
        if conditions_ranked and conditions_ranked[0]['is_emergency']:
            emergency_flag = True
        
        # Scrape medical info (non-blocking enrichment)
        scraped_data = []
        if detected_symptoms:
            search_query = ' '.join(detected_symptoms[:3])  # Top 3 symptoms
            scraped_data = scrape_medical_info(search_query, max_sources=3)
        
        # Generate insights
        insights = generate_insights(
            detected_symptoms,
            conditions_ranked[:5],  # Top 5 conditions
            emergency_flag,
            scraped_data
        )
        
        # Build response
        response = {
            "summary": insights["summary"],
            "possible_conditions": conditions_ranked[:5],
            "severity_level": conditions_ranked[0]["severity"] if conditions_ranked else "Unknown",
            "recommendations": insights["recommendations"],
            "prevention": insights["prevention"],
            "emergency_flag": emergency_flag,
            "sources": insights["sources"],
            "detected_symptoms": detected_symptoms,
            "timestamp": datetime.now().isoformat()
        }
        
        # Cache response
        query_cache[cache_key] = {
            'timestamp': datetime.now(),
            'response': response
        }
        
        logger.info(f"Analysis complete. Emergency: {emergency_flag}, Conditions found: {len(conditions_ranked)}")
        
        return jsonify(response)
        
    except Exception as e:
        logger.error(f"Error in analyze endpoint: {str(e)}")
        return jsonify({
            "error": "An error occurred processing your request. Please try again.",
            "emergency_flag": False
        }), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "cache_size": len(query_cache),
        "scrape_cache_size": len(scrape_cache)
    })

@app.route('/sitemap.xml')
def sitemap():
    """Basic sitemap for SEO"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
    <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <url>
            <loc>https://medintel.ai/</loc>
            <changefreq>daily</changefreq>
            <priority>1.0</priority>
        </url>
        <url>
            <loc>https://medintel.ai/privacy</loc>
            <changefreq>monthly</changefreq>
            <priority>0.5</priority>
        </url>
    </urlset>''', 200, {'Content-Type': 'application/xml'}

@app.route('/privacy')
def privacy():
    """Privacy policy page"""
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Privacy Policy - MedIntel AI</title>
        <style>
            body { font-family: system-ui; max-width: 800px; margin: 40px auto; padding: 20px; }
            h1 { color: #2c3e50; }
            p { line-height: 1.6; }
        </style>
    </head>
    <body>
        <h1>Privacy Policy</h1>
        <p>Last updated: February 2025</p>
        <p>MedIntel AI is committed to protecting your privacy. This service is provided for educational purposes only.</p>
        <p><strong>Data Collection:</strong> We do not store or collect personal health information. All queries are processed in real-time and not permanently stored.</p>
        <p><strong>Caching:</strong> Temporary caching is used to improve performance, with automatic expiration.</p>
        <p><strong>Third-party Sources:</strong> We scrape publicly available medical information from trusted sources for educational purposes.</p>
        <p><strong>No Medical Advice:</strong> This platform does not provide medical advice, diagnosis, or treatment.</p>
        <p>For questions, contact: privacy@medintel.ai</p>
    </body>
    </html>
    '''

# ==================== ERROR HANDLERS ====================
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    logger.error(f"Internal server error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500

# ==================== MAIN ====================
if __name__ == '__main__':
    logger.info("Starting MedIntel AI Health Intelligence Platform...")
    app.run(debug=True, host='0.0.0.0', port=5000)