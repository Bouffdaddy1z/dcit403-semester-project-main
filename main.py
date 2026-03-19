import asyncio

from agents.seat_monitor_agent import SeatMonitorAgent
from agents.reservation_agent import ReservationAgent
from agents.recommendation_agent import RecommendationAgent


async def main():

    seat_monitor = SeatMonitorAgent(
        "seatmonitor.agent@xmpp.jp",
        "agent123"
    )

    reservation = ReservationAgent(
        "reservation.agent@xmpp.jp",
        "agent123"
    )

    recommendation = RecommendationAgent(
        "recommend.agent@xmpp.jp",
        "agent123"
    )

    # ✅ START IN CORRECT ORDER
    await recommendation.start()
    await reservation.start()
    await seat_monitor.start()

    print("All agents started...")

    # Allow time for connection stabilization
    await asyncio.sleep(5)

    # Run system
    await asyncio.sleep(60)

    await seat_monitor.stop()
    await reservation.stop()
    await recommendation.stop()


asyncio.run(main())