import sys
import requests
import json
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import time

'''arg1 = 
   arg2 =
   arg3 =
   arg4 =
   arg5 =
   arg6 =
   arg7 =
'''


alarmID=sys.argv[1]
assetFileName=sys.argv[2]

endpoint=str(sys.argv[3])
API_Key=str(sys.argv[4])

SMTP_Server = str(sys.argv[5])
mail_From = str(sys.argv[6])
mail_From_Password = str(sys.argv[7])


mail_To=""



URL = endpoint+"/lr-drilldown-cache-api/drilldown/"+str(alarmID)

headers = {"Authorization": "Bearer "+str(API_Key)}


def Notify():

    try:
        response = (requests.get(URL, headers=headers,json={"Content-Type": "application/json"}, verify=False)).json()
        logMessage=json.loads(response['Data']['DrillDownResults']['RuleBlocks'][0]['DrillDownLogs'])
        AIERuleName=str(response['Data']['DrillDownResults']['AIERuleName'])

        logSourceEntity=str(logMessage[0]['entityName'])
        logSourceHost=str(logMessage[0]['logSourceHost'])


        
        fields = []
        rows = []
        
        with open(assetFileName, 'r') as csvfile:
        
            csvreader = csv.reader(csvfile)
            
            fields = next(csvreader)
        
        
            for row in csvreader:
                if(logSourceEntity.lower()==row[0].lower() and logSourceHost.lower()==row[1].lower()):
                    mail_To=row[2]
                    break





        mail_To=list(mail_To.split(";")) 


        msg = MIMEMultipart()

        subject = "An alarm was triggered for your device"


        html = """\
        <html>
        <head></head>
        <body>
            <p>Hi,
            <br>
            <br>
            Below alarm was triggered for your device.
            <br><br>
            <table style="width: 100%;">
                <tr>
                    <td style="font-weight: bold; width: 61px;" class="modal-sm">Alarm Name:</td>
                    <td style="color: #FF0000">"""+AIERuleName+"""</td>
                </tr>

                <tr>
                    <td style="font-weight: bold; width: 61px;" class="modal-sm">Log Source:</td>
                    <td style="color: #FF0000">"""+logSourceHost+"""</td>
                </tr>
            </table>
            </p>
        </body>
        </html>
        """


        msg['From'] = mail_From
        msg['To'] = ", ".join(mail_To)
        msg['Subject'] = subject
        msg.attach(MIMEText(html, 'html'))
        text=msg.as_string()
        s = smtplib.SMTP(SMTP_Server)
        s.login(mail_From,mail_From_Password)
        s.sendmail(mail_From,mail_To, text)
        s.quit()

        print("Mail sent to successfully.")
    
    except Exception as e:
        print(str(e))
        return False
    return True
    


for i in [1,2,3,4,5]:
    print("Waiting 60 sec")
    time.sleep(60)
    if(Notify()==True):
        break

