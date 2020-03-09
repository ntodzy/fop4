# Nathan Todzy
# Foundations of Programming U4P-2
# Goal for this section of the project is to parse through application data to automatically approve or deny a user.
# 3/3/2020

import requests
import json

def main():

  raw_data = requests.get("http://foundations-of-programming-unit-4-project--skyguy92.repl.co/api/get/applications?cmd=pending")

  data = json.loads(raw_data.content)

  # Add minimum requirements

  for application in data:
    
    content = data[application]['content']

    if content['computer'] == 'y' and int(content['sr']) >= 2750:

      print('Application #{} has been accepted! Sending denied request now!'.format(application))

      payload = json.dumps({
        "id": application,
        "status": "approved",
        "reason": "Met minimum entrance requirements."
      })

      print(payload)

      requests.post('https://foundations-of-programming-unit-4-project--skyguy92.repl.co/api/application', data = payload, auth=('app_review', 'mcd0na1dz!'))
    
    else:

      print('Application #{} has been denied! Sending approving request now!'.format(application))

      reason = None

      if content['computer'] != 'y':
        reason = "You do not have a computer! We are a pc only club! "
      
      if int(content['sr']) < 2750:

        reason = "Your skill rating is too low! Please be mid-gold to apply!"
      
      if content['computer'] != 'y' and int(content['sr']) < 2750:

        reason = "You do not have a computer, we are a pc only club! Your skill rating is also too low, Please be mid-gold to apply!"

      payload =json.dumps({
        "id": int(application),
        "status": "denied",
        "reason": reason
        })
        

      print(payload)

      requests.post('https://foundations-of-programming-unit-4-project--skyguy92.repl.co/api/application', data=payload, auth=('app_review', 'mcd0na1dz!'))

  return

main()