from aioanticaptcha.antinetworking import *
import asyncio


class recaptchaV2EnterpriseProxyless(antiNetworking):
    async def solve_and_return_solution(self):
        if (
            await self.create_task(
                {
                    "clientKey": self.client_key,
                    "task": {
                        "type": "RecaptchaV2EnterpriseTaskProxyless",
                        "websiteURL": self.website_url,
                        "websiteKey": self.website_key,
                        "enterprisePayload": self.recaptcha_enterprise_payload,
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
