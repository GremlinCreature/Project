ticket_id=0
tickets={}
#calling ticket ID now for later use
class Ticket:
    def __init__(self, staff_id, creator_name, email, description, ticket_id, tickets):
        self.staff_id=staff_id
        self.creator_name=creator_name
        self.email=email
        self.description=description
        self.ticket_id=ticket_id
        self.tickets=tickets

    def add_new(self):
        self.ticket_id=len(self.tickets)+1
        #generating ID for the ticket
        response="Not yet provided"
        ticket_info={"Staff ID": self.staff_id,"Creator Name":self.creator_name, "Contact Email":self.email,"Description":self.description, "Response":response}
        #creating a dictionary with ticket info
        self.tickets[self.ticket_id]=ticket_info
        return self.tickets

new=Ticket(int(input("Input staff ID: ")), input("Input auithor's name: "), input("Input contact email: "), input("Input problem descrtiption: "),ticket_id, tickets)
print(new.add_new())