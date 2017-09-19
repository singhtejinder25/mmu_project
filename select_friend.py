from friend import friend_list
import re
from colorama import init, Fore
init()
choexpr = "^[0-9]+$"
def select_friend():
    i = 1
    for friend in friend_list:
        print str(i) + " Name : " + friend.get_name() + "  Age : " + str(friend.get_age())
        i = i + 1;
    while True:
        result = raw_input("Select your friend from the list: ")
        if re.match(choexpr, result, flags=0) != None:
             break

        else:
            print (Fore.RED + "Please enter only integer choice." + Fore.RESET)
    result = int(result)
    if (result > 0 and result < i):
        return result - 1
    else:
        return "error"
