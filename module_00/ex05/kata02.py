import datetime

kata = (2019, 9, 25, 3, 30)

tm = datetime.datetime(kata[0], kata[1], kata[2], kata[3], kata[4])
print(tm.strftime("%m/%d/%Y %H:%M"))
