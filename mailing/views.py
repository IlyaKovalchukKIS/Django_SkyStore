from datetime import datetime

from django.shortcuts import render

# Create your views here.
def send_email():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Текущее время: {current_time}")