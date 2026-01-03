import datetime
now = datetime.datetime.now()
nowTimestamp = now.timestamp()
pastTimestamp = datetime.datetime(1970, 1, 1).timestamp()

secondsPast = nowTimestamp - pastTimestamp

print(f'Seconds since January 1, 1970: {secondsPast} or {"{:.2e}".format(secondsPast)} in scientific notation')
print(f'{now.strftime("%b %d %Y")}')
