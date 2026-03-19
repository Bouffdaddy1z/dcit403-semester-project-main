from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
import random
import asyncio


class SeatMonitorAgent(Agent):

    class MonitorBehaviour(CyclicBehaviour):

        async def run(self):

            seats = {
                "A1": random.choice(["free", "occupied"]),
                "A2": random.choice(["free", "occupied"]),
                "A3": random.choice(["free", "occupied"])
            }

            print("Seat Status:", seats)

            msg = Message(
                to="reservation.agent@xmpp.jp"
            )

            msg.body = str(seats)
            msg.set_metadata("performative", "inform")

            await self.send(msg)

            await asyncio.sleep(5)

    async def setup(self):
        print("Seat Monitor Agent started")
        self.add_behaviour(self.MonitorBehaviour())