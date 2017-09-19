from steganography.steganography import Steganography
from select_friend import select_friend
from friend import friend_list
from datetime import datetime
import re
from emergency_msg import emergency
from colorama import init, Fore
init()
imageexpr = "^[a-zA-Z0-9]+.jpg$"
def read_message():
    sender = select_friend()
    if (sender == "error"):
        print Fore.RED + "Wrong Choice" + Fore.RESET
    else:
        while (True):
            encrypted_image = raw_input("Please provide the encryted image to decode")
            if re.match(imageexpr, encrypted_image, flags=0) is not None:
                break
           else:
                print Fore.RED + "Image name must be alpha numeric and image extension must be .jpg" + Fore.RESET
        try:
            secret_message = Steganography.decode(encrypted_image)
            print "The secret message is: " + secret_message
            # emergency messages
            for i in emergency:
                if i == secret_message.upper():
                    print Fore.RED + "Your emergency message has been handled" + Fore.RESET
                chats = friend_list[sender].get_chats()
                all_message = secret_message
            for chat in chats:
                if not chat['send_by_me']:
                    all_message = all_message + " " + chat['message']

            avg_words = len(all_message.split())
            if (avg_words > 100):
                print Fore.RED + "Error!! Spy speaking too much. Removing the spy from friend list...." + Fore.RESET
                del friend_list[sender]
            else:
                print Fore.GREEN + "Hello you are speaking fine. your average words speaked till date is: " + str(avg_words) + Fore.RESET

                new_chat = {
                'message': secret_message,
                'time': datetime.now(),
                'send_by_me': False
                }

                friend_list[sender].get_chats().append(new_chat)

                print Fore.GREEN + "Message saved" + Fore.RESET
      except:
        print Fore.RED + "Sry either image is not available or the image does not contain any valid message" + Fore.RESET




