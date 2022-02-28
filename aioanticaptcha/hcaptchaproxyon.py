from aioanticaptcha.antinetworking import *
import asyncio


class hCaptchaProxyon(antiNetworking):
    async def solve_and_return_solution(self):
        if (
            await self.create_task(
                {
                    "clientKey": self.client_key,
                    "task": {
                        "type": "HCaptchaTask",
                        "websiteURL": self.website_url,
                        "websiteKey": self.website_key,
                        "proxyType": self.proxy_type,
                        "proxyAddress": self.proxy_address,
                        "proxyPort": self.proxy_port,
                        "proxyLogin": self.proxy_login,
                        "proxyPassword": self.proxy_password,
                        "userAgent": self.user_agent,
                        "cookies": self.cookies,
                    },
                }
            )
            == 1
        ):
            self.log("created task with id " + str(self.task_id))
        else:
            self.log("could not create task")
            self.log(self.err_string)
            return 0
        # checking result
        await asyncio.sleep(3)
        task_result = await self.wait_for_result(300)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]["gRecaptchaResponse"]
