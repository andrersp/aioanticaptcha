import asyncio
from aioanticaptcha.funcaptchaproxyon import *


async def main():
    async with funcaptchaProxyon() as solver:
        solver.set_verbose(1)
        solver.set_key("YOUR_KEY")
        solver.set_website_url("https://website.com")
        solver.set_website_key("XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX")
        solver.set_proxy_address("PROXY_ADDRESS")
        solver.set_proxy_port(1234)
        solver.set_proxy_login("proxylogin")
        solver.set_proxy_password("proxypassword")
        solver.set_user_agent("Mozilla/5.0")

        token = solver.solve_and_return_solution()
        if token != 0:
            print("result token: " + token)
        else:
            print("task finished with error " + solver.error_code)


if __name__ == "__main__":
    asyncio.run(main())
