
from collections import defaultdict

from datetime import datetime, timedelta

LOG_FILE = "sample-auth.log"

TIME_WINDOW_MINUTES = 5

failed_logins = defaultdict(list)
latest_timestamp = None
invalid_logs = 0
seen_logs = set()
duplicate_logs = 0
with open(LOG_FILE, "r", encoding="utf-8") as file:
    for line in file:
        fields = line.split()
        log_key = line.strip()

        if log_key in seen_logs:
            duplicate_logs += 1
            continue
        else:
            seen_logs.add(log_key)
        timestamp_text = " ".join(fields[:2])

        try:
            timestamp = datetime.strptime(
                timestamp_text, "%Y-%m-%d %H:%M:%S"
            )
        except ValueError:
            invalid_logs += 1
            continue

        if latest_timestamp is None or timestamp > latest_timestamp:
           latest_timestamp = timestamp

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
        if not user or not status:
            invalid_logs += 1
            continue

        if status not in ("FAILED", "SUCCESS"): 
             invalid_logs += 1
             continue

        
        
        if user and status == "FAILED":
            failed_logins[user].append(timestamp)



print("SOC Failed-Login Detection")
print("--------------------------")
print(f"Invalid log entries: {invalid_logs}")
print(f"Duplicate log entries: {duplicate_logs}")

if not failed_logins:
    print("No failed login attempts found.")


for username, timestamps in sorted(failed_logins.items()):
    recent_cutoff = latest_timestamp - timedelta(
        minutes=TIME_WINDOW_MINUTES
    )

    recent_count = sum(
        1 for timestamp in timestamps
        if recent_cutoff <= timestamp <= latest_timestamp
    )

    print(f"{username}: {recent_count} failed login attempts in the last {TIME_WINDOW_MINUTES} minutes")

    if recent_count >= 3:
        print("  ALERT: Review this account")

