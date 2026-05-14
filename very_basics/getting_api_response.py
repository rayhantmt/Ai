import requests
respose=requests.get("https://github.com/rayhantmt/Ai")
print(respose.status_code)