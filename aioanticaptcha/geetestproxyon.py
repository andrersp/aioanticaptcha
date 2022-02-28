from aioanticaptcha.antinetworking import *
import asyncio


class geetestProxyon(antiNetworking):

    js_api_domain = ""
    gt = ""
    challenge = ""
    geetest_lib = ""

    async def solve_and_return_solution(self):
        if (
            await self.create_task(
                {
                    "clientKey": self.client_key,
                    "task": {
                        "type": "GeeTestTask",
                        "websiteURL": self.website_url,
                        "gt": self.gt,
                        "challenge": self.challenge,
                        "geetestApiServerSubdomain": self.js_api_domain,
                        "geetestGetLib": self.geetest_lib,
                        "proxyType": self.proxy_type,
                        "proxyAddress": self.proxy_address,
                        "proxyPort": self.proxy_port,
                        "proxyLogin": self.proxy_login,
                        "proxyPassword": self.proxy_password,
                        "userAgent": self.user_agent,
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
        task_result = self.wait_for_result(600)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]

    def set_gt_key(self, value):
        self.gt = value

    def set_challenge_key(self, value):
        self.challenge = value

    def set_js_api_domain(self, value):
        self.js_api_domain = value

    def set_geetest_lib(self, value):
        self.geetest_lib = value
