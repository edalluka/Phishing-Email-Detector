
import re


def analyze_email(email):

    suspicious_keywords = [
        "urgent",
        "verify your account",
        "password",
        "click here",
        "account suspended",
        "bank details",
        "confirm your identity"
    ]

    score = 0
    findings = []
    email_lower = email.lower()

    # Detect suspicious keywords
    for keyword in suspicious_keywords:
        if keyword in email_lower:
            score += 10
            findings.append(
                f"Suspicious keyword detected: {keyword}"
            )

    # Detect URLs
    urls = re.findall(r'https?://\S+', email)

    if urls:
        for url in urls:
            findings.append(f"URL detected: {url}")

    # Classify email
    if score >= 40:
        risk = "Phishing"
    elif score >= 20:
        risk = "Suspicious"
    else:
        risk = "Low Risk"

    return score, risk, findings


# Test email
sample_email = """
URGENT! Your account has been suspended.
Verify your account immediately.
Click here: http://example.com/login
"""

# Analyze email
score, risk, findings = analyze_email(sample_email)

# Display results
print("PHISHING EMAIL DETECTOR")
print("-----------------------")
print("Risk Score:", score)
print("Risk Level:", risk)

print("\nFindings:")

for finding in findings:
    print("-", finding)
