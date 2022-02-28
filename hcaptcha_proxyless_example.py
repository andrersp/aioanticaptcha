from aioanticaptcha.hcaptchaproxyless import *
import asyncio


async def main():
    async with hCaptchaProxyless() as solver:
        solver.set_verbose(1)
        solver.set_key("YOUR_KEY")
        solver.set_website_url("https://website.com")
        solver.set_website_key("SITE_KEY")

        g_response = solver.solve_and_return_solution()
        if g_response != 0:
            print("g-response: " + g_response)
        else:
            print("task finished with error " + solver.error_code)


if __name__ == "__main__":
    asyncio.run(main())
