from playwright.async_api import async_playwright
from auth.session_store import SessionStore

ARENA_URL = "https://arena.ai"

class GoogleOAuth:
    async def authenticate(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-dev-shm-usage"]
            )
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto(ARENA_URL)
            print("Authenticate once locally if needed.")
            await page.wait_for_timeout(30000)
            storage = await context.storage_state()
            SessionStore.save(storage)
            await browser.close()
