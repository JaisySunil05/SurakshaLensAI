import joblib
from rules import rule_score

# Load ML assets
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
vectorizer = joblib.load(os.path.join(BASE_DIR, "vectorizer.pkl"))


def analyze_message(text):

    # ML Layer
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]  # "scam" or "ham"
    prob = max(model.predict_proba(vec)[0])  # 0–1

    # Rule Layer
    rule_points, rule_reasons = rule_score(text)

    # Combine Scores
    risk_score = rule_points

    if prediction.lower() == "scam":
        risk_score += int(prob * 50)

    risk_score = min(risk_score, 100)

    # Decision (IMPORTANT for frontend)
    if risk_score >= 70:
        decision = "SCAM"
    elif risk_score >= 40:
        decision = "SUSPICIOUS"
    else:
        decision = "SAFE"

    reasons = list(set(rule_reasons))

    if prediction.lower() == "scam":
        reasons.append("ML model detected scam pattern")

    return {
        "risk_score": risk_score,
        "decision": decision,
        "reasons": reasons
    }