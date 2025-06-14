# 🔐 Password Strength Checker

## 🧠 Task Objective
The goal of this project is to create a **Password Strength Checker** that evaluates the quality of a user's password and provides:
- A score (0 to 100)
- A strength label (Weak, Moderate, Strong)
- Detailed feedback on what makes the password secure or insecure

The primary aim is to promote stronger password habits among users.

---

## 🛠️ Approach
The script uses **regular expressions** to evaluate several aspects of the password:
- ✅ Length (short, moderate, or strong)
- ✅ Presence of uppercase and lowercase letters
- ✅ Use of numbers and special characters
- ❌ Detection of common weak passwords (e.g., `123456`, `password`)

Each criterion contributes to a score, and based on the final score, the password is classified as:
- **Strong 🔒** (Score ≥ 80)
- **Moderate 🟠** (Score ≥ 50 and < 80)
- **Weak 🔴** (Score < 50)

The script uses the `getpass` module to securely input the password without showing it on the screen.

---

## 🧰 Tools Used
- **Python**: Main programming language
- **re (Regular Expressions)**: For pattern matching
- **getpass**: For secure password entry (hides input)

---

## 📚 What I Learned
- How to use **regular expressions** for text validation and pattern detection.
- How to structure a scoring system based on password complexity.
- The importance of **user feedback** in guiding better password practices.
- How to use `getpass` to protect user input in terminal-based scripts.

---

## ▶️ How to Run

```bash
python password_strength_checker.py
