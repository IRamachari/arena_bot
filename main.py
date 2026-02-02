import asyncio
from tg_bot.bot import run_bot
from auth.google_oauth import GoogleOAuth

if __name__ == "__main__":
    asyncio.run(GoogleOAuth().authenticate())
    run_bot()
