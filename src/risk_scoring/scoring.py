def calculate_risk_score(rules_triggered):
    score = 0
    for rule in rules_triggered:
        score += 20
    return score
