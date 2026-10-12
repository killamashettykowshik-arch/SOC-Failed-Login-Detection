# SOC Failed-Login Detection

## Project Overview
This beginner SOC project uses fictional authentication logs to practise identifying repeated failed login attempts.

## Objective
- Understand authentication logs.
- Identify repeated failed login attempts.
- Practise basic security event analysis.
- Prepare a simple incident report.

## Project Files
- `sample_auth.log` — fictional login events for practice.
- `README.md` — project overview and documentation.
- `incident_report.md` — investigation findings (to be added).

## Initial Findings
The sample log contains three failed login attempts for `admin` and two for `bob`. The `alice` account has one successful login.

Repeated failures can be suspicious, but this small sample alone does not prove a brute-force attack.

## Tools
- GitHub for version control and project documentation.
- Python will be added later to automate log analysis.

## Data and Safety
All records are fictional and intended for learning. No real user credentials or private logs are used.

## Learning Status
In progress — sample authentication logs have been added. Incident reporting and Python-based detection are planned next.
