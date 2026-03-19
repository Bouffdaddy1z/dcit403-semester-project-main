from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template
import time


class RecommendationAgent(Agent):

    class RecommendationBehaviour(CyclicBehaviour):

        def __init__(self):
            super().__init__()
            self.reserved_seats = {}
            self.reservation_duration = 1800  # 30 minutes

        def clear_expired_reservations(self):
            current_time = time.time()
            expired = []

            for seat, timestamp in self.reserved_seats.items():
                if current_time - timestamp > self.reservation_duration:
                    expired.append(seat)

            for seat in expired:
                print(f"Reservation expired for seat: {seat}")
                del self.reserved_seats[seat]

        async def run(self):

            # Remove expired reservations
            self.clear_expired_reservations()

            msg = await self.receive(timeout=10)

            if msg:
                print("Recommendation Agent received:", msg.body)

                seats = eval(msg.body)

                for seat, status in seats.items():
                    if status == "free" and seat not in self.reserved_seats:

                        print(f"Recommended seat: {seat}")

                        # Reserve seat
                        self.reserved_seats[seat] = time.time()

                        print(f"Seat {seat} reserved for 30 minutes")
                        break

    async def setup(self):

        print("Recommendation Agent started")

        template = Template()
        template.set_metadata("performative", "inform")

        self.add_behaviour(self.RecommendationBehaviour(), template)