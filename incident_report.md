# SOC Failed-Login Investigation

## 1. Objective
Analyse fictional authentication logs and identify repeated failed login attempts.

## 2. Data Source
- File: `sample_auth.log`
- Data: Fictional training records only.

## 3. Findings
- `admin`: 3 failed login attempts from `192.0.2.10` within 20 seconds.
- `bob`: 2 failed login attempts from `192.0.2.30` within 10 seconds.
- `alice`: 1 successful login from `192.0.2.20`.

## 4. Assessment
Repeated failed logins may indicate mistyped passwords or suspicious activity. The small sample does not prove a brute-force attack. Further investigation is needed.

## 5. Recommended Actions
1. Review surrounding authentication events.
2. Check whether the activity is expected.
3. Follow the organisation's incident-response procedures.
4. Apply appropriate account protections if suspicious activity is confirmed.

## 6. Limitations
This is a small fictional dataset, not a real security incident. The findings are for learning purposes only.

## 7. Learning Outcome
Practised reading authentication logs, counting failed attempts, and documenting findings as a beginner SOC analyst.
