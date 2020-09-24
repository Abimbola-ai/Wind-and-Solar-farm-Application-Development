# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from automate import final_merged_data
import os
from datetime import datetime


#print(final_merged_data)


#print(less_data)
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = os.environ.get('account_sid')
auth_token = os.environ.get('auth_token')

client = Client(account_sid, auth_token)


def send_message(message):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message, 
        to='whatsapp:+2348106061236')
    return message


current_timestamp = str(datetime.now())

messages = f"Solar and Wind farm 7 days report @ {current_timestamp}"


rows = zip(final_merged_data['Day'].tolist(), final_merged_data['SolarFarm_Output(MW)'].tolist(), final_merged_data['WindFarm_Output(MW)'].tolist(), final_merged_data['Total_MW'].tolist())
for row in rows:
    message_partition = f"""
    [{row[0]}]

    Solar_Power_Generated in MW = {str(row[1])}
    Wind_Power_Generated in MW = {str(row[2])}
    Total_Power_Generated in MW = {str(row[3])}"""
    messages = messages + message_partition

send_message(messages)
#print(messages)