# Project Statement - Railway PNR & Berth Reservation Simulator

## Problem Statement
Booking railway tickets manually often leads to errors in managing berth allocations, RAC (Reservation Against Cancellation) slots, and Waiting List queues. When passengers cancel confirmed tickets, shifting the next eligible passenger by hand is slow and confusing. This project provides a simple command-line simulator to automate berth allocation, PNR generation, and waitlist shifts.

## Scope of the Project
- Simulates ticket bookings for a single train coach using the command line.
- Enforces fixed quotas across Confirmed berths, RAC seats, and Waiting List slots.
- Provides automatic queue shifts when a confirmed or RAC seat is cancelled.
- Saves passenger records to a plain text file for persistent tracking.

## Target Users
- Railway counter clerks and station operators.
- Beginners studying queue-based inventory management.

## High-Level Features
- **PNR Generation**: Assigns an automatic 5-digit PNR for each passenger.
- **Berth Preference**: Gives Lower berth priority to senior citizens (age 60+).
- **Auto Promotion**: Automatically promotes RAC passengers to Confirmed and Waiting List passengers to RAC on cancellation.
- **Status & Chart Display**: Allows searching by PNR and viewing the full passenger chart.
