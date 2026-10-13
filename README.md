# SOC Failed-Login Detection

## Project Overview
This beginner SOC project uses fictional authentication logs to practise identifying repeated failed login attempts.

## Objective
- Understand authentication logs.
- Identify repeated failed login attempts.
- Practise basic security event analysis.
- Prepare a simple incident report.

## Project Files
- `sample-auth.log` — fictional login events for practice.
- `README.md` — project overview, features, and usage instructions.
- `incident_report.md` — investigation findings and recommended actions.

## Initial Findings
The sample log contains three failed login attempts for `admin`, two for `bob`, two for `charlie`, and one successful login for `alice`. One exact duplicate log entry is also included for testing duplicate detection.

Repeated failures can be suspicious, but this small sample alone does not prove a brute-force attack.

## Tools
- GitHub for version control and project documentation.
- Python automates log analysis and flags suspicious login patterns.

## Data and Safety
All records are fictional and intended for learning. No real user credentials or private logs are used.

## Learning Status
In progress — sample log analysis, failed-login detection, invalid log validation, and duplicate log detection are implemented.
 
### Detection Features
- Parses fictional authentication log entries.
- Counts failed login attempts per user within a five-minute window.
- Flags malformed log entries and missing fields.
- Detects exact duplicate log lines and reports their count.
- Generates a review alert when a user reaches three failed attempts within the time window.

### Limitations

- This is a beginner learning project using sample logs, not a real-time monitoring system.
- Exact duplicate lines are counted separately; similar events with different timestamps are not treated as duplicates.
- An alert indicates suspicious activity for investigation; it does not prove an attack.
