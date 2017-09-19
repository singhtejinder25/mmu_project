from select_friend import select_friend
from friend import friend_list
from main import Spy
from colorama import init, Fore
sd = friend_list()
init()
def read_chat():
      # selecting a friend from the list
    choice = select_friend()
    if choice == "error":
        print Fore.RED + "Wrong choice" + Fore.RESET
     else:
        print (Fore.GREEN + "Messages sent by you is shown in green color \n" + Fore.RED + "Messages received and read by your friend is shown in red color:" + Fore.RESET)
        choice = int(choice)
        chats = friend_list[choice].get_chats()

        for chat in chats:
             if chat['send_by_me']:
                print (Fore.BLUE + str(chat['time']) + " " + Fore.GREEN + sd.get_name() + " " + Fore.RESET + chat['message'])
             else:
                print (Fore.BLUE + str(chat['time']) + " " + Fore.RED + friend_list[choice].get_name() + " " + Fore.RESET + chat['message'])
