

import re
exclude_emails = []
exclude_domains = "exclude.com"


text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)

def excluded_emails():
    for email in emails:
        if not email.endswith(f"@exclude.com"):
            exclude_emails.append(email)
    print(exclude_emails)

excluded_emails()
