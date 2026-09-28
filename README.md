# Railway PNR & Berth Reservation Simulator

A simple, modular terminal-based Python tool to simulate railway seat allocations, RAC handling, and waiting list shifts.

## What It Does
- Lets you book tickets with passenger details (Name, Age, Gender, Berth Preference).
- Automatically assigns seats to Confirmed, RAC, or Waiting List based on available limits.
- Automatically gives Lower berths to senior citizens (age 60 or above).
- Automatically promotes RAC passengers to Confirmed when someone cancels.
- Saves all records in `tickets.txt` so no external database is needed.

## Requirements
- Python 3 (installed on your system).
- No external libraries or third-party packages needed.

## How to Set Up and Run

1. Open your terminal and navigate to the project directory:
   ```bash
   cd railway_reservation
