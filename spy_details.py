# import statements
from main import spy
from start_chat import start_chat
from termcolor import colored
import re
print "Let's get started!"
repeat = True
while repeat:
    question = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N): "
    existing = raw_input(question)
    # validating users input
    if (existing.upper() == "Y"):
        spy_name = spy['salutation'] + " " + spy['name']
        # starting chat application.
        start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])

    elif (existing.upper() == "N"):
    # user wants to continue as new user
    # chek wether spy has input something or not
        repeat = False
        wholecheck = True
        while (wholecheck):
            tempcheck = True
            patternsalutation = '^Mr|Ms$'
            patternname = '^[A-Za-z][A-Za-z\s]+$'
            patternage = '^[0-9]+$'
            patternrating = '^[0-9]+\.[0-9]$'
            while tempcheck:
                spy['name'] = raw_input("Enter your name. ?")
                if (re.match(patternname, spy['name']) != None):
                    tempcheck = False
                else:
                    print colored("invalid name , try again", 'red')
            tempcheck = True
            while tempcheck:
                spy['salutation'] = raw_input("Mr or Ms ? : ")
                if (re.match(patternsalutation, spy['salutation']) != None):
                    tempcheck = False
                else:
                    print colored("invalid salutation , try again", 'red')
                    #   concatination of salutation and name of spy.
            spy['name'] = spy['salutation'] + " " + spy['name']
            tempcheck = True
            while tempcheck:
                spy['age'] = raw_input("Enter your age. ?")
                if (re.match(patternage, spy['age']) != None):
                    tempcheck = False
                else:
                    print colored("invalid age , try again", 'red')
            tempcheck = True
            while tempcheck:
                spy['rating'] = raw_input("What is your spy rating?")
                if (re.match(patternrating, spy['rating']) != None):
                    tempcheck = False
                else:
                    print colored("invalid rating , try again", 'red')
            spy['is_online'] = True
            wholecheck = False
    start_chat(spy['name'], spy['age'], spy['rating'], spy['is_online'])
