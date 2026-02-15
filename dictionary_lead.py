# Mini Task – Lead Scoring System

""""
Rules:

Industry Tech → +20

Company size > 100 → +30

Otherwise → 0

Add one more rule:
If score >= 40 → "High Priority"
If score between 20–39 → "Medium Priority"
Else → "Low Priority"
"""

leads = [
    {"name": "Rohit", "industry":"Tech", "company_size":110},
    {"name": "Harsh", "industry":"Financial", "company_size":50},
    {"name": "samay", "industry":"Tech", "company_size":130},
]

for lead in leads:
    score = 0

if lead["industry"] == "Tech" :
    score += 20

if lead["company_size"] >100:
    score += 30

 # Priority decision
if score >= 40:
    priority = "High Priority"
elif score >= 20:
    priority = "Medium Priority"
else:
    priority = "Low Priority"

print(lead["name"], "Score:",score)