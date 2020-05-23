def computegrade(score):
    while True:
        if score < 0.6:
            return "F"
        elif score < 0.7 and score >= 0.6:
            return "D"
        elif score < 0.8 and score >= 0.7:
            return "C"
        elif score < 0.9 and score >= 0.8:
            return "B"
        elif score <= 1.0 and score >= 0.9:
            return "A"
    
