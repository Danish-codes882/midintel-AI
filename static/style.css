/* ==================== CSS VARIABLES ==================== */
:root {
    /* Colors - Light Theme */
    --bg-primary: #f8f9fa;
    --bg-secondary: #ffffff;
    --bg-glass: rgba(255, 255, 255, 0.7);
    --text-primary: #1a1a2e;
    --text-secondary: #4a4a68;
    --text-muted: #6c757d;
    
    /* Gradients */
    --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    --gradient-secondary: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    --gradient-success: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    --gradient-warning: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    --gradient-danger: linear-gradient(135deg, #ff0844 0%, #ffb199 100%);
    
    /* Accent Colors */
    --accent-primary: #667eea;
    --accent-secondary: #764ba2;
    --accent-success: #00f2fe;
    --accent-warning: #fee140;
    --accent-danger: #ff0844;
    
    /* Shadows */
    --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 8px 32px rgba(0, 0, 0, 0.15);
    --shadow-xl: 0 16px 48px rgba(0, 0, 0, 0.2);
    
    /* Spacing */
    --spacing-xs: 0.5rem;
    --spacing-sm: 1rem;
    --spacing-md: 1.5rem;
    --spacing-lg: 2rem;
    --spacing-xl: 3rem;
    
    /* Border Radius */
    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    --radius-xl: 24px;
    
    /* Typography */
    --font-display: 'Syne', sans-serif;
    --font-body: 'DM Sans', sans-serif;
}

/* Dark Theme */
body.dark-theme {
    --bg-primary: #0f0f1e;
    --bg-secondary: #1a1a2e;
    --bg-glass: rgba(26, 26, 46, 0.7);
    --text-primary: #ffffff;
    --text-secondary: #b8b8d4;
    --text-muted: #8888a8;
}

/* ==================== RESET & BASE ==================== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: var(--font-body);
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.6;
    overflow-x: hidden;
    transition: background 0.3s ease, color 0.3s ease;
}

/* Animated Background */
body::before {
    content: '';
    position: fixed;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at 20% 50%, rgba(102, 126, 234, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(118, 75, 162, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 40% 20%, rgba(0, 242, 254, 0.1) 0%, transparent 50%);
    animation: gradientShift 20s ease infinite;
    z-index: -1;
}

@keyframes gradientShift {
    0%, 100% { transform: translate(0, 0) rotate(0deg); }
    33% { transform: translate(5%, 5%) rotate(120deg); }
    66% { transform: translate(-5%, 5%) rotate(240deg); }
}

.bg-decoration {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: -1;
    opacity: 0.3;
}

/* ==================== NAVIGATION ==================== */
.navbar {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: var(--bg-glass);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding: 1rem 0;
    animation: slideDown 0.6s ease;
}

@keyframes slideDown {
    from { transform: translateY(-100%); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-family: var(--font-display);
    font-size: 1.5rem;
    font-weight: 800;
    cursor: pointer;
    transition: transform 0.3s ease;
}

.logo:hover {
    transform: scale(1.05);
}

.logo-icon {
    font-size: 2rem;
    animation: pulse 2s ease infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
}

.logo-text {
    color: var(--text-primary);
}

.logo-ai {
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 2rem;
}

.nav-links a {
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
    position: relative;
}

.nav-links a::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    width: 0;
    height: 2px;
    background: var(--gradient-primary);
    transition: width 0.3s ease;
}

.nav-links a:hover {
    color: var(--text-primary);
}

.nav-links a:hover::after {
    width: 100%;
}

.theme-toggle {
    background: var(--bg-glass);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-md);
    padding: 0.5rem 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 1.2rem;
}

.theme-toggle:hover {
    transform: scale(1.1);
    box-shadow: var(--shadow-md);
}

/* ==================== HERO SECTION ==================== */
.hero {
    max-width: 1200px;
    margin: 0 auto;
    padding: 6rem 2rem 4rem;
    text-align: center;
}

.hero-content {
    animation: fadeInUp 0.8s ease;
}

@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

.hero-title {
    font-family: var(--font-display);
    font-size: clamp(2.5rem, 8vw, 5rem);
    font-weight: 800;
    line-height: 1.1;
    margin-bottom: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.title-line {
    animation: slideInLeft 0.8s ease;
}

.title-line:nth-child(2) {
    animation-delay: 0.2s;
}

@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-50px); }
    to { opacity: 1; transform: translateX(0); }
}

.gradient-text {
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-subtitle {
    font-size: 1.25rem;
    color: var(--text-secondary);
    max-width: 600px;
    margin: 0 auto 2.5rem;
    animation: fadeIn 1s ease 0.4s both;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.hero-cta {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
    animation: fadeInUp 1s ease 0.6s both;
}

.cta-button {
    padding: 1rem 2.5rem;
    border-radius: var(--radius-lg);
    font-weight: 600;
    font-size: 1.1rem;
    text-decoration: none;
    transition: all 0.3s ease;
    border: none;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.primary-cta {
    background: var(--gradient-primary);
    color: white;
    box-shadow: var(--shadow-lg);
}

.primary-cta:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-xl);
}

.secondary-cta {
    background: var(--bg-glass);
    backdrop-filter: blur(10px);
    color: var(--text-primary);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.secondary-cta:hover {
    background: var(--bg-secondary);
    transform: translateY(-2px);
}

/* Hero Stats */
.hero-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin-top: 4rem;
    animation: fadeInUp 1.2s ease 0.8s both;
}

.stat-card {
    background: var(--bg-glass);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-lg);
    padding: 2rem;
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
}

.stat-card:hover {
    transform: translateY(-5px);
    box-shadow: var(--shadow-lg);
}

.stat-number {
    font-family: var(--font-display);
    font-size: 3rem;
    font-weight: 800;
    background: var(--gradient-primary);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.stat-label {
    color: var(--text-secondary);
    font-size: 0.9rem;
    margin-top: 0.5rem;
}

/* ==================== FEATURES SECTION ==================== */
.features-section {
    max-width: 1200px;
    margin: 6rem auto;
    padding: 0 2rem;
}

.section-title {
    font-family: var(--font-display);
    font-size: 2.5rem;
    font-weight: 700;
    text-align: center;
    margin-bottom: 3rem;
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.feature-card {
    background: var(--bg-glass);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-lg);
    padding: 2rem;
    box-shadow: var(--shadow-md);
    transition: all 0.4s ease;
    animation: fadeInUp 0.6s ease both;
}

.feature-card:nth-child(1) { animation-delay: 0.1s; }
.feature-card:nth-child(2) { animation-delay: 0.2s; }
.feature-card:nth-child(3) { animation-delay: 0.3s; }
.feature-card:nth-child(4) { animation-delay: 0.4s; }
.feature-card:nth-child(5) { animation-delay: 0.5s; }
.feature-card:nth-child(6) { animation-delay: 0.6s; }

.feature-card:hover {
    transform: translateY(-10px);
    box-shadow: var(--shadow-xl);
    border-color: rgba(102, 126, 234, 0.3);
}

.feature-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    display: inline-block;
    animation: bounce 2s ease infinite;
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

.feature-card h3 {
    font-family: var(--font-display);
    font-size: 1.5rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.feature-card p {
    color: var(--text-secondary);
    line-height: 1.7;
}

/* ==================== ANALYZER SECTION ==================== */
.analyzer-section {
    max-width: 1000px;
    margin: 4rem auto;
    padding: 0 2rem;
}

.analyzer-container {
    background: var(--bg-glass);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-xl);
    padding: 3rem;
    box-shadow: var(--shadow-xl);
}

.analyzer-header {
    text-align: center;
    margin-bottom: 2.5rem;
}

.analyzer-header h2 {
    font-family: var(--font-display);
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 0.5rem;
}

.analyzer-header p {
    color: var(--text-secondary);
    font-size: 1.1rem;
}

.input-section {
    margin-bottom: 2rem;
}

.input-wrapper {
    position: relative;
    margin-bottom: 1rem;
}

#symptomInput {
    width: 100%;
    padding: 1.5rem;
    border: 2px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-lg);
    background: var(--bg-secondary);
    color: var(--text-primary);
    font-family: var(--font-body);
    font-size: 1.1rem;
    resize: vertical;
    transition: all 0.3s ease;
}

#symptomInput:focus {
    outline: none;
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}

.char-counter {
    position: absolute;
    bottom: 10px;
    right: 15px;
    color: var(--text-muted);
    font-size: 0.85rem;
}

.analyze-button {
    width: 100%;
    padding: 1.25rem 2rem;
    background: var(--gradient-primary);
    color: white;
    border: none;
    border-radius: var(--radius-lg);
    font-size: 1.2rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    box-shadow: var(--shadow-md);
}

.analyze-button:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

.analyze-button:active {
    transform: translateY(0);
}

.btn-icon {
    font-size: 1.5rem;
    transition: transform 0.3s ease;
}

.analyze-button:hover .btn-icon {
    transform: translateX(5px);
}

.quick-examples {
    margin-top: 1.5rem;
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    align-items: center;
}

.examples-label {
    color: var(--text-secondary);
    font-size: 0.9rem;
    font-weight: 500;
}

.example-chip {
    padding: 0.5rem 1rem;
    background: var(--bg-secondary);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-md);
    color: var(--text-secondary);
    font-size: 0.9rem;
    cursor: pointer;
    transition: all 0.3s ease;
}

.example-chip:hover {
    background: var(--gradient-primary);
    color: white;
    border-color: transparent;
    transform: translateY(-2px);
}

/* ==================== LOADING ANIMATION ==================== */
.loading-section {
    text-align: center;
    padding: 3rem 0;
    animation: fadeIn 0.3s ease;
}

.loading-animation {
    position: relative;
    width: 120px;
    height: 120px;
    margin: 0 auto 2rem;
}

.pulse-ring {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100%;
    height: 100%;
    border: 3px solid var(--accent-primary);
    border-radius: 50%;
    animation: pulsate 2s ease-out infinite;
}

.pulse-ring.delay-1 {
    animation-delay: 0.5s;
}

.pulse-ring.delay-2 {
    animation-delay: 1s;
}

@keyframes pulsate {
    0% {
        transform: translate(-50%, -50%) scale(0.5);
        opacity: 1;
    }
    100% {
        transform: translate(-50%, -50%) scale(1.5);
        opacity: 0;
    }
}

.loading-icon {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 3rem;
    animation: spin 3s linear infinite;
}

@keyframes spin {
    from { transform: translate(-50%, -50%) rotate(0deg); }
    to { transform: translate(-50%, -50%) rotate(360deg); }
}

.loading-text {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
}

.loading-steps {
    display: flex;
    flex-direction: column;
    gap: 0.75rem;
    max-width: 300px;
    margin: 0 auto;
}

.step {
    padding: 0.75rem;
    background: var(--bg-secondary);
    border-radius: var(--radius-md);
    color: var(--text-muted);
    font-size: 0.9rem;
    opacity: 0.5;
    transition: all 0.3s ease;
}

.step.active {
    background: var(--gradient-primary);
    color: white;
    opacity: 1;
    transform: translateX(5px);
}

/* ==================== RESULTS SECTION ==================== */
.results-section {
    margin-top: 2rem;
    animation: fadeInUp 0.6s ease;
}

.result-card {
    background: var(--bg-secondary);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-lg);
    padding: 2rem;
    margin-bottom: 1.5rem;
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
    animation: slideInUp 0.5s ease both;
}

.result-card:nth-child(1) { animation-delay: 0.1s; }
.result-card:nth-child(2) { animation-delay: 0.2s; }
.result-card:nth-child(3) { animation-delay: 0.3s; }
.result-card:nth-child(4) { animation-delay: 0.4s; }
.result-card:nth-child(5) { animation-delay: 0.5s; }
.result-card:nth-child(6) { animation-delay: 0.6s; }

@keyframes slideInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.result-card:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-lg);
}

.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1.5rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid rgba(255, 255, 255, 0.05);
}

.card-header h3 {
    font-family: var(--font-display);
    font-size: 1.5rem;
    font-weight: 700;
}

.info-badge {
    padding: 0.4rem 0.8rem;
    background: var(--gradient-primary);
    color: white;
    border-radius: var(--radius-md);
    font-size: 0.75rem;
    font-weight: 600;
}

.result-actions {
    display: flex;
    gap: 0.5rem;
}

.icon-btn {
    padding: 0.5rem;
    background: var(--bg-glass);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-sm);
    cursor: pointer;
    transition: all 0.3s ease;
    font-size: 1.2rem;
}

.icon-btn:hover {
    background: var(--gradient-primary);
    transform: scale(1.1);
}

.summary-text {
    font-size: 1.1rem;
    line-height: 1.8;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
}

.severity-indicator {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.severity-label {
    font-weight: 600;
    color: var(--text-secondary);
}

.severity-badge {
    padding: 0.5rem 1.5rem;
    border-radius: var(--radius-lg);
    font-weight: 700;
    font-size: 1rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.severity-low {
    background: var(--gradient-success);
    color: white;
}

.severity-moderate {
    background: var(--gradient-warning);
    color: #333;
}

.severity-high {
    background: var(--gradient-secondary);
    color: white;
}

.severity-critical {
    background: var(--gradient-danger);
    color: white;
    animation: pulse 2s ease infinite;
}

/* Emergency Alert */
.emergency-alert {
    background: linear-gradient(135deg, #ff0844 0%, #ff5e7e 100%);
    color: white;
    padding: 2rem;
    border-radius: var(--radius-lg);
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 1.5rem;
    box-shadow: 0 8px 32px rgba(255, 8, 68, 0.3);
    animation: emergencyPulse 2s ease infinite;
}

@keyframes emergencyPulse {
    0%, 100% {
        box-shadow: 0 8px 32px rgba(255, 8, 68, 0.3);
        transform: scale(1);
    }
    50% {
        box-shadow: 0 12px 40px rgba(255, 8, 68, 0.5);
        transform: scale(1.02);
    }
}

.emergency-icon {
    font-size: 3rem;
    animation: shake 0.5s ease infinite;
}

@keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
}

.emergency-content h3 {
    font-family: var(--font-display);
    font-size: 1.75rem;
    margin-bottom: 0.5rem;
}

.emergency-content p {
    font-size: 1.1rem;
    line-height: 1.6;
}

/* Risk Meter */
.risk-meter {
    padding: 1rem 0;
}

.risk-bar {
    width: 100%;
    height: 30px;
    background: linear-gradient(to right,
        #4facfe 0%,
        #00f2fe 25%,
        #fee140 50%,
        #fa709a 75%,
        #ff0844 100%
    );
    border-radius: var(--radius-lg);
    position: relative;
    overflow: hidden;
}

.risk-fill {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    background: rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(5px);
    transition: width 1s ease;
    border-radius: var(--radius-lg);
}

.risk-labels {
    display: flex;
    justify-content: space-between;
    margin-top: 0.75rem;
    font-size: 0.85rem;
    color: var(--text-muted);
    font-weight: 500;
}

/* Conditions List */
.condition-item {
    background: var(--bg-glass);
    padding: 1.5rem;
    border-radius: var(--radius-md);
    margin-bottom: 1rem;
    cursor: pointer;
    transition: all 0.3s ease;
    border: 1px solid rgba(255, 255, 255, 0.05);
}

.condition-item:hover {
    background: var(--bg-primary);
    transform: translateX(5px);
}

.condition-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
}

.condition-name {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--text-primary);
}

.match-percentage {
    padding: 0.4rem 1rem;
    background: var(--gradient-primary);
    color: white;
    border-radius: var(--radius-md);
    font-weight: 700;
    font-size: 0.9rem;
}

.condition-details {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    max-height: 0;
    overflow: hidden;
    transition: max-height 0.3s ease;
}

.condition-item.expanded .condition-details {
    max-height: 500px;
}

.detail-section {
    margin-bottom: 1rem;
}

.detail-section h4 {
    font-size: 1rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: var(--accent-primary);
}

.detail-section ul {
    list-style: none;
    padding-left: 0;
}

.detail-section li {
    padding: 0.3rem 0;
    color: var(--text-secondary);
}

.detail-section li::before {
    content: '• ';
    color: var(--accent-primary);
    font-weight: bold;
    margin-right: 0.5rem;
}

/* Recommendations */
.recommendation-item {
    padding: 1rem 1.5rem;
    background: var(--bg-glass);
    border-left: 4px solid var(--accent-primary);
    border-radius: var(--radius-sm);
    margin-bottom: 0.75rem;
    transition: all 0.3s ease;
}

.recommendation-item:hover {
    transform: translateX(5px);
    background: var(--bg-primary);
}

/* Sources */
.source-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1rem 1.5rem;
    background: var(--bg-glass);
    border-radius: var(--radius-md);
    margin-bottom: 0.75rem;
    transition: all 0.3s ease;
}

.source-item:hover {
    background: var(--bg-primary);
    transform: translateX(5px);
}

.source-name {
    font-weight: 600;
    color: var(--text-primary);
}

.source-link {
    color: var(--accent-primary);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.3s ease;
}

.source-link:hover {
    color: var(--accent-secondary);
    text-decoration: underline;
}

/* ==================== HISTORY SECTION ==================== */
.history-section {
    max-width: 1000px;
    margin: 4rem auto;
    padding: 0 2rem;
}

.history-container {
    background: var(--bg-glass);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-xl);
    padding: 2rem;
    box-shadow: var(--shadow-md);
}

.history-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.history-header h2 {
    font-family: var(--font-display);
    font-size: 2rem;
    font-weight: 700;
}

.clear-history-btn {
    padding: 0.6rem 1.2rem;
    background: var(--gradient-danger);
    color: white;
    border: none;
    border-radius: var(--radius-md);
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
}

.clear-history-btn:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.history-list {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.history-item {
    background: var(--bg-secondary);
    padding: 1.5rem;
    border-radius: var(--radius-md);
    border: 1px solid rgba(255, 255, 255, 0.05);
    cursor: pointer;
    transition: all 0.3s ease;
}

.history-item:hover {
    transform: translateX(5px);
    box-shadow: var(--shadow-md);
}

.empty-state {
    text-align: center;
    color: var(--text-muted);
    padding: 3rem;
    font-size: 1.1rem;
}

/* ==================== ABOUT SECTION ==================== */
.about-section {
    max-width: 1000px;
    margin: 6rem auto;
    padding: 0 2rem;
}

.about-content {
    background: var(--bg-glass);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: var(--radius-xl);
    padding: 3rem;
    box-shadow: var(--shadow-md);
}

.about-content h2 {
    font-family: var(--font-display);
    font-size: 2.5rem;
    margin-bottom: 1.5rem;
}

.about-content p {
    font-size: 1.1rem;
    line-height: 1.8;
    color: var(--text-secondary);
    margin-bottom: 1.5rem;
}

.tech-stack {
    margin-top: 3rem;
}

.tech-stack h3 {
    font-family: var(--font-display);
    font-size: 1.75rem;
    margin-bottom: 1rem;
}

.tech-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 1rem;
}

.tech-badge {
    padding: 0.75rem 1.5rem;
    background: var(--gradient-primary);
    color: white;
    border-radius: var(--radius-lg);
    font-weight: 600;
    font-size: 0.9rem;
    transition: all 0.3s ease;
}

.tech-badge:hover {
    transform: translateY(-3px);
    box-shadow: var(--shadow-md);
}

/* ==================== MODAL ==================== */
.modal {
    display: flex;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(10px);
    z-index: 2000;
    justify-content: center;
    align-items: center;
    animation: fadeIn 0.3s ease;
}

.modal-content {
    background: var(--bg-secondary);
    max-width: 600px;
    width: 90%;
    border-radius: var(--radius-xl);
    box-shadow: var(--shadow-xl);
    animation: slideInUp 0.4s ease;
}

.modal-header {
    padding: 2rem 2rem 1rem;
    border-bottom: 2px solid rgba(255, 255, 255, 0.1);
}

.modal-header h2 {
    font-family: var(--font-display);
    font-size: 1.75rem;
}

.modal-body {
    padding: 2rem;
}

.modal-body ul {
    margin: 1rem 0;
    padding-left: 1.5rem;
}

.modal-body li {
    margin-bottom: 0.75rem;
    line-height: 1.6;
}

.modal-footer-text {
    margin-top: 1.5rem;
    font-weight: 600;
    color: var(--accent-primary);
}

.modal-btn {
    width: 100%;
    padding: 1rem;
    background: var(--gradient-primary);
    color: white;
    border: none;
    border-radius: var(--radius-lg);
    font-size: 1.1rem;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.3s ease;
    margin-top: 1rem;
}

.modal-btn:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
}

/* ==================== FOOTER ==================== */
.footer {
    background: var(--bg-glass);
    backdrop-filter: blur(20px);
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    margin-top: 6rem;
    padding: 3rem 2rem 1rem;
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    margin-bottom: 2rem;
}

.footer-section h4 {
    font-family: var(--font-display);
    font-size: 1.25rem;
    margin-bottom: 1rem;
}

.footer-section a {
    display: block;
    color: var(--text-secondary);
    text-decoration: none;
    margin-bottom: 0.5rem;
    transition: color 0.3s ease;
}

.footer-section a:hover {
    color: var(--accent-primary);
}

.footer-bottom {
    max-width: 1200px;
    margin: 0 auto;
    padding-top: 2rem;
    border-top: 1px solid rgba(255, 255, 255, 0.05);
    text-align: center;
    color: var(--text-muted);
    font-size: 0.9rem;
}

/* ==================== UTILITY CLASSES ==================== */
.hidden {
    display: none !important;
}

/* ==================== RESPONSIVE DESIGN ==================== */
@media (max-width: 768px) {
    .nav-container {
        padding: 0 1rem;
    }
    
    .nav-links {
        gap: 1rem;
    }
    
    .nav-links a {
        font-size: 0.9rem;
    }
    
    .hero {
        padding: 4rem 1rem 2rem;
    }
    
    .hero-title {
        font-size: 2.5rem;
    }
    
    .hero-subtitle {
        font-size: 1rem;
    }
    
    .hero-cta {
        flex-direction: column;
    }
    
    .cta-button {
        width: 100%;
        justify-content: center;
    }
    
    .features-grid {
        grid-template-columns: 1fr;
    }
    
    .analyzer-container {
        padding: 2rem 1.5rem;
    }
    
    .analyzer-header h2 {
        font-size: 2rem;
    }
    
    .quick-examples {
        flex-direction: column;
        align-items: stretch;
    }
    
    .example-chip {
        width: 100%;
        text-align: center;
    }
    
    .card-header {
        flex-direction: column;
        align-items: flex-start;
        gap: 1rem;
    }
    
    .modal-content {
        width: 95%;
    }
    
    .footer-content {
        grid-template-columns: 1fr;
    }
}

/* ==================== ANIMATIONS ==================== */
@keyframes typing {
    from { width: 0; }
    to { width: 100%; }
}

@keyframes blink {
    50% { border-color: transparent; }
}

/* ==================== PRINT STYLES ==================== */
@media print {
    .navbar,
    .hero-cta,
    .input-section,
    .result-actions,
    .footer {
        display: none;
    }
    
    .results-section {
        box-shadow: none;
    }
}
