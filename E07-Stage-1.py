#-------------random----------#
# import random
# winner_id = random.randint(1, 10)
# winner_id = random.randrange(1, 10, 2)
# users = ['amirhsosein', 'ali', 'zahra']
# random_user = random.choice(users)
# print(random_user)
#-------------TimeStamp----------#
# import time
# myTime = time.time()
# print(myTime)
#-------------Sleep-------------#
# import time
# print('Helloworld')
# time.sleep(2) #Second
# print("GoodBye")
#-------------DateTime----------#
# from datetime import datetime
# date = datetime.now()
# # formated_date = today.strftime("%Y/%m/%d %H:%M:%S")
# # print(formated_date)
# today = date.day
# print(f"today is: {today}")
# this_month = date.month
# this_year = date.year
# print(this_month)
# print(this_year)
#-------------Password Input----------#
# import getpass
# password = getpass.getpass("Enter Your Pass: ")
# print(password)
#-------------OS----------#
# import os
# FileName = input("enter your file name: ")
# os.system(f'md {FileName}') #Make Directory #Linux: mkdir
# os.system(f"cd {FileName}") #Change Directory
# with open(f"{FileName}\FileName.txt", 'w') as filename:
#     filename.write("Test IS DONE")
#-------------Regex--------------#
#1:amirhossein 2:@ 3:gmail 4:.com 
#Start with: ^ Caret End With: $ 
#Meta Sequences 
#1: . Any Single Character
#2: \s Any White Space Character
#3: \S Any Non-Wite Space Character
#4: \d Any Digit
#5: \D Any Non-Digit 
#6: \w Any Word Character
#7: \W Any Non-Word Character
import re #Regex
# text = 'Linux Windows Mac'
# need = re.findall('\S+', text)
# print(need)
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)
#Function	#Description
#findall	#Returns a list containing all matches
#search	    #Returns a Match object if there is a match anywhere in the string
#split	    #Returns a list where the string has been split at each match
#sub	    #Replaces one or many matches with a string
#MetaCharacter
#Character	Description	Example	Try it
#[]	A set of characters	"[a-m]"	
# txt = 'The rain in Spain'
# #Lower Case a-z or Upper Case [A-Z]
# x = re.findall("[A-Z]", txt)
# print(x)
#\	Signals a special sequence (can also be used to escape special characters)	"\d"	
# txt = "That will be 59 dollars"
# #Find all digit characters:
# x = re.findall("\d", txt)
# print(x)
#.	Any character (except newline character)	"he..o"	
# txt = "hello world"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
# x = re.findall("he..o", txt)
# print(x)
# ^	Starts with	"^hello"
# txt = input(": ")
# #Check if the string starts with 'hello':
# x = re.findall("^hello", txt)
# if x:
#   print(f"Yes, the string starts with '{txt}'")
# else:
#   print("No match")
# $	Ends with	"world$"
# txt = "hello world"
# #Check if the string ends with 'world':
# x = re.findall("world$", txt)
# if x:
#   print("Yes, the string ends with 'world'")
# else:
#   print("No match")
# *	Zero or more occurrences	"aix*"	
# txt = "The rain in Spain falls mainly in the plain!"
# #Check if the string contains "ai" followed by 0 or more "x" characters:
# x = re.findall("aix*", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
# +	One or more occurrences	"aix+"	
# txt = "The rain in Spain falls mainly in the plain!"
# #Check if the string contains "ai" followed by 1 or more "x" characters:
# x = re.findall("aix+", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
# {}	Exactly the specified number of occurrences	"al{2}"	
# txt = "The rain in Spain falls mainly in the plain!"
# #Check if the string contains "a" followed by exactly two "l" characters:
# x = re.findall("al{3}", txt)
# print(x)
# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
# |	Either or	"falls|stays"	
txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays", txt)
print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
# ()	Capture and group
