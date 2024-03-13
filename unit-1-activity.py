# Unit 1 Activity
# Taylor Sayson
# 4 March 2024

#import time for timing and typing letters out and date for current year
import time
from datetime import date
today = date.today()
yr = today.strftime("%Y")
year = int(yr)

# Create a function called type that types out lettrs, also sleeps for a bit every line
def type(x):
    time.sleep(.4)
    for letters in x:
        print(letters, end='', flush=True)
        time.sleep(0.03)
    print()
        
# Function without a line of print at end
def typeline(x):
    time.sleep(.33)
    for letters in x:
        print(letters, end='', flush=True)
        time.sleep(0.02)

#Introduce percent bot
type("Hello, I am Percent Bot!")
type("I will ask you certain questions to determine what percentage of your life you spend on different activiites.")
type("To answer, simply enter your answer when prompted.")
type("There will be multiple choice questions, where you input the letter of your answer, and short answer questions, where you type in a response to the question")

# Ask do you understand question, proceeding with yes answer, repeating with no answer, or asking for yes or no for invaid answer
while True:
    type("Do you understand?")
    type("A) Yes")
    type("B) No")
    typeline("Answer: ")
    understand = input().lower().strip(".!() /")
    if understand == "yes" or understand == "y" or understand == "a":
            type("Alright, let's begin!")
            break
    if understand == "no" or understand == "n" or understand == "b":
        type("I will explain again.")
        type("I will ask you certain questions to determine what percentage of your life you spend on different activiites")
        type("To answer, simply enter your answer when prompted. ")
        type("There will be multiple choice questions, where you input the letter of your answer, and short answer questions, where you type in a response to the question")
    else:
        type("Please respond A or B.")
        
# Start with information questions
type("To start off, tell me a little about yourself.")
type("Please enter the information asked below.")
typeline("First Name: ")
first_name = input()
typeline("Last Name: ")
last_name = input()

#Make sure birth year is an actual number or year
while True:
    typeline("Birth Year: ")
    birth = input().lower().strip(" !/()year")
    if birth.isdigit():    
        birthyear = int(birth)
        if birthyear > 1900 and birthyear < year:
            break
        else:
            type("Please enter a vaild number for your year of birth.")
    else:
        type("Please enter a vaild number for your year of birth.")     
            
# Thank user then ask work questions
type(f"Thank you, {first_name}. Now I will ask you about some of the activities in your life.")
type("Which of the following best represent your work life?")
type("A) I currently work at a job")
type("B) I used to work at a job but now I do not")
type("C) I do not currently work and have never worked at a job before")

# Ensure user chooses a,b, or c
while True:
    typeline("Answer: ")
    job_answer = input().lower().strip(" .!/()")
    if job_answer == "a":
        break
    if job_answer == "b":
        break
    elif job_answer == "c":
        break
    else:
        type("Please enter a valid letter that corresponds to an answer above")

# Job answer is A ask how often they work, followup questions depending on answer 
if job_answer == "a":
    type("How often do you work at your job?")
    type("A) I work at least once almost every week")
    type("B) I don't always work at least once a week")
    while True:
        typeline("Answer: ")
        work_days = input().lower().strip(" .!/()")
        if work_days == "a":
            break
        if work_days == "b":
            break
        else:
            type("Please enter a valid letter that corresponds to an answer above")
    if work_days == "a":
        type("On average, how many days a week do you work?")
        while True:
            typeline("Answer: ")
            daysaweek = input().lower().strip(" !/()days")
            if daysaweek.isdigit():    
                intdaysaweek = int(daysaweek)
                if intdaysaweek > 0 and intdaysaweek < 8:
                    break
                else:
                    type("Please enter a vaild whole numerical value from 1-7 for how many days a week you work")
            else:
                type("Please enter a vaild whole numerical value from 1-7 for how many days a week you work")
                
    if work_days == "b":
        type("How many days a month do you work?")
        while True:
            typeline("Answer: ")
            daysamonth = input().lower().strip("!/()months")
            if daysamonth.isdigit():    
                intmonth = int(daysamonth)
                if intmonth > 0:
                    break
                else:
                    type("Please enter a positive whole numerical value for the average days you work in a month")
            else:
                type("Please enter a positive whole numerical value for the average days you work in a month")
        intdaysaweek = intmonth / 4
    type("In months, how long have you've had a job?")
    while True:
        typeline("Answer: ")
        month_work = input().strip(" ,!/months")
        if month_work.isdigit():
            intworkmonths = int(month_work)
            if intworkmonths > 0 :
                break
            else:
                type("Please enter a positive whole numerical value for the number of months you worked")
            break
        else:
            type("Please enter a positive whole numerical value for the number of months you worked")
            
# Job answer is B ask how often they work, followup questions depending on answer 
if job_answer == "b":
    type("In total, how many months did you end up working?")
    while True:
        typeline("Answer: ")
        month_work = input().strip(" ,!/months")
        if month_work.isdigit():
            intworkmonths = int(month_work)
            if intworkmonths > 0 :
                break
            else:
                type("Please enter a positive whole numerical value for the number of months you worked")
            break
        else:
            type("Please enter a positive whole numerical value for the number of months you worked")
    type("On average, how many days a week did you work?")
    while True:
        typeline("Answer: ")
        daysaweek = input().lower().strip("!/()days")
        if daysaweek.isdigit():    
            intdaysaweek = int(daysaweek)
            if intdaysaweek > 0 and intdaysaweek < 8:
                break
            else:
                type("Please enter a vaild whole numerical value from 1-7 for how many days a week you worked")
        else:
            type("Please enter a vaild whole numerical value from 1-7 for how many days a week you worked")
    
#If job answer is C, hours work in job is zero
if job_answer == "c":
    intdaysaweek = 0
    floatshiftlength = 0
    intworkmonths = 0

# If they did/do work  how long is their shift
if job_answer == "a" or job_answer == "b":
    type("On average, how long is one of your work days in hours?")
    while True:
        typeline("Answer: ")
        shift_length = input().lower().strip("!/()hours")
        if shift_length.isdigit():
            floatshiftlength = float(shift_length)
            if floatshiftlength > 0:
                break
            else:
                type("Please enter a positive numerical value for the length of one of your works days")
        else:
            type("Please enter a positive numerical value for the length of one of your works days")

# Calculate total hours worked       
job_hours = floatshiftlength * intdaysaweek * 4 * intworkmonths

#Ask questions about school
type(f"Thanks {first_name}! Now I will ask you questions about school")
type("Which of the following best describe your school life?")
type("A) I am currently in school")
type("B) I am not currently in school")

#Ensure answer is a or b
while True:
    typeline("Answer: ")
    school_answer = input().lower().strip(" .!/()")
    if school_answer == "a":
        break
    if school_answer == "b":
        break
    else:
        type("Please enter a valid letter that corresponds to an answer above")

# Ask if they ARE in school now, follow up questions based on responses
if school_answer == "a":
    type("What level of education are you currently in?")
    type("A) Elementary School")
    type("B) High School")
    type("C) Post-Secondary")
    
    while True:
        typeline("Answer: ")
        current_school = input().lower().strip(" .!/()")        
        if current_school == "a" or current_school == "b":
            floatcollegeyears = 0
            type("Type in the number of the grade you are in?")
            while True:
                typeline("Answer: ")
                grade = input().strip(" .!/,thstndrdgrade")
                if grade.isdigit():
                    intgrade = int(grade)
                    if intgrade > 0:
                        break
                    else:
                        type("Please enter a whole number representing the grade you currently are in.")
                else:
                    type("Please enter a whole number representing the grade you currently are in.")
            break
        if current_school == "c":
            intgrade = 12
            type("How many years of post-secondary education have you completed?")
            while True:
                typeline("Answer: ")
                college_years = input().lower().strip(" .!/,years")
                if college_years.isdigit():
                    floatcollegeyears = float(college_years)
                    if floatcollegeyears > 0:
                        break
                    else:
                        type("Please enter a positive numerical value for the number of years you have been in post sercondary education.")
                else:
                    type("Please enter a positive numerical value for the number of years you have been in post sercondary education.")
            break
        else:
                type("Please enter a valid letter that corresponds to an answer above")
                
# Ask if they ARE NOT in school now, follow up questions based on responses
if school_answer == "b":
    type("What was the highest level of education you've attended")
    type("A) Elementary School")
    type("B) High School")
    type("C) Post-Secondary")
    while True:
        typeline("Answer: ")
        completed_school = input().lower().strip(" .!/()")        
        if completed_school == "a" or completed_school == "b":
            floatcollegeyears = 0
            type("What is the last grade you've completed")
            while True:
                typeline("Answer: ")
                grade = input().lower().strip(" .!/()stndrdthgrade")
                if grade.isdigit():
                    intgrade = int(grade)
                    if intgrade > 0:
                        break
                    else:
                        type("Please enter a whole number representing the grade you currently are in.")
                else:
                    type("Please enter a whole number representing the grade you currently are in.")
            break
        if completed_school == "c":
            intgrade = 12
            type("How many years were you in post-secondary education?")
            while True:
                typeline("Answer: ")
                college_years = input().lower().strip(" .!/()years")
                if college_years.isdigit():
                    floatcollegeyears = float(college_years)
                    if floatcollegeyears > 0:
                        break
                    else:
                        type("Please enter a positive number representing the number of years you were in post-secondary education.")  
                else:
                    type("Please enter a positive number representing the number of years you were in post-secondary education.")
            break            
        else:
            type("Please enter a valid letter that corresponds to an answer above.")
    
#Calculate total hours spent in school(6.5hr/day for 180 days a year) and postsecondary(45hr/week for 30 weeks a year)
gradeschool_hours = intgrade * 6.5 * 180
college_hours = floatcollegeyears * 30 * 45

#Ask final questions first on sleep
type(f"Thank you {first_name}. I just have a few more questions to ask you.")
type("On average, how many hours a night do you sleep?")
while True:
    typeline("Answer: ")
    slept = input().lower().strip(" !/()hours")
    if slept.isdigit():    
        sleep = int(slept)
        if sleep > 0 and sleep < 15:
            break
        else:
            type("Please enter a vaild number for the average hours you sleep a night.")
    else:
        type("Please enter a vaild number for the average hours you sleep a night.")      
sleephoursyear = sleep * 365

#Ask about eating time
type("How many meals do you eat a day?")
while True:
    typeline("Answer: ")
    food = input().lower().strip(" !/()meals")
    if food.isdigit():    
        meals = int(food)
        if meals > 0 and meals < 6:
            break
        else:
            type("Please enter a vaild number for how many meals you eat a day.")
    else:
        type("Please enter a vaild number for how many meals you eat a day.")

type("On average, how many minutes do you spend eating one meal?")
while True:
    typeline("Answer: ")
    eating = input().lower().strip(" !/()meals")
    if eating.isdigit():    
        eattime = int(eating)
        if eattime > 0 and eattime < 200:
            break
        else:
            type("Please enter a vaild number for the length of one of your meals")
    else:
        type("Please enter a vaild number for the length of one of your meals")

#Ask about screen usage
type("Lastly, one average, how many hours a day do you spend using a screen such as a phone, computer, or TV?")
while True:
    typeline("Answer: ")
    screen = input().lower().strip(" !/()hours")
    if screen.isdigit():    
        screentime = float(screen)
        if screentime > 0 and screentime < 24:
            break
        else:
            type("Please enter a vaild number for your screentime in hours.")
    else:
        type("Please enter a vaild number for your screentime in hours.")


#Calculate everything to a percentage
life = year - birthyear
hours_lived = life * 8760

pjob = job_hours / hours_lived * 100
pschool = gradeschool_hours / hours_lived * 100
pcollege =  college_hours / hours_lived * 100
psleep = (sleep * 365 * life) / hours_lived * 100
peat = (eattime / 60 * meals * 365 * life) / hours_lived * 100
pscreen = (screentime * 365 * life) / hours_lived * 100

#Give results
type("Thank you for talking to me! Now I will give you your results")
type("Calculating results...")
print()
time.sleep(2)
type(f"{first_name.upper()} {last_name.upper()}'S RESULTS:")
type(f"PERCENTAGE OF LIFE...")
print()
if pjob > 0:
    type(f"WORKING = {round(pjob, 2)}%")
if pschool > 0:
    type(f"IN SCHOOL = {round(pschool, 2)}%")
if pcollege > 0:
    type(f"IN POST-SECONDARY = {round(pcollege, 2)}%")
type(f"SLEEPING = {round(psleep, 2)}%")
type(f"EATING = {round(peat, 2)}%")
type(f"USING A SCREEN = {round(pscreen, 2)}%")
print()