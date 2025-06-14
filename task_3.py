import re
from getpass import getpass

def check_password_strength(password):
    """Analyze password strength and return a score (0-100) and feedback."""
    score = 0
    feedback = []

    # Length check (8+ chars)
    if len(password) >= 12:
        score += 30
        feedback.append("✓ Long (12+ characters)")
    elif len(password) >= 8:
        score += 20
        feedback.append("✓ Moderate length (8+ characters)")
    else:
        feedback.append("✗ Too short (min 8 characters)")

    # Uppercase letters
    if re.search(r'[A-Z]', password):
        score += 15
        feedback.append("✓ Contains uppercase letters")
    else:
        feedback.append("✗ Missing uppercase letters")

    # Lowercase letters
    if re.search(r'[a-z]', password):
        score += 15
        feedback.append("✓ Contains lowercase letters")
    else:
        feedback.append("✗ Missing lowercase letters")

    # Numbers
    if re.search(r'[0-9]', password):
        score += 15
        feedback.append("✓ Contains numbers")
    else:
        feedback.append("✗ Missing numbers")

    # Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 20
        feedback.append("✓ Contains special characters")
    else:
        feedback.append("✗ Missing special characters")

    # Common password check
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() in common_passwords:
        score = 0
        feedback.append("✗ Common password (easily guessable)")

    # Score interpretation
    if score >= 80:
        strength = "Strong 🔒"
    elif score >= 50:
        strength = "Moderate 🟠"
    else:
        strength = "Weak 🔴"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

def main():
    print("=== Password Strength Checker ===")
    password = getpass("Enter password: ")
    result = check_password_strength(password)

    print("\n--- Results ---")
    print(f"Strength: {result['strength']} (Score: {result['score']}/100)")
    print("\nDetailed Feedback:")
    for item in result["feedback"]:
        print(f"- {item}")

if __name__ == "__main__":
    main()