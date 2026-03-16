from spade.agent import Agent
from spade.behaviour import CyclicBehaviour


class RecommendationAgent(Agent):

    class RecommendationBehaviour(CyclicBehaviour):

        async def run(self):

            msg = await self.receive(timeout=10)

            if msg:

                seats = eval(msg.body)

                for seat, status in seats.items():
                    if status == "free":
                        print("Recommended seat:", seat)
                        break

    async def setup(self):
        print("Recommendation Agent started")
        self.add_behaviour(self.RecommendationBehaviour())