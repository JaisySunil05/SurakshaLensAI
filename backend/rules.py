def rule_score(text):
    score = 0
    reasons = []
    text = text.lower()

    groups = {
        "Critical Credential Request": {
            "keywords": ["otp", "password", "pin", "cvv", "share"],
            "weight": 40
        },
        "Financial/KYC Impersonation": {
            "keywords": ["kyc", "bank", "pan card", "income tax", "aadhar", "recharge"],
            "weight": 30
        },
        "Urgency & Panic": {
            "keywords": ["urgent", "immediately", "expired", "blocked", "last warning"],
            "weight": 25
        },
        "Suspicious Call-to-Action": {
            "keywords": ["click", "verify", "update", "link", "claim", "won"],
            "weight": 20
        }
    }

    for group_name, data in groups.items():
        if any(word in text for word in data["keywords"]):
            score += data["weight"]
            reasons.append(group_name)

    return score, reasons