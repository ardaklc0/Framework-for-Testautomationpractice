#CONSTANTS
import inspect

URL = "https://testautomationpractice.blogspot.com/"
USERNAME = "testuser"
EMAIL = "testuser@example.com"
PHONE = "1234567890"
ADDRESS = "123 Test St, Test City, Test Country"

def whoami():
    return inspect.stack()[1][3]
