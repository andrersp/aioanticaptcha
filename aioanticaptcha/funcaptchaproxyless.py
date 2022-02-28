from aioanticaptcha.antinetworking import *
import asyncio


class funcaptchaProxyless(antiNetworking):

    js_api_domain = ""
    data_blob = ""

    async def solve_and_return_solution(self):
        if (
            await self.create_task(
                {
                    "clientKey": self.client_key,
                    "task": {
                        "type": "FunCaptchaTaskProxyless",
                        "websiteURL": self.website_url,
                        "funcaptchaApiJSSubdomain": self.js_api_domain,
                        "data": self.data_blob,
                        "websitePublicKey": self.website_key,
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
        task_result = await self.wait_for_result(600)
        if task_result == 0:
            return 0
        else:
            return task_result["solution"]["token"]

    def set_js_api_domain(self, value):
        self.js_api_domain = value

    def set_data_blob(self, value):
        self.data_blob = value
