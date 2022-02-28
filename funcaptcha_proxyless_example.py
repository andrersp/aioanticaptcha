import asyncio
from aioanticaptcha.funcaptchaproxyless import *


async def main():
    async with funcaptchaProxyless() as solver:
        solver.set_verbose(1)
        solver.set_key("YOUR_KEY")
        solver.set_website_url("https://website.com")
        solver.set_website_key("XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX")

        token = solver.solve_and_return_solution()
        if token != 0:
            print("result token: " + token)
        else:
            print("task finished with error " + solver.error_code)


if __name__ == "__main__":
    asyncio.run(main())
