from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message


class ReservationAgent(Agent):

    class ReservationBehaviour(CyclicBehaviour):

        async def run(self):

            msg = await self.receive(timeout=10)

            if msg:
                print("Reservation Agent received:", msg.body)

                recommendation_msg = Message(
                    to="recommend.agent@xmpp.jp"
                )

                recommendation_msg.body = msg.body

                await self.send(recommendation_msg)

                print("Sent seat info to RecommendationAgent")

    async def setup(self):

        print("Reservation Agent started")

        behaviour = self.ReservationBehaviour()

        self.add_behaviour(behaviour)
