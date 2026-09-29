import re


def check_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, feedback


print("===================================")
print("     PASSWORD STRENGTH ANALYZER")
print("===================================")

password = input("Enter your password: ")

score, strength, feedback = check_password(password)

print("\nPassword Strength:", strength)
print("Score:", score, "/ 5")

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)
else:
    print("\nExcellent! Your password satisfies all basic checks.")