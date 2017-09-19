import re
from colorama import Fore, init
status_message = []
init()
nameexpr = "^[a-zA-Z0-9@!]+[\s0-9a-zA-Z!]*$";
choexpr = "^[0-9]+$"

def add_status(current_status):
    print "\nEnter 1 to choose from the previous status and 2 to add new status: "
    ch = choose()
    if (ch == 1):
        pos = 1
        for i in status_message:
            print pos, ". " + i;
            pos = pos + 1;
    if not status_message:
        return "Sorry. No previous history available"
    else:
        msg_select = choose()
        if (msg_select < pos):
            return msg_select;
        else:
            return "Wrong choice"
        elif (ch == 2):
        while True:
            new_status = raw_input("Enter your new status: ");
            if (re.match(nameexpr, new_status, flags=0) != None):
                status_message.append(new_status);
                break
            else:
                print "Please enter some status."
        return len(status_message);
     else:
        return Fore.RED + "Wrong choice" + Fore.RESET

def choose():
    while True:
    choice = raw_input("Enter your choice: ")
    if (re.match(choexpr, choice, flags=0) != None):
        return int(choice)
    else:
        print (Fore.RED + "Please enter only integer choice." + Fore.RESET)
