ticket_id=0
tickets=[]
open_tickets=[]
closed_tickets=[]
#calling ticket ID and all the tickets dictionaries now for later use
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
        self.ticket_id=len(self.tickets)+2001
#generating ID for the ticket
        response="Not yet provided"
        ticket_info={"Staff ID": self.staff_id,"Creator Name":self.creator_name, "Contact Email":self.email,"Description":self.description,"Status": "Open", "Response":response}
#creating a dictionary with ticket info
        description_lower_case=self.description.lower()
#converting all letters in description to lower case
        words = description_lower_case.split()
#splitting description into a list of single words
        if "password" in words and "change" in words:
            ticket_info["Status"] = "Closed"
            ticket_info["Response"] = "Your new password is: " + self.staff_id[:2] + self.creator_name[:3]
        if "password" in words and "change," in words:
            ticket_info["Status"] = "Closed"
            ticket_info["Response"] = "Your new password is: " + self.staff_id[:2] + self.creator_name[:3]
        if "password," in words and "change" in words:
            ticket_info["Status"] = "Closed"
            ticket_info["Response"] = "Your new password is: " + self.staff_id[:2] + self.creator_name[:3]
        if "password" in words and "change." in words:
            ticket_info["Status"] = "Closed"
            ticket_info["Response"] = "Your new password is: " + self.staff_id[:2] + self.creator_name[:3]
        if "password." in words and "change" in words:
            ticket_info["Status"] = "Closed"
            ticket_info["Response"] = "Your new password is: " + self.staff_id[:2] + self.creator_name[:3]
        if "password" in words and "change?" in words:
            ticket_info["Status"] = "Closed"
            ticket_info["Response"] = "Your new password is: " + self.staff_id[:2] + self.creator_name[:3]
        if "password?" in words and "change" in words:
            ticket_info["Status"] = "Closed"
            ticket_info["Response"] = "Your new password is: " + self.staff_id[:2] + self.creator_name[:3]
        if "password" in words and "change!" in words:
            ticket_info["Status"] = "Closed"
            ticket_info["Response"] = "Your new password is: " + self.staff_id[:2] + self.creator_name[:3]
        if "password!" in words and "change" in words:
            ticket_info["Status"] = "Closed"
            ticket_info["Response"] = "Your new password is: " + self.staff_id[:2] + self.creator_name[:3]
#Here i had a choice - i could research "translate" function to remove all punctuation or i could just add some extra variations. I've decided to add more variations.
#Giving the user new password
        ticket={self.ticket_id:ticket_info}
        tickets.append(ticket)
        if ticket_info["Status"]=="Open":
            open_tickets.append(ticket)
        elif ticket_info["Status"]=="Closed":
            closed_tickets.append(ticket)
        print("New ticket created.")

    def respond(self):
        search_id = int(input("Input ID of a ticket you want to respond to: "))
#Inputting ID to search for
        for i in open_tickets:
            #checks every item in the array
            for key, value in i.items():
#checks every key and value within integrated dictionary
                if key == search_id:
#checks if a key corresponds to the search request
                    value["Response"]=input("Input your response: ")
                    question=input("Do you want to close the ticket ? (y/n): ")
#checks if responder wants to close the ticket
                    if question=="y":
                        value["Status"]="Closed"
                        closed_tickets.append(i)
                        open_tickets.remove(i)
                else: print("Incorrect ID. Please, try again.")
#error in case someone inputs a wrong id

    def search_ticket(self):
        search_id = int(input("Input ID of a ticket you want to view: "))
        for i in tickets:
            for key, value in i.items():
                if key == search_id:
                    print("Displaying ticket info:")
                    print("ID: ", search_id)
                    print("Staff ID: ", value["Staff ID"])
                    print("Creator: ", value["Creator Name"])
                    print("Email: ", value["Contact Email"])
                    print("Ticket description: ", value["Description"])
                    print("Status: ", value["Status"])
                    print("Response: ", value["Response"])
#due to how the tickets are put into the list, the easiest way to get info would be requesting to print whatever is on the spot corresponding to requested ID-2001. Ex: ID 2005 within the array would be in the position 2005-2001, so position 4

    def display_statistics(self):
        print("Displaying ticket statistics:")
        print("Total number of tickets: ", len(tickets))
        print("Total number of solved tickets: ", len(closed_tickets))
        print("Total number of unsolved tickets: ", len(open_tickets))

    def change_status(self):
        search_id = int(input("Input ID of a ticket you want to change the status of: "))
        for i in tickets:
            for key, value in i.items():
                if key == search_id:
                    if value["Status"] == "Open":
                        question = input("Do you want to close the ticket ? (y/n): ")
                        if question == "y":
                            value["Status"] = "Closed"
                            closed_tickets.append(i)
                            open_tickets.remove(i)
                    elif value["Status"] == "Closed":
                        question = input("Do you want to re-open the ticket ? (y/n): ")
                        if question == "y":
                            value["Status"] = "Open"
                            closed_tickets.remove(i)
                            open_tickets.append(i)

new=Ticket(input("Input staff ID: "), input("Input author's name: "), input("Input contact email: "), input("Input problem descrtiption: "),ticket_id, tickets, open_tickets, closed_tickets)
new.add_new()
new.search_ticket()