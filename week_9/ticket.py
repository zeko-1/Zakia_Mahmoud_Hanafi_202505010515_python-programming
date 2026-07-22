def create_ticket():
    print("=== IT Helpdesk Ticket ===")
    name = input("Student Name: ")
    id = int(input("Student ID: "))
    issue = input("Issue: ")
    location = input("Location: ")
    priority = input("Priority(High/Medium/Low): ")

    if priority == "High":
        technician = "Ahmed"
    elif priority == "Medium":
        technician = "Siti"
    else:
        technician = "Ali"

    Status = "Pending"

    return {"name":name, 
            "id":id, 
            "issue":issue, 
            "location":location, 
            "priority":priority,
            "technician":technician,
            "status":Status
            }