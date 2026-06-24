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
## Sample Output


### LOW RISK EXAMPLE : 

<img width="502" height="405" alt="sc_1" src="https://github.com/user-attachments/assets/f6ceb46f-8e43-40a6-a0ef-0d2a5bc7d749" />

### POSSIBLE PHISHING EXAMPLE :

<img width="512" height="401" alt="sc_2" src="https://github.com/user-attachments/assets/b15f50d6-fd72-45d1-902d-a0785077d274" />

### HIGH CHANCE OF PHISHING EXAMPLE :

<img width="967" height="411" alt="sc_3" src="https://github.com/user-attachments/assets/f8a109b3-51cb-487e-af85-7fa26449a080" />
