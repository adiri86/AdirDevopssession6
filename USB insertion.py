import http.client

conn = http.client.HTTPConnection("10,70,80,30")

payload = "name=CSN02024&channel=0&Action=Assign"

headers = {
    'Content-Length': "37"
    }

conn.request("POST", "UsbCtrl.htm", payload, headers)

res = conn.getresponse()
data = res.read()





payload = "name=CSN02024&channel=1&Action=Assign"

headers = {
    'Content-Length': "37",
    'cache-control': "no-cache",
    'Postman-Token': "8e826443-4562-403e-9738-2759af5924e7"
    }

conn.request("POST", "UsbCtrl.htm", payload, headers)

res = conn.getresponse()
data = res.read()



payload = "name=CSN02024&channel=2&Action=Assign"

headers = {
    'Content-Length': "37",
    'cache-control': "no-cache",
    'Postman-Token': "8e826443-4562-403e-9738-2759af5924e7"
    }

conn.request("POST", "UsbCtrl.htm", payload, headers)

res = conn.getresponse()
data = res.read()



payload = "name=CSN02024&channel=1&Action=Assign"

headers = {
    'Content-Length': "37",
    'cache-control': "no-cache",
    'Postman-Token': "8e826443-4562-403e-9738-2759af5924e7"
    }

conn.request("POST", "UsbCtrl.htm", payload, headers)

res = conn.getresponse()
data = res.read()




payload = "name=CSN02024&channel=0&Action=Assign"

headers = {
    'Content-Length': "37",
    'cache-control': "no-cache",
    'Postman-Token': "8e826443-4562-403e-9738-2759af5924e7"
    }

conn.request("POST", "UsbCtrl.htm", payload, headers)

res = conn.getresponse()
data = res.read()



