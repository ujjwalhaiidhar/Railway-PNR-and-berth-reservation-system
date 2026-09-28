# main.py
from booking import book_passenger
from cancel import cancel_passenger_ticket
from display import search_by_pnr, print_chart

def run():
    while True:
        print("====== RAILWAY RESERVATION SYSTEM ======")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. Check PNR Status")
        print("4. View Reservation Chart")
        print("5. Exit")

        choice = input("Enter choice (1-5): ").strip()

        if choice == "1":
            name = input("Enter passenger name: ").strip()
            if name == "":
                print("Name cannot be empty.\n")
                continue

            age_str = input("Enter passenger age: ").strip()
            if not age_str.isdigit():
                print("Invalid age. Enter digits only.\n")
                continue

            gender = input("Enter gender (M/F/O): ").strip().upper()
            pref = input("Enter berth preference (Lower/Middle/Upper): ").strip().capitalize()

            ticket = book_passenger(name, age_str, gender, pref)
            if ticket != None:
                print("\n>>> Ticket Booked Successfully! <<<")
                print("PNR Number : " + ticket["pnr"])
                print("Status     : " + ticket["status"])
                print("Seat/Berth : " + ticket["berth"] + "\n")
            else:
                print("\n>>> Regret: Confirmed, RAC, and Waiting List are all full! <<<\n")

        elif choice == "2":
            pnr = input("Enter PNR to cancel: ").strip()
            success, msg = cancel_passenger_ticket(pnr)
            print(">>> " + msg + "\n")

        elif choice == "3":
            pnr = input("Enter PNR to check: ").strip()
            t = search_by_pnr(pnr)
            if t != None:
                print("\n--- PNR DETAILS ---")
                print("PNR    : " + t["pnr"])
                print("Name   : " + t["name"])
                print("Age    : " + t["age"])
                print("Status : " + t["status"])
                print("Berth  : " + t["berth"] + "\n")
            else:
                print(">>> PNR not found.\n")

        elif choice == "4":
            print_chart()

        elif choice == "5":
            print("Thank you for using the railway system. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number from 1 to 5.\n")

if __name__ == "__main__":
    run()
