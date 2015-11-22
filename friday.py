import datetime

cur_date = datetime.datetime.now()
for _ in xrange(70*365):
    if cur_date.weekday() == 4 and cur_date.day == 13:
        print cur_date
    cur_date += datetime.timedelta(1)
