import urllib2
import json
from datetime import datetime, date, time

def converttime(s):
    d={"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8,"Sep":9, "Oct":10, "Nov":11, "Dec":12}
    year=int(s[12:16])
    month=d[s[8:11]]
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
