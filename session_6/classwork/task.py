data = {
    "company": "FutureTech",
    "location": {
        "city": "San Francisco",
        "country": "USA",
        "offices": [
            {"id": 1, "address": "123 Market St", "employees": 120},
            {"id": 2, "address": "42 Silicon Ave", "employees": 85},
            {"id": 3, "address": "77 Innovation Dr", "employees": 60}
        ]
    },
    "departments": [
        {
            "name": "Engineering",
            "budget": 500000,
            "teams": [
                {
                    "team_name": "Backend",
                    "lead": "E002",
                    "members": ["E002", "E003"],
                    "projects": [
                        {"id": "P101", "title": "API Upgrade", "status": "Completed"},
                        {"id": "P102", "title": "Microservice Migration", "status": "In Progress"}
                    ]
                },
                {
                    "team_name": "Frontend",
                    "lead": "E004",
                    "members": ["E004", "E005"],
                    "projects": [
                        {"id": "P103", "title": "Dashboard Redesign", "status": "Not Started"}
                    ]
                }
            ]
        },
        {
            "name": "Marketing",
            "budget": 200000,
            "teams": [
                {
                    "team_name": "Content",
                    "lead": "E006",
                    "members": ["E006", "E007", "E008"],
                    "projects": [
                        {"id": "P201", "title": "Blog Launch", "status": "Completed"},
                        {"id": "P202", "title": "Brand Awareness", "status": "In Progress"}
                    ]
                }
            ]
        }
    ],
    "employees": {
        "E002": {"name": "Alice", "role": "Backend Engineer", "age": 25, "location": 1},
        "E003": {"name": "Bob", "role": "DevOps Engineer", "age": 27, "location": 1},
        "E004": {"name": "Clara", "role": "Frontend Engineer", "age": 24, "location": 2},
        "E005": {"name": "David", "role": "Frontend Engineer", "age": 28, "location": 2},
        "E006": {"name": "Emma", "role": "Content Lead", "age": 30, "location": 3},
        "E007": {"name": "Fiona", "role": "Content Writer", "age": 26, "location": 3},
        "E008": {"name": "George", "role": "SEO Specialist", "age": 31, "location": 3}
    },
    "policies": {
        "remote_work": True,
        "vacation_days": 20,
        "bonus_eligibility": ["Engineering", "Marketing"]
    }
}


# task 1
# for department in data["departments"]:
#     print(f"Department - {department['name']}: ")
#     for team in department['teams']:
#         for project in team['projects']:
#             print(f"Project - {project['title']}")

# task2 

# print 
# <project_name> team is led by <name of the person>(<role>)


# ouput 
# backend team is led by Alice (Backend engineer)


# for department in data["departments"]:
#     for team in department["teams"]:
#         print(f"Team: {team['team_name']} is led by ")

# for dep in data["departments"]:

for dep in data["departments"]:
    for team in dep['teams']:
        lead = data['employees'][team['lead']]       

        print(f"{team['team_name']} is led by {lead['name']} ({lead['role']})")

