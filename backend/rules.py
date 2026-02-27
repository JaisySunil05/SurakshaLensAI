def rule_score(text):
    score = 0
    reasons = []

    text = text.lower()
    keywords = ["otp", "kyc", "urgent", "click", "verify"]

    for word in keywords:
        if word in text:
            score += 20
            reasons.append(word)

    return score, reasons