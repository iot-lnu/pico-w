import wifiConnection
from requests import get, Response


def http_get(url:str = 'http://detectportal.firefox.com/') -> None:
    response: Response = get(url)
    if not response:
        print("No Response!")
        return
    print(str(response.content))

# Try WiFi Connection then HTTP GET
try:
    ip = wifiConnection.connect()
    http_get()
except (Exception, KeyboardInterrupt) as err:
    print("Keyboard interrupt")

# WiFi Disconnect
# wifiConnection.disconnect().