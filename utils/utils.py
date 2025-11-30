#CONSTANTS
import inspect

URL = "https://www.saucedemo.com/"
USERNAME = "visual_user"
PASSWORD = "secret_sauce"


def whoami():
    return inspect.stack()[1][3]
