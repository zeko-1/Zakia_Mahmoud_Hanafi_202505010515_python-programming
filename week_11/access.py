def check_access(registered, lab_open, computer_available):

    if registered.upper() == "Y" and lab_open.upper() == "Y" and computer_available.upper() == "Y":
        return "Access Granted"

    else:
        return "Access Denied"


def get_reason(registered, lab_open, computer_available):

    if registered.upper() != "Y":
        return "Student is not registered"

    elif lab_open.upper() != "Y":
        return "Computer lab is closed"

    elif computer_available.upper() != "Y":
        return "No available computer"

    else:
        return "Welcome to the lab."