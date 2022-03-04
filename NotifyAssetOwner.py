import requests
import json

endpoint="192.168.1.52:8501"
API_Key="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1aWQiOi0xMDAsImp0aSI6ImY2MzNmZjdiLTMzYzAtNGU0OS05YmExLTAyYzExZjkzMTk3MSIsImNpZCI6IjM5QURDRTUwLTMxOEMtNDAyRi04QTgyLUQyNTlCNERFMTc4OSIsImlzcyI6ImxyLWF1dGgiLCJyaWQiOiJnbG9iYWxBZG1pbiIsInBpZCI6LTEwMCwic3ViIjoiTG9nUmh5dGhtQWRtaW4iLCJleHAiOjE2Nzc4ODMxNjQsImRlaWQiOjEsImlhdCI6MTY0NjM0NzE2NH0.ZWcrWpJtqYZ_cWK3Qw51aZZUTDTTMzzv6nB0QPIdrxLHDpxQRH6hpsxrRot1Zb-fgRnCmKkMv7PeipAUH9O4PozYyCMuEu61UUt7Ix0rsDUFJsB7zWeZr2vw9hiNUARHUVtGCddjrStMwPFOq4bxEUOWenL7OR9EhHCOFyJyM7u12Ubn-00f0OTuY1ggD2SBJUKcP-vZF6P0g_JRybsxhffRlYDv1GFdXlIp7N9nxoGlc0U5Ir78C8GJ81QNX5tsvjcJWzj2G8zIoznKI2WwuG_K3BBhN1La0pJakcwUpWaBh2HQKbA58xtpwNikCZhJ2PF9vJOOREWvry9fe5QSIg"
alarmID=7

URL = "https://"+endpoint+"/lr-drilldown-cache-api/drilldown/"+str(alarmID)

headers = {"Authorization": "Bearer "+str(API_Key)}
response = (requests.get(URL, headers=headers,json={"Content-Type": "application/json"}, verify=False)).json()
logMessage=json.loads(response['Data']['DrillDownResults']['RuleBlocks'][0]['DrillDownLogs'])

logSourceEntity=logMessage[0]['entityName']
logSourceHost=logMessage[0]['logSourceHost']

print(logSourceEntity)
print(logSourceHost)

