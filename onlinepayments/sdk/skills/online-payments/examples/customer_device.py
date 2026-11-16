from onlinepayments.sdk.domain.browser_data import BrowserData
from onlinepayments.sdk.domain.customer_device import CustomerDevice

from app_types import BrowserInfo


# [START customer-device]
# 3-D Secure needs details about the customer's browser. Collect the browser values with JavaScript on the checkout
# page and read the rest from the HTTP request (e.g. in Flask: request.headers.get("Accept"),
# request.headers.get("User-Agent"), request.remote_addr).
def build_customer_device(accept_header: str, user_agent: str, ip_address: str, browser: BrowserInfo) -> CustomerDevice:
    browser_data = BrowserData()
    browser_data.color_depth = browser.color_depth
    browser_data.java_enabled = browser.java_enabled
    browser_data.java_script_enabled = True
    browser_data.screen_height = str(browser.screen_height)
    browser_data.screen_width = str(browser.screen_width)

    device = CustomerDevice()
    device.accept_header = accept_header
    device.user_agent = user_agent
    device.ip_address = ip_address
    device.locale = browser.locale
    device.timezone_offset_utc_minutes = str(browser.timezone_offset_utc_minutes)
    device.browser_data = browser_data
    return device
# [END customer-device]
