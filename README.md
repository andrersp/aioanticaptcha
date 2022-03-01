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
Report previosly solved Recaptcha V2/V3/Enterprise as incorrect:
```python
...
solver.report_incorrect_recaptcha()
```

Report it as correct to improve your quality:
```python
...
solver.report_correct_recaptcha()
```
---
&nbsp;

Solve [image captcha](https://anti-captcha.com/apidoc/task-types/ImageToTextTask):

```python
import asyncio
from aioanticaptcha.imagecaptcha import *


async def main():
    async with imagecaptcha() as solver:
        solver.set_verbose(1)
        solver.set_key("YOUR_KEY")
        captcha_text = await solver.solve_and_return_solution("captcha.jpeg")
        if captcha_text != 0:
            print("captcha text " + captcha_text)
        else:
            print("task finished with error " + solver.error_code)


if __name__ == "__main__":
    asyncio.run(main())
```
Report previosly solved image captcha as incorrect:
```python
...
solver.report_incorrect_image_captcha()
```

---

&nbsp;

Solve [Funcaptcha](https://anti-captcha.com/apidoc/task-types/FunCaptchaTaskProxyless) (Arkoselabs):

```python
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

```
___

&nbsp;

Solve [GeeTest](https://anti-captcha.com/apidoc/task-types/GeeTestTask) captcha:

```python
import asyncio
from aioanticaptcha.geetestproxyless import *


async def main():
    async with geetestProxyless() as solver:
        solver.set_verbose(1)
        solver.set_key("YOUR_API_KEY")
        solver.set_website_url("https://address.com")
        solver.set_gt_key("CONSTANT_GT_KEY")
        solver.set_challenge_key("VARIABLE_CHALLENGE_KEY")
        token = solver.solve_and_return_solution()
        if token != 0:
            print("result tokens: ")
            print(token)
        else:
            print("task finished with error " + solver.error_code)


if __name__ == "__main__":
    asyncio.run(main())

```
___

&nbsp;

Solve [HCaptcha](https://anti-captcha.com/apidoc/task-types/HCaptchaTask):

```python
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

```
___

Check out [examples](https://github.com/andrersp/aioanticaptcha) for other captcha types

License
[MIT](https://choosealicense.com/licenses/mit/)