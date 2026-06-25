from datetime import datetime

now=datetime.now()
print("today's date:",now.date())
print("today's time:",now.time())
print("today's weekday:",now.strftime("%A"))

print("today's date:",now.strftime("%d"))
print("today's date:",now.strftime("%H:%M:%S:%s"))