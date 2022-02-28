from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'Async lib for  Anti-Captcha service.'
LONG_DESCRIPTION = 'Async lib for bypass captcha using Anti-Captcha.'

# Setting up
setup(
    name="python3-aioanticaptcha",
    version=VERSION,
    author="André França",
    author_email="rsp.assistencia@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['aiohttp', 'aiofiles'],


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
