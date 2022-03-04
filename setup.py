from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '1.1'
DESCRIPTION = 'Async lib for  Anti-Captcha service.'


# Setting up
setup(
    name="python3-aioanticaptcha",
    version=VERSION,
    author="André França",
    author_email="rsp.assistencia@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['aiohttp', 'aiofiles'],
    url="https://github.com/andrersp/aioanticaptcha",

    keywords=['python', 'anti-captcha', 'async'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        "Operating System :: OS Independent"
    ]
)
