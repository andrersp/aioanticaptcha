import asyncio
from aioanticaptcha.recaptchav2proxyless import *


async def main():
    async with recaptchaV2Proxyless() as solver:
        solver.set_verbose(1)
        solver.set_key("YOUR_KEY")
        balance = await solver.get_balance()

        print(f"account balance: {balance}")


if __name__ == "__main__":
    asyncio.run(main())
