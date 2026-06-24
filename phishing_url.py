import re
from urllib.parse import urlparse


# Suspicious keywords commonly found in phishing URLs
suspicious_keywords = [
    "login",
    "verify",
    "verification",
    "update",
    "secure",
    "account",
    "bank",
    "password",
    "signin",
    "confirm",
    "wallet",
    "payment"
]


def check_url_length(url):

    if len(url) > 75:
        return 1, "Long URL detected"

    return 0, "URL length looks normal"



def check_https(url):

    if url.startswith("https://"):
        return 0, "HTTPS enabled"

    return 1, "HTTPS missing"



def check_special_characters(url):

    special_chars = ['@', '-', '_', '?', '%']

    count = 0

    for char in special_chars:
        count += url.count(char)


    if count >= 3:
        return 1, "Many special characters detected"

    return 0, "Special characters look normal"



def check_keywords(url):

    found_keywords = []

    url = url.lower()


    for word in suspicious_keywords:

        if word in url:
            found_keywords.append(word)


    if found_keywords:

        return 1, f"Suspicious keywords found: {', '.join(found_keywords)}"


    return 0, "No suspicious keywords found"



def check_ip_address(url):

    ip_pattern = r"https?://(\d{1,3}\.){3}\d{1,3}"

    if re.search(ip_pattern, url):

        return 1, "IP address used instead of domain"


    return 0, "Domain name detected"



def check_subdomains(url):

    domain = urlparse(url).netloc

    dots = domain.count(".")


    if dots > 3:

        return 1, "Too many subdomains detected"


    return 0, "Subdomain structure looks normal"



def analyze_url(url):

    risk_score = 0


    print("\nURL Analysis")
    print("-" * 40)


    checks = [

        check_url_length(url),
        check_https(url),
        check_special_characters(url),
        check_keywords(url),
        check_ip_address(url),
        check_subdomains(url)

    ]


    for score, message in checks:

        print(message)

        risk_score += score



    print("\nRisk Score:", risk_score, "/ 6")


    print("-" * 40)



    if risk_score > 4:

        print(" Result: HIGH CHANCE OF PHISHING URL")


    elif risk_score >2 & risk_score <= 3:

        print(" Result: POSSIBLE PHISHING URL")


    else:

        print(" Result: LOW RISK URL")




print("""
------------------------------------
       PHISHING URL DETECTOR
------------------------------------
""")


url = input("Enter URL to analyze: ")



if not url.startswith(("http://", "https://")):

    url = "http://" + url



analyze_url(url)