import pandas as pd
import string

def attraction_names(attractions_spec):
    return [x.strip().lower() for x in attractions_spec["Attraction"]]

punctuation_remove = str.maketrans("", "", string.punctuation)

def get_information(attractions_spec):
    print("Hi, nice to see you! I will ask you five simple questions to suggest you the best choice you can do. It will last less than a minute!") 
    while True:
        usr_position = input("Which is the nearest attraction you can see?\n").strip().lower().replace(" ","")
        names = attraction_names(attractions_spec)
        if usr_position in names:
            break
        else:
            print("Attraction name not found, please digit it again.\n ")
    print("Perfect!")    
    while True:
        usr_flashpass = input("Do you have a flashpass? Reply \"yes\" or \"no\"\n").strip().lower().replace(" ","")
        usr_flashpass = usr_flashpass.translate(punctuation_remove)
        if usr_flashpass in ["yes","no"]:
            break
        else:
            print("Please digit \"yes\" or \"no\".\n ")
    print("Nice, now two questions in order to suggest you only attractions you can do.\n ")
    while True:
        usr_age = input("How old are you? Write it in number.\n (If you are in a group consider the age of the youngest person)\n").strip().replace(" ","")
        usr_age = usr_age.translate(punctuation_remove)
        try:
            usr_age = int(usr_age)
            break
        except:
            print("Age has not been written in the correct format, please it digit again.\n ")
    if usr_age <= 12:
        while True:
            usr_parent = input("Is there an adult available to do the attraction with you? Some attractions requires a partner for people younger than 12.\n Reply with \"yes\" or \"no\"\n").strip().lower().replace(" ","")
            usr_parent = usr_parent.translate(punctuation_remove)
            if usr_parent in ["yes","no"]:
                break
            else:
                print("Please digit \"yes\" or \"no\".\n ")
    else:
        usr_parent = "yes"
    print("Good, now I'll ask you your height.\n ")
    while True:
        usr_height = input("How tall are you? Write it in centimeter, for example 190 if you are 1.90m.\n(Still refer to the youngest person if you are in a group)\n").strip().replace(" ","")
        usr_height = usr_height.translate(punctuation_remove)
        try:
            int(usr_height)
            break
        except:
            print("Height has not been written in the correct format, please it digit again.\n ")
    print("Perfect, the last two questions about the activities you prefer doing.\n ")
    while True:
        usr_water = input("Do you want to do an attraction with the chance of getting wet or not? Reply \"yes\" or \"no\"\n").strip().lower().replace(" ","")
        usr_water = usr_water.translate(punctuation_remove)
        if usr_water in ["yes","no"]:
            break
        else:
            print("Please digit \"yes\" or \"no\".\n ")
    print("Nice choice!\n ")
    while True:
        usr_attraction = input("Which type of attraction do you prefer? Choose one of these option:\n\"Super Chill\" (I'm just a kid)\n\"Easy\" (something not fast but not even boring)\n\"Normal\" (I don't want to have stomacache for the vertical loops)\n\"Adrenaline\" (I like the speed but there are attractions which are too much)\n\"Extreme\" (I'm not scary of anything)\n").strip().lower().replace(" ","")
        response_list = ["superchill","easy","normal","adrenaline","extreme"]
        if usr_attraction in response_list:
            break
        else:
            print("The type of attraction has not been written well, please write one of the options quoted.\n ")
    print("Thank you for the information, I will output the attractions I suggest you in a moment!")
    usr_info = {"Position":usr_position,
                "Flashpass":usr_flashpass,
                "Age":usr_age,
                "Parent":usr_parent,
                "Height":usr_height,
                "Water":usr_water,
                "Attraction":usr_attraction
                }
    return usr_info
