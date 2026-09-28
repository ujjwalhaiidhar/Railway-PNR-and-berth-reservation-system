# booking.py
# Core booking engine

import random
from config import MAX_CONFIRMED, MAX_RAC, MAX_WAITLIST
from storage import load_tickets, save_tickets

def generate_pnr():
    return str(random.randint(10000, 99999))

def book_passenger(name, age, gender, berth_pref):
    tickets = load_tickets()

    cnf_count = 0
    rac_count = 0
    wl_count = 0

    for t in tickets:
        if t["status"] == "CONFIRMED":
            cnf_count = cnf_count + 1
        elif "RAC" in t["status"]:
            rac_count = rac_count + 1
        elif "WL" in t["status"]:
            wl_count = wl_count + 1

    pnr = generate_pnr()

    # 1. Confirmed berth allocation
    if cnf_count < MAX_CONFIRMED:
        seat_no = cnf_count + 1
        
        # Senior citizens get Lower berth preference
        if int(age) >= 60:
            assigned_berth = "Lower"
        elif berth_pref != "":
            assigned_berth = berth_pref
        else:
            assigned_berth = "Middle"

        ticket = {
            "pnr": pnr,
            "name": name,
            "age": age,
            "gender": gender,
            "status": "CONFIRMED",
            "berth": str(seat_no) + "-" + assigned_berth
        }
        tickets.append(ticket)
        save_tickets(tickets)
        return ticket

    # 2. RAC allocation
    elif rac_count < MAX_RAC:
        rac_no = rac_count + 1
        ticket = {
            "pnr": pnr,
            "name": name,
            "age": age,
            "gender": gender,
            "status": "RAC-" + str(rac_no),
            "berth": "Side-Seat"
        }
        tickets.append(ticket)
        save_tickets(tickets)
        return ticket

    # 3. Waiting List allocation
    elif wl_count < MAX_WAITLIST:
        wl_no = wl_count + 1
        ticket = {
            "pnr": pnr,
            "name": name,
            "age": age,
            "gender": gender,
            "status": "WL-" + str(wl_no),
            "berth": "None"
        }
        tickets.append(ticket)
        save_tickets(tickets)
        return ticket

    # 4. All categories full
    else:
        return None
