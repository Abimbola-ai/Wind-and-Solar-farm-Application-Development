# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from automate import final_merged_data
from datetime import datetime


final_merged_data['Total MW'] = final_merged_data['Power_Solar'] + final_merged_data['Power_Wind']
# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACd4a0ae62a0f010f9cd84c1533031ebdb'
auth_token = 'd641cc2f6383d7d1724ec6e863e50133'
client = Client(account_sid, auth_token)


def send_message(message):
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=message, 
        to='whatsapp:+2348106061236')
    return message

#receiver = ['+2348106061236']
days = final_merged_data['Day'].tolist()
current_timestamp = str(datetime.now())

messages = f"THIS is UPDATED REPORT at {current_timestamp}"
for day in days:
    each_row = final_merged_data[final_merged_data['Day'] == days]

    message_partition = f"""
    [{day}]
    Solar_Power_Generated in MW = {str(each_row['Power_Solar'].tolist()[0])}
    Wind_Power_Generated in MW = {str(each_row['Power_Wind'].tolist()[0])}
    Total_Power_Generated in MW = {str(each_row['Total MW'].tolist()[0])}"""
    messages = messages + message_partition

#send_message(messages)
print(messages)