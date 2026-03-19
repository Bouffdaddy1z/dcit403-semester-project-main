from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from spade.template import Template


class ReservationAgent(Agent):

    class ReservationBehaviour(CyclicBehaviour):

        async def run(self):

            msg = await self.receive(timeout=10)

            if msg:
                print("Reservation Agent received:", msg.body)

                forward_msg = Message(
                    to="recommend.agent@xmpp.jp"
                )

                forward_msg.body = msg.body
                forward_msg.set_metadata("performative", "inform")

                await self.send(forward_msg)

                print("Sent to RecommendationAgent")

    async def setup(self):

        print("Reservation Agent started")

        template = Template()
        template.set_metadata("performative", "inform")

        self.add_behaviour(self.ReservationBehaviour(), template)