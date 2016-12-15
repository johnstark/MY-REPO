import re
import datetime

match_record = re.compile(r"^[^ ]+ - (C[^ ]*) \[([^ ]+)").match
strptime = datetime.datetime.strptime

f = open("/var/www/msin/flmain/2016-04-11-08-47-32-6CE5F66353D546A4", "rb")

for line in f:
    match = match_record(line)
    if match is not None:
        user, str_time = match.groups()
        time = strptime(str_time, "%d/%b/%Y:%H:%M:%S")
        print user, repr(time)
