import requests

def print_hi(name):

    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

print_hi('Rayhan')

respose=requests.get("https://github.com/rayhantmt/Ai")
print(respose.status_code)