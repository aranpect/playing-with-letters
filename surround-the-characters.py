import math
import pyperclip

while True:
    print("1:ASCII art around letters"+"\n"+"2:Line breaks one character at a time"+"\n"+"3:Shift characters by one character"+"\n"+"4:Circle the letters"+"\n"+"5:Finish")
    firsttext = int(input("which one would you choose: "))

    if(firsttext==1):
        text = input("Enter a text: ")
        surrounding_char = input("Enter a surrounding character: ")

        new_text = surrounding_char * (len(text) + 2) + "\n"
        new_text += surrounding_char + text + surrounding_char + "\n"
        new_text += surrounding_char * (len(text) + 2)

        print(new_text)
    elif(firsttext==2):
        text = input("Enter a text: ")

        for char in text:
            print(char + "\n")
    elif(firsttext==3):
        text = input("Enter a text: ")
        for i in range(len(text)):
            print(" " * i + text[i])

    elif(firsttext==4):
        text = input("Enter a text: ")

        max_word_length = max([len(word) for word in text.split()])

        radius = max_word_length / math.pi

        for i in range(len(text)):
            angle = (i / (len(text) - 1)) * math.pi
            x = math.cos(angle) * radius
            y = math.sin(angle) * radius
            print(" " * int(round(y)) + text[i])
    
    elif(firsttext==5):
        break
    else:
        print("Please enter the appropriate characters")