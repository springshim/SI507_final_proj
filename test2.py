from datetime import datetime, timedelta

date = '2018-11-11'
test = '2018-11-28'

date = datetime.strptime(date, "%Y-%m-%d")
test = datetime.strptime(test, "%Y-%m-%d")

print(date)