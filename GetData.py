import base64
import requests
url = "https://api.github.com/repos/NikolayNPanev/TestRemoteFileAccess/contents/Data.txt"

def scrape(url):
    content = ""
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        req = req.json()
        content = base64.b64decode(req['content'])
        content = str.strip(content.decode("utf-8"))
    else:
        print("404")
        return

    global data 
    data = ""
    if "False" == content:
        return "False"
    if "True" == content:
        return "True"
    else:
        return "418 - not a boolean"

print(scrape(url))