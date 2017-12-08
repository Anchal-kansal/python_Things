import urllib2
import json
from datetime import datetime, date, time

def convertmonth(m):
    if m=="Jan":
        return 01
    elif m=="Feb":
        return 02
    elif m=="Mar":
        return 03
    elif m=="Apr":
        return 04
    elif m=="May":
        return 05
    elif m=="Jun":
        return 06
    elif m=="Jul":
        return 07
    elif m=="Aug":
        return 8
    elif m=="Sep":
        return 9
    elif m=="Oct":
        return 10
    elif m=="Nov":
        return 11
    elif m=="Dec":
        return 12


def converttime(s):
    year=int(s[12:16])
    month=convertmonth(s[8:11])
    date=int(s[5:7])

    hour=int(s[17:19])
    minute=int(s[20:22])
    second=int("00")

    d=datetime(year,month,date,hour,minute,second)
    return d

response = urllib2.urlopen("https://contesttrackerapi.herokuapp.com/android/")
data = json.load(response)

timespan=data["result"]["timestamp"]
timespan=converttime(timespan)

oncontests=data["result"]["ongoing"]
upcontests=data["result"]["upcoming"]

upcoming_contest=[]
past_contest=[]
live_contest=[]

for contest in oncontests:
    end=converttime(contest["EndTime"])
    contest["EndTime"]=end
    if end>datetime.now() and end>timespan:
        live_contest.append(contest)
    if end<datetime.now():
        past_contest.append(contest)

for contest in upcontests:
    start=converttime(contest["StartTime"])
    end=converttime(contest["EndTime"])
    if start>datetime.now():
        upcoming_contest.append(contest)
    if end<datetime.now():
        past_contest.append(contest)
    if  start<datetime.now() and end>datetime.now():
        live_contest.append(contest)

print "<---#######################################################Ongoing Contest#########################################---->"
print "\n"
for contest in live_contest:
    print "End Time of Contest", contest["EndTime"]
    print "Name", contest["Name"]
    print "Platform", contest["Platform"]
    print "url-->", contest["url"]
    print "\n"

print "<---#######################################################Upcoming Contest#########################################---->"
print "\n"
for contest in upcoming_contest:
    print "Duration left", contest["Duration"]
    print "End Time of Contest", contest["EndTime"]
    print "Name", contest["Name"]
    print "Platform", contest["Platform"]
    print "Starting Time", contest["StartTime"]
    print "url-->", contest["url"]
    print "\n"
