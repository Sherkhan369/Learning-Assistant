# scheduler.py

import schedule
import time
from recommender import Recommender
from notifier import send_notification

def job():
    recommender = Recommender()
    today_info = recommender.get_today_topic()
    if today_info:
        message = f"Today topic: {today_info['topic']}\nCode: {today_info['code']}\nyoutube: {today_info['youtube']}"
        send_notification("remember", message)

def run_scheduler():
    schedule.every().day.at("10:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(60)
