import datetime as dt

today = dt.datetime.today()
yesterday = today - dt.timedelta(days=1)
tomorrow = today + dt.timedelta(days=1)
print("today is" , today)
print("yesterday was", yesterday)
print("next day will be",tomorrow)