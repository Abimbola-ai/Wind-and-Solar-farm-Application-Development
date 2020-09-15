from apscheduler.schedulers.blocking import BlockingScheduler
from sms import *

scheduler = BlockingScheduler()
def the_funct():
    for numb in receiver_list:
        print(f"sending message to {numb}")
        send_message(numb, messages)

scheduler.add_job(the_funct, 'cron', hour=1)
scheduler.start()