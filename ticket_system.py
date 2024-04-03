def main():
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
            print(" ")
            print("Displaying ticket info:")
            print("ID: ", self.ticket_id)
            print("Staff ID: ", ticket_info["Staff ID"])
            print("Creator: ", ticket_info["Creator Name"])
            print("Email: ", ticket_info["Contact Email"])
            print("Ticket description: ", ticket_info["Description"])
            print("Status: ", ticket_info["Status"])
            print("Response: ", ticket_info["Response"])

        def respond(self):
            check=0
            search_id = int(input("Input ID of a ticket you want to respond to: "))
    #Inputting ID to search for
            for i in open_tickets:
                #checks every item in the array
                for key, value in i.items():
    #checks every key and value within integrated dictionary
                    if key == search_id:
    #checks if a key corresponds to the search request
                        value["Response"]=input("Input your response: ")
                        check=1
                        question=input("Do you want to close the ticket ? (y/n): ")
    #checks if responder wants to close the ticket
                        if question=="y":
                            value["Status"]="Closed"
                            closed_tickets.append(i)
                            open_tickets.remove(i)
            if check==0:
                print("Incorrect ID. Try again.")

        def search_ticket(self):
            check=0
            search_id = int(input("Input ID of a ticket you want to view: "))
            for i in tickets:
                for key, value in i.items():
                    if key == search_id:
                        check=1
                        print("Displaying ticket info:")
                        print("ID: ", search_id)
                        print("Staff ID: ", value["Staff ID"])
                        print("Creator: ", value["Creator Name"])
                        print("Email: ", value["Contact Email"])
                        print("Ticket description: ", value["Description"])
                        print("Status: ", value["Status"])
                        print("Response: ", value["Response"])
            if check==0:
                print("Ticket not found.")
    #due to how the tickets are put into the list, the easiest way to get info would be requesting to print whatever is on the spot corresponding to requested ID-2001. Ex: ID 2005 within the array would be in the position 2005-2001, so position 4

        def display_statistics(self):
            print("Displaying ticket statistics:")
            print("Total number of tickets: ", len(tickets))
            print("Total number of solved tickets: ", len(closed_tickets))
            print("Total number of unsolved tickets: ", len(open_tickets))

        def change_status(self):
            check=0
            search_id = int(input("Input ID of a ticket you want to change the status of: "))
            for i in tickets:
                for key, value in i.items():
                    if key == search_id:
                        check=1
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
            if check==0:
                print("Incorrect ID. Try again.")
        def view_all(self):
            query=input("What tickets would you like to view ? (all, closed, open): ")
            if query=="all":
                for i in tickets:
                    for key, value in i.items():
                        print("Displaying ticket info:")
                        print("ID: ", key)
                        print("Staff ID: ", value["Staff ID"])
                        print("Creator: ", value["Creator Name"])
                        print("Email: ", value["Contact Email"])
                        print("Ticket description: ", value["Description"])
                        print("Status: ", value["Status"])
                        print("Response: ", value["Response"])
                        print("--------------------------------------------------")
            elif query=="closed":
                for i in closed_tickets:
                    for key, value in i.items():
                        print("Displaying ticket info:")
                        print("ID: ", key)
                        print("Staff ID: ", value["Staff ID"])
                        print("Creator: ", value["Creator Name"])
                        print("Email: ", value["Contact Email"])
                        print("Ticket description: ", value["Description"])
                        print("Status: ", value["Status"])
                        print("Response: ", value["Response"])
                        print("--------------------------------------------------")
            elif query=="open":
                for i in open_tickets:
                    for key, value in i.items():
                        print("Displaying ticket info:")
                        print("ID: ", key)
                        print("Staff ID: ", value["Staff ID"])
                        print("Creator: ", value["Creator Name"])
                        print("Email: ", value["Contact Email"])
                        print("Ticket description: ", value["Description"])
                        print("Status: ", value["Status"])
                        print("Response: ", value["Response"])
                        print("--------------------------------------------------")
            else: print("Incorrect input. Please, try again.")


    print("Welcome to staff ticketing system !")
    print(" ")
    print("""NOTE: this is a test version, none of the features are final.
    For testing purposes, four tickets will be automatically added into the system after this message.""")
    print(" ")
    new=Ticket("A3100" , "John Test" , "testmail@gmail.com", "This ticket tests abilit to add new tickets", ticket_id, tickets, open_tickets, closed_tickets)
    new.add_new()
    new=Ticket("P1500" , "Ariane Yeong" , "penrose-512@gmail.com", "Great holes are dug in places where earth's pores ought to sufice. And things have learnt to walk that ought to crawl.", ticket_id, tickets, open_tickets, closed_tickets)
    new.add_new()
    new=Ticket("P4500" , "Mike Password" , "nomepassowrd:c@gmail.com", "This ticket tests automatic handling of tickets concerning password change .", ticket_id, tickets, open_tickets, closed_tickets)
    new.add_new()
    new=Ticket("LSTR512" , "Replica LSTR-512" , "yeong@gmail.com", "Promise.", ticket_id, tickets, open_tickets, closed_tickets)
    new.add_new()
    print(" ")
    print(" ")
    end=0
    while end==0:
        print("What would you like to do? (input option number)")
        print(" ")
        print("1. Create new ticket.")
        print("----Support staff options ahead for testing purposes only----")
        print("2. Search ticket by ID")
        print("3. Open/close ticket")
        print("4. Respond to ticket")
        print("5. View all tickets")
        print("6. Display statistics")
        print("--------------------------------------------------")
        inpt=int(input("Input your choice: "))
        while inpt>7 or inpt<0:
            inpt = int(input("Wrong option. Please, try again: "))
        while inpt<7 and inpt>0:
            if inpt==1:
                new=Ticket(input("Input your staff ID: "), input("Input your name: "), input("Input your email: "), input("Describe your problem: "), ticket_id, tickets, open_tickets, closed_tickets)
                new.add_new()
                inpt=0
            elif inpt==2:
                new.search_ticket()
                inpt=0
            elif inpt==3:
                new.change_status()
                inpt=0
            elif inpt==4:
                new.respond()
                inpt=0
            elif inpt==5:
                new.view_all()
                inpt=0
            elif inpt==6:
                new.display_statistics()
                inpt=0
        print(" ")
        quest=input("Do you want to do anything else ? (y/n) ")
        while quest!="y" and quest!="n":
            quest = input("Incorrect input. Please, respond y/n: ")
        if quest=="n":
            end=1
main()



