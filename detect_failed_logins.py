
from collections import defaultdict

LOG_FILE = "sample-auth.log"

failed_logins = defaultdict(int)

with open(LOG_FILE, "r", encoding="utf-8") as file:
    for line in file:
        fields = line.split()

        user = next(
            (item.split("=", 1)[1] for item in fields
             if item.startswith("user=")),
            None
        )

        status = next(
            (item.split("=", 1)[1] for item in fields
             if item.startswith("status=")),
            None
        )

        if user and status == "FAILED":
            failed_logins[user] += 1

print("SOC Failed-Login Detection")
print("--------------------------")

if not failed_logins:
    print("No failed login attempts found.")

for username, count in sorted(failed_logins.items()):
    print(f"{username}: {count} failed login attempts")

    if count >= 3:
        print("  ALERT: Review this account")
