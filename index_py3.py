import re

def check_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("🔸 Password should be at least 8 characters long.")

    # Check for lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("🔸 Add lowercase letters.")

    # Check for uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("🔸 Add uppercase letters.")

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("🔸 Add numbers.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("🔸 Add special characters (e.g. !, @, #, etc).")

    # Final judgment
    if strength == 5:
        verdict = "✅ Strong password!"
    elif 3 <= strength < 5:
        verdict = "⚠ Moderate password. Consider improving it."
    else:
        verdict = "❌ Weak password. Needs major improvements."

    return verdict, feedback

def main():
    print("=== Password Complexity Checker ===")
    password = input("Enter a password to check: ")

    verdict, suggestions = check_password_strength(password)
    print("\n🔍 Result:")
    print(verdict)

    if suggestions:
        print("\n💡 Suggestions to improve:")
        for tip in suggestions:
            print(tip)

if __name__ == "__main__":
    main()