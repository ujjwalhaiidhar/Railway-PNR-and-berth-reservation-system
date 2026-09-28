# display.py
from storage import load_tickets

def search_by_pnr(pnr):
    tickets = load_tickets()
    for t in tickets:
        if t["pnr"] == pnr:
            return t
    return None

def print_chart():
    tickets = load_tickets()
    print("\n---------------- RESERVATION CHART ----------------")
    if len(tickets) == 0:
        print("No passengers booked currently.")
    else:
        for t in tickets:
            print("PNR: " + t["pnr"] + " | Name: " + t["name"] + " | Status: " + t["status"] + " | Berth: " + t["berth"])
    print("---------------------------------------------------\n")
