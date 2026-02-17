leads = [
    {"name": "Rohit", "industry": "Tech", "company_size": 200},
    {"name": "Amit", "industry": "Finance", "company_size": 50},
    {"name": "Priya", "industry": "Tech", "company_size": 30}
]

def calculate_score(lead):
    score = 0

    if lead["industry"] == "Tech":
        score += 20
    if lead["company_size"] >100:
        score += 30

    return score

def get_priority(score):

    if(score >= 20):
        return "High Priority"
    elif(score >=40):
        return "medium priority"
    else:
        return "Low Priority"


for lead in leads:
 score = calculate_score(lead)
 priority = get_priority(score)
    
print(lead["name"], "| Score:", score, "|", priority)