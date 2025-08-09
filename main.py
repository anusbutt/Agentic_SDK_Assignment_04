import asyncio
from agents_config import Traige_Agent
from configuration import config
from context import UserContext
from openai.types.responses import ResponseTextDeltaEvent
from agents import Runner

async def main():
    context = UserContext(
        user_name="Anus Butt",
        account_number="134564",
        balance=1500.75,
        authenticated=True
    )

    user_input = input("you: ")
    result = Runner.run_streamed(
        Traige_Agent,
        user_input,
        context=context,
        run_config=config
    )

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
