from select_friend import select_friend
from steganography.steganography import Steganography
from datetime import datetime
from friend import friend_list
from colorama import init, Fore
from emergency_msg import emergency
import re
init()
imageexpr = "^[a-zA-Z0-9]+.jpg$"
nameexpr = "^[a-zA-Z]+[\sa-zA-Z]*$";

def send_message():
    friend_choice = select_friend();
    if (friend_choice == "error"):
        print Fore.RED + "wrong choice" + Fore.RESET
    else:
        friend_choice = int(friend_choice);
        while True:
            original_image = raw_input("Provide name of image to hide message into")
            if re.match(imageexpr, original_image, flags=0) is not None:
                break;
            else:
                print Fore.RED + "Image name must be alpha numeric and image extension must be .jpg" + Fore.RESET
        while True:
            output_image = raw_input("Provide the name of output image")
            if re.match(imageexpr, output_image, flags=0) is not None:
                break;
            else:
                print Fore.RED + "Image name must be alpha numeric and image extension must be .jpg" + Fore.RESET
        while True:
            text = raw_input("Enter your message")
            if (len(text) > 0):
                break
            else:
                print Fore.RED + "Please provide some message. It cannot be empty." + Fore.RESET
    try:
        Steganography.encode(original_image, output_image, text);
        print Fore.GREEN + "Message encrypted successfully"
        # Save the chats
        new_chat = {
        'message': text,
        'time': datetime.now(),
        'send_by_me': True
        }
        # saving the dictionary
        friend_list[friend_choice].get_chats().append(new_chat)
        print "Message saved successfully" + Fore.RESET
        for i in emergency:
            if i == text.upper():
                print Fore.RED + "Your emergency message has been sent. You need not to worry." + Fore.RESET
     except:
        print Fore.RED + "NO such image exist in the module." + Fore.RESET
