from aioanticaptcha.antinetworking import *
import asyncio


class recaptchaV2Proxyless(antiNetworking):
    async def solve_and_return_solution(self):
        task = {
            "type": "RecaptchaV2TaskProxyless",
            "websiteURL": self.website_url,
            "websiteKey": self.website_key,
            "websiteSToken": self.website_stoken,
            "recaptchaDataSValue": self.recaptcha_data_s,
        }
        if self.is_invisible:
            task["isInvisible"] = True
        if await self.create_task({"clientKey": self.client_key, "task": task}) == 1:
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
