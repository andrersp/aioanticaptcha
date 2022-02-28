# python3-aioanticaptcha


[![PyPI version](https://badge.fury.io/py/python3-aioanticaptcha.svg)](https://badge.fury.io/py/python3-anticaptcha)
[![Python versions](https://img.shields.io/pypi/pyversions/python3-aioanticaptcha.svg?logo=python&logoColor=FBE072)](https://badge.fury.io/py/python3-anticaptcha)

Python library forked from  [anticaptchaofficial](https://github.com/AdminAnticaptcha/anticaptcha-python).


The main purpose of the fork was to add implementation for async request using [aiohttp](https://docs.aiohttp.org/en/stable/)

## How to install?

```bash
pip install python3-aioanticaptcha
```

### Source
```bash
git clone https://github.com/andrersp/aioanticaptcha
python setup.py install
```
___

&nbsp;

Example how to create [Recaptcha V2](https://anti-captcha.com/apidoc/task-types/RecaptchaV2TaskProxyless) task and receive g-response:

```python
import asyncio
from aioanticaptcha.recaptchav2proxyless import *


async def main():

    async with recaptchaV2Proxyless() as solver:
        solver.set_verbose(1)
        solver.set_key("YOUR_KEY")
        solver.set_website_url("https://website.com")
        solver.set_website_key("SITE_KEY")

        # only for V2-invisible Recaptcha! :
        # solver.set_is_invisible(1)

        g_response = solver.solve_and_return_solution()
        if g_response != 0:
            print("g-response: " + g_response)
        else:
            print("task finished with error " + solver.error_code)


if __name__ == "__main__":
    asyncio.run(main())
```
Report it as correct to improve your quality:
```python
...
solver.report_correct_recaptcha()
```

License
-------

[MIT](https://choosealicense.com/licenses/mit/)