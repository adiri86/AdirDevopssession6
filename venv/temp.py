import requests
import time

url = "http://10.70.80.30/UsbCtrl.htm"

payload = "name=CSN02024&channel=1&Action=Assign"
headers = {
    'Content-Length': "37",
    'cache-control': "no-cache",
    'Postman-Token': "31876461-0ab2-4bbb-b151-8400a1322112"
    }

response = requests.request("POST", url, data=payload, headers=headers)

time.sleep(10)

payload = "name=CSN02024&channel=2&Action=Assign"
headers = {
    'Content-Length': "37",
    'cache-control': "no-cache",
    'Postman-Token': "31876461-0ab2-4bbb-b151-8400a1322112"
    }

response = requests.request("POST", url, data=payload, headers=headers)

time.sleep(10)
payload = "name=CSN02024&channel=1&Action=Assign"
headers = {
    'Content-Length': "37",
    'cache-control': "no-cache",
    'Postman-Token': "31876461-0ab2-4bbb-b151-8400a1322112"
    }

response = requests.request("POST", url, data=payload, headers=headers)

time.sleep(10)

payload = "name=CSN02024&channel=0&Action=Assign"
headers = {
    'Content-Length': "37",
    'cache-control': "no-cache",
    'Postman-Token': "31876461-0ab2-4bbb-b151-8400a1322112"
    }

response = requests.request("POST", url, data=payload, headers=headers)



