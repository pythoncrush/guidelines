
#Use regex to solve each of these problems
#Watch this video before starting https://www.youtube.com/watch?v=K8L6KVGG-7o
#This is a good site to use https://pythex.org/ cleaner than regex101.com


#This is necessary to use the re (short for regex libary built into python)
#Documentatation for this module is here https://docs.python.org/3/library/re.html
import re

#1 Write a regex to parse name,dob, city and state of residence 
#from a string passed in
datum_1 = "Steven-Barker-5-18-1989-Pensacola-Florida"
datum_2 = "Mike-Leostold-7-23-2001-Fairbanks-Alaska"
datum_3 = "Emmit-Imovov-1-7-1965-Patterson-Vermont"


def data_puller(datam):
	#your code to parse the passed in string goes here
	print(f"First name is : ")
	print(f"Last name is : ")
	print(f"DOB is : ")
	print(f"Current city is : ")
	print(f"Current state is : ")

#2 Remove spaces from string
datum_4 = "Here we go again!"
datam_5 = "Ring the alarm, another sound is dying, woh-oh hey"

#3 Remove puncuation and non English characters from strings
lyric_1 = "Tive razão"
lyric_2 = "Posso falar"
lyric_3 = "Não foi legal, não pegou bem"
lyric_4 = "Que vontade de chorar, dói"
lyric_5 = "Em pensar que ela não vem, só dói"

#4 Detect if string a is inside of string b
string_a = "and"
string_b = "stand"

#5 Say beep every 7 seconds

#Here is how you say beep
import os
os.system("say beep")

#Here is how to use time in python
import time
from datetime import datetime

# Using the time module
current_time_seconds = time.time()
print(f"Current time in seconds since epoch: {current_time_seconds}")

current_time_string = time.ctime(current_time_seconds)
print(f"Current local time: {current_time_string}")

# Using the datetime module
now = datetime.now()
print(f"Current datetime object: {now}")

