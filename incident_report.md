# SOC Failed-Login Investigation

## 1. Objective
Analyse fictional authentication logs and identify repeated failed login attempts.
## 2. Data Source
- File: sample-auth.log
- Data: Fictional training records only.
## 3. Findings
- `admin`: 3 failed login attempts from `192.0.2.10`.
- `bob`: 2 failed login attempts from `192.0.2.30`.
- `charlie`: 2 failed login attempts from `192.0.2.40`.
- `alice`: 1 successful login from `192.0.2.20`.
- Exact duplicate log entries detected: 1. The duplicate is reported separately and is not counted again as a failed-login attempt.
## 4. Assessment
Repeated failed logins may indicate mistyped passwords or suspicious activity. The small sample does not prove a brute-force attack. Further investigation is needed.
## 5. Recommended Actions
1. Review surrounding authentication events.
2. Check whether the activity is expected.
3. Follow the organisation's incident-response procedures.
4. Apply appropriate account protections if suspicious activity is confirmed.
## 6. Limitations
This is a small fictional dataset, not a real security incident.
 The findings are for learning purposes only.
## 7. Learning Outcome
Practised authentication log analysis, five-minute failed-login detection, malformed log validation, missing-field validation, and exact duplicate-line detection. Learned to generate review alerts and document findings while recognising that alerts do not prove an attack.