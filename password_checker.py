import re

COMMON_WORDS = ['password', 'admin', '1234', 'qwerty']

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
        feedback.append("✔ Good length (12+ characters).")
    elif len(password) >= 8:
        score += 1
        feedback.append("✔ Decent length (8+ characters).")
    else:
        feedback.append("✖ Too short (less than 8 characters).")

    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✔ Contains uppercase letter.")
    else:
        feedback.append("✖ Missing uppercase letter.")

    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✔ Contains lowercase letter.")
    else:
        feedback.append("✖ Missing lowercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
        feedback.append("✔ Contains number.")
    else:
        feedback.append("✖ Missing number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("✔ Contains special character.")
    else:
        feedback.append("✖ Missing special character.")

    for word in COMMON_WORDS:
        if word in password.lower():
            feedback.append(f"✖ Contains common word: '{word}'.")
            score -= 1

    print("\nFeedback:")
    for f in feedback:
        print(f)

    print(f"\nFinal Score: {max(score, 0)}/10")
    if score >= 8:
        print("🟢 Strength: Strong")
    elif score >= 5:
        print("🟡 Strength: Moderate")
    else:
        print("🔴 Strength: Weak")

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    check_strength(pwd)
