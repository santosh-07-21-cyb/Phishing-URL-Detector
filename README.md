# Phishing-URL-Detector
Python-based phishing URL detector that analyzes URL patterns and assigns risk scores to identify suspicious websites.

---

## Features

- Detects suspicious phishing URL patterns
- Analyzes URL characteristics
- Generates a risk score based on detected threats
- Classifies URLs as:
  - Low Risk
  - Possible Phishing
  - High Chance of Phishing

---

## Technologies Used

- Python
- **Libraries:**
  - re (Regular Expressions)
  - urllib (URL Parsing)

---

## How It Works

The detector follows a rule-based analysis approach:

```
User URL Input
        |
        ↓
URL Feature Extraction
        |
        ↓
Security Rule Checking
        |
        ↓
Risk Score Calculation
        |
        ↓
Phishing Detection Result
```

---

## Detection Parameters

The tool analyzes multiple URL features:

| Feature | Description |
|---------|-------------|
| URL Length | Detects unusually long URLs |
| HTTPS Check | Identifies missing secure connections |
| Keywords | Detects words like login, verify, update, password |
| Special Characters | Checks suspicious symbols in URLs |
| IP Address | Detects URLs using IP addresses instead of domains |
| Subdomains | Identifies excessive subdomain usage |

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/phishing_url.git
```

### Navigate to Project Directory

```bash
cd phishing_url
```

### Check Python Installation

```bash
python --version
```

No external libraries are required because the project uses built-in Python modules.

---

## Usage

Run the program:

```bash
python phishing_url.py
```
