import joblib
from rules import rule_score

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def analyze_message(text):
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    prob = max(model.predict_proba(vec)[0])

    rule_points, reasons = rule_score(text)

    risk_score = rule_points
    if prediction == "scam":
        risk_score += int(prob * 50)

    if risk_score > 80:
        decision = "HIGH RISK"
    elif risk_score > 40:
        decision = "SUSPICIOUS"
    else:
        decision = "SAFE"

    return {
        "prediction": prediction,
        "confidence": round(prob, 2),
        "risk_score": risk_score,
        "decision": decision,
        "reasons": reasons,
        "actions": generate_actions(decision)
    }

def generate_actions(decision):
    if decision == "HIGH RISK":
        return ["Do NOT click links", "Do NOT share OTP"]
    elif decision == "SUSPICIOUS":
        return ["Verify before acting"]
    else:
        return ["Message appears safe"]