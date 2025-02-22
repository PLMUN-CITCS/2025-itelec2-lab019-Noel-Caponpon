def problem_one(score):
    
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

score = float(input("Enter your score: "))
    if 0 <= score <= 100:
        print(f"Your Grade is: {problem_one(score)}")
    else:
        print("Invalid")