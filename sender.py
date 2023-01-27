from twilio.rest import Client

SID = 'AC99a94038fd381be4668808ec6d3ffb65'
AUTHTOKEN = 'aef2bcd1154d91d1e629e8258c613092'

cl = Client(SID, AUTHTOKEN)

input_number = input("Enter number for send: ")

if input_number != None || input_number != 0:
   cl.messages.create(body='Your package number US151203912313 is in transit.', from_='+19713662389', to=f"{input_number}")
else:
   print(f"You entered {input_number}, We detect an error please try again!")
