from aioanticaptcha.antigatetask import *

solver = antigateTask()
solver.set_verbose(1)
solver.set_key("YOUR_KEY")
solver.set_website_url("http://antigate.com/logintest.php")
solver.set_template_name("Sign-in and wait for control text")
solver.set_variables(
    {
        "login_input_css": "#login",
        "login_input_value": "test login",
        "password_input_css": "#password",
        "password_input_value": "test password",
        "control_text": "You have been logged successfully",
    }
)

result = solver.solve_and_return_solution()
if result != 0:
    cookies, localStorage, fingerprint, url, domain = (
        result["cookies"],
        result["localStorage"],
        result["fingerprint"],
        result["url"],
        result["domain"],
    )
    print("cookies: ", cookies)
    print("localStorage: ", localStorage)
    print("fingerprint: ", fingerprint)
    print("url: " + url)
    print("domain: " + domain)
else:
    print("task finished with error " + solver.error_code)
