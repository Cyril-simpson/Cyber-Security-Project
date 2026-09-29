import random


emails = [
    {
        "subject": "URGENT: Your account will be closed!",
        "sender": "security@example.invalid",
        "body": """
Dear User,

Your account will be permanently closed today.
Verify your account immediately to avoid losing access.

Click here to verify your account.

Regards,
Security Team
""",
        "answer": "phishing",
        "reasons": [
            "Uses urgent and threatening language.",
            "Asks the user to verify an account immediately.",
            "The sender uses a fictional .invalid domain."
        ]
    },

    {
        "subject": "You have won a prize!",
        "sender": "winner@example.invalid",
        "body": """
Congratulations!

You have been selected as the winner of a special prize.
Send your personal information to claim your prize.

Thank you.
""",
        "answer": "phishing",
        "reasons": [
            "Unexpected prize claim.",
            "Requests personal information.",
            "The message creates excitement to encourage quick action."
        ]
    },

    {
        "subject": "Weekly Library Newsletter",
        "sender": "library@example.edu",
        "body": """
Hello,

Here is this week's library newsletter.

New books and study resources are now available.
You can visit the library website when convenient.

Regards,
Library Team
""",
        "answer": "safe",
        "reasons": [
            "No urgent request.",
            "Does not ask for passwords or sensitive information.",
            "The message provides ordinary informational content."
        ]
    }
]


def show_email(email):
    print("\n" + "=" * 60)
    print("EMAIL")
    print("=" * 60)

    print("From:", email["sender"])
    print("Subject:", email["subject"])

    print("\nMessage:")
    print(email["body"])


def run_simulation():
    print("=" * 60)
    print("       PHISHING EMAIL AWARENESS SIMULATOR")
    print("=" * 60)

    print("\nThis is an educational simulation.")
    print("No real emails are sent and no passwords are collected.")

    score = 0

    selected_emails = random.sample(emails, len(emails))

    for number, email in enumerate(selected_emails, start=1):

        print(f"\n\nEmail {number} of {len(selected_emails)}")

        show_email(email)

        print("\nIs this email:")
        print("1. Phishing")
        print("2. Safe")

        choice = input("Your answer: ").strip()

        if choice == "1":
            answer = "phishing"
        elif choice == "2":
            answer = "safe"
        else:
            print("Invalid choice.")
            continue

        if answer == email["answer"]:
            print("\nCorrect!")
            score += 1
        else:
            print("\nNot quite.")

        print("\nWhy?")

        for reason in email["reasons"]:
            print("-", reason)

    print("\n" + "=" * 60)
    print("SIMULATION COMPLETE")
    print("=" * 60)

    print(f"Your score: {score}/{len(selected_emails)}")

    if score == len(selected_emails):
        print("Excellent awareness!")
    elif score >= 2:
        print("Good awareness. Keep checking suspicious messages carefully.")
    else:
        print("Review the warning signs of phishing emails.")


run_simulation()