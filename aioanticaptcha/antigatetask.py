from aioanticaptcha.antinetworking import *
import asyncio


class antigateTask(antiNetworking):

    template_name = ""
    variables = {}

    def push_variable(self, task_id, name, value):
        result = self.make_request(
            "pushAntiGateVariable",
            {
                "clientKey": self.client_key,
                "taskId": self.task_id,
                "name": name,
                "value": value,
            },
        )
        if result == 0:
            return 0
        else:
            if result["errorId"] == 0:
                return 1
            else:
                return 0

    async def send_antigate_task(self):
        if (
            await self.create_task(
                {
                    "clientKey": self.client_key,
                    "task": {
                        "type": "AntiGateTask",
                        "websiteURL": self.website_url,
                        "templateName": self.template_name,
                        "variables": self.variables,
                        "proxyAddress": self.proxy_address,
                        "proxyPort": self.proxy_port,
                        "proxyLogin": self.proxy_login,
                        "proxyPassword": self.proxy_password,
                    },
                }
            )
            == 1
        ):
            self.log("created task with id " + str(self.task_id))
            return self.task_id
        else:
            self.log("could not create task")
            self.log(self.err_string)
            return 0

    async def solve_and_return_solution(self):
        if (
            await self.create_task(
                {
                    "clientKey": self.client_key,
                    "task": {
                        "type": "AntiGateTask",
                        "websiteURL": self.website_url,
                        "templateName": self.template_name,
                        "variables": self.variables,
                        "proxyAddress": self.proxy_address,
                        "proxyPort": self.proxy_port,
                        "proxyLogin": self.proxy_login,
                        "proxyPassword": self.proxy_password,
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
            return task_result["solution"]

    def set_template_name(self, value):
        self.template_name = value

    def set_variables(self, value):
        self.variables = value
