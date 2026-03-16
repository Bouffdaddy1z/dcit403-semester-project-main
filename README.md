Intelligent Library Seat Monitoring System
DCIT403 – Intelligent Agents Project
Project Overview

This project implements a Multi-Agent System that monitors library seat availability and recommends free seats to users.

The system uses:

Python

SPADE (Smart Python Agent Development Environment)

XMPP messaging protocol

Gajim XMPP client (for monitoring agent communication)

Three intelligent agents collaborate to achieve the system goal:

SeatMonitorAgent – detects seat availability

ReservationAgent – processes seat data

RecommendationAgent – recommends available seats

The system demonstrates the Percept → Decide → Act intelligent agent cycle.

Requirements

The system requires the following software:

1. Python

Python 3.9 or higher is recommended.

Check your version:

python3 --version
2. Install Required Python Libraries

Create a requirements.txt file containing:

spade
slixmpp
asyncio

Install dependencies using:

pip install -r requirements.txt
XMPP Agent Accounts

The agents communicate using XMPP accounts.

Example accounts used in the project:

Agent	XMPP ID
Seat Monitor Agent	seatmonitor.agent@xmpp.jp

Reservation Agent	reservation.agent@xmpp.jp

Recommendation Agent	recommend.agent@xmpp.jp

You must create these accounts on the XMPP server (e.g., xmpp.jp).

Running the System

Navigate to the project directory:

cd library-seat-agent-system

Run the system using:

python main.py

Expected output:

Seat Monitor Agent started
Reservation Agent started
Recommendation Agent started

Seat Status: {'A1': 'occupied', 'A2': 'free'}