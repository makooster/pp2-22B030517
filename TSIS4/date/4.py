import datetime as dt

d1 = dt.datetime(2023, 2, 15)
d2 = dt.datetime(2023, 1, 1)

print(dt.timedelta.total_seconds(d1 - d2))