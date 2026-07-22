from ticket import create_ticket
from display import display_ticket

def Main():
    ticket_data = create_ticket()
    display_ticket(ticket_data)

if __name__ == "__main__":
    Main()