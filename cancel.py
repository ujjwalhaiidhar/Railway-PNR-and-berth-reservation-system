# cancel.py
# Handles ticket cancellations and queue shifting

from storage import load_tickets, save_tickets

def cancel_passenger_ticket(pnr):
    tickets = load_tickets()
    found_idx = -1

    for i in range(len(tickets)):
        if tickets[i]["pnr"] == pnr:
            found_idx = i
            break

    if found_idx == -1:
        return False, "PNR not found in records."

    deleted = tickets.pop(found_idx)

    # If cancelled ticket was confirmed, promote first RAC person
    if deleted["status"] == "CONFIRMED":
        vacated_berth = deleted["berth"]
        promoted_rac = False

        for t in tickets:
            if "RAC" in t["status"] and promoted_rac == False:
                t["status"] = "CONFIRMED"
                t["berth"] = vacated_berth
                promoted_rac = True
                break

        # If an RAC was promoted, shift the first WL into RAC
        if promoted_rac:
            for t in tickets:
                if "WL" in t["status"]:
                    t["status"] = "RAC-Shifted"
                    t["berth"] = "Side-Seat"
                    break

    # If cancelled ticket was RAC, promote first WL into RAC
    elif "RAC" in deleted["status"]:
        for t in tickets:
            if "WL" in t["status"]:
                t["status"] = "RAC-Shifted"
                t["berth"] = "Side-Seat"
                break

    save_tickets(tickets)
    return True, "Ticket " + pnr + " cancelled. Queue updated."
