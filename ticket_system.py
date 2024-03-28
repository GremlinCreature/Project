ticket_id=0
tickets=[]
open_tickets=[]
closed_tickets=[]
#calling ticket ID now for later use
class Ticket:
    def __init__(self, staff_id, creator_name, email, description, ticket_id, tickets, open_tickets, closed_tickets):
        self.staff_id=staff_id
        self.creator_name=creator_name
        self.email=email
        self.description=description
        self.ticket_id=ticket_id
        self.tickets=tickets
        self.open_tickets=open_tickets
        self.closed_tickets=closed_tickets

    def add_new(self):
        self.ticket_id=len(self.tickets)+1
        #generating ID for the ticket
        response="Not yet provided"
        ticket_info={"Staff ID": self.staff_id,"Creator Name":self.creator_name, "Contact Email":self.email,"Description":self.description,"Status": "Open", "Response":response}
        #creating a dictionary with ticket info
        ticket={self.ticket_id:ticket_info}
        tickets.append(ticket)
        open_tickets.append(ticket)

new=Ticket(int(input("Input staff ID: ")), input("Input auithor's name: "), input("Input contact email: "), input("Input problem descrtiption: "),ticket_id, tickets, open_tickets, closed_tickets)
new.add_new()
print(tickets)
print(open_tickets)