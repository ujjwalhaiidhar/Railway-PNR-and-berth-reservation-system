# storage.py
from config import DATA_FILE

def load_tickets():
    tickets = []
    try:
        f = open(DATA_FILE, "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                ticket = {
                    "pnr": parts[0],
                    "name": parts[1],
                    "age": parts[2],
                    "gender": parts[3],
                    "status": parts[4],
                    "berth": parts[5]
                }
                tickets.append(ticket)
    except FileNotFoundError:
        f = open(DATA_FILE, "w")
        f.close()
    return tickets

def save_tickets(tickets):
    f = open(DATA_FILE, "w")
    for t in tickets:
        row = t["pnr"] + "," + t["name"] + "," + str(t["age"]) + "," + t["gender"] + "," + t["status"] + "," + str(t["berth"]) + "\n"
        f.write(row)
    f.close()
