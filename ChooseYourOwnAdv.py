import time
import random


def print_pause(text_print):
    print(text_print)
    time.sleep(1)


def intro(items, alt):
    print_pause("Welcome to Tombstone, Arizona,\n")
    print_pause("The Most Dangerous Town in the Wild West!\n")
    print_pause("You just got the job as the New Sheriff in town.\n")
    print_pause("Where the Most Wanted " + alt + " has been hiding out.\n")
    print_pause("You've been hired to locate them, dead or alive.\n")
    print_pause("Someone said that he was at the Saloon.\n")
    print_pause("Another person says he's hiding at the Motel.\n")
    print_pause("Another person said speak to the Rancher first.\n")
    print_pause("Times is running out, you have until nightfall!\n")


def ranch(items, alt):
    if "saloon" in items:
        print_pause("\nYou walk onto the Ranch and meet the Rancher.")
        print_pause("He's already spoken to you about the " + alt + ".")
        print_pause("You don't want to make the Rancher angry! ")
        print_pause("Get out of here and go find him!\n")
    else:
        print_pause("\nYou walk onto the Ranch and meet the Rancher.")
        print_pause("He's angry because the " + alt + " broke into his Ranch.")
        print_pause("He said his horse was stolen by the " + alt + "!")
        print_pause("He said he saw him heading towards the Saloon.")
        print_pause("Go to the Saloon to follow up on this tip.\n")
        items.append("saloon")
    station(items, alt)


def saloon(items, alt):
    if "gun" in items:
        print_pause("\nYou walk into the bustling Saloon.")
        print_pause("You head up to the bar to ask the barman")
        print_pause("if he's seen the " + alt + " recently.")
        print_pause("He said he already told you!")
        print_pause("Nothing more to see here, head to the Motel.\n")
    else:
        print_pause("\nYou walk into the bustling Saloon.")
        print_pause("You head up to the bar to ask the barman.")
        print_pause("if he's seen the " + alt + " recently.")
        print_pause("He said he has!")
        print_pause("He kicked the " + alt + " out for fighting.")
        print_pause("The barman said he stumbled over to the Motel.")
        print_pause("The barman warns you to bring the BIG GUNS.")
        print_pause("Head to the Sherriff's Station to get guns.\n")
        items.append("gun")
    station(items, alt)

  
def motel(items, alt):
    print_pause("\nYou enter the Motel and it's quiet.. too quiet.\n")
    print_pause("You walk a little further and BANG!\n")
    print_pause("You've just been shot by the " + alt + "!\n")
    print_pause("You duck to hide from the " + alt + "'s flying bullets!\n")
    print_pause("You're injured, but you can still fight.\n")
    if "gun" not in items:
        print_pause("What do you do?\n")
    while True:
        option2 = input("1 - Shoot\n"
                        "2 - Regroup\n")
        if option2 == "1":
            if "gun" in items:
                print_pause("\nThe " + alt + " tries to shoot but misses.\n")
                print_pause("You fire with your shotgun and he falls.\n")
                print_pause("The " + alt + " is injured but will survive!\n")
                print_pause("You saved the town from the " + alt + ".\n")
                print_pause("For your bravery you are awarded a bounty!\n")
                print_pause("Hooray!\n")
            else:
                print_pause("\nYou fire off your revolver.\n")
                print_pause("The " + alt + " shoots you!\n")
                print_pause("The " + alt + " escapes and you bleed out.\n")
                print_pause("You Died!\n")
            restart_game()
            break
        if option2 == "2":
            print_pause("\nBack to the Sherriff's Station to regroup\n")
            station(items, alt)
            break


def station(items, alt):
    print_pause("\nWhere are you going?\n")
    print_pause("1 - Ranch.")
    print_pause("2 - Saloon.")
    print_pause("3 - Motel.\n")
    while True:
        option1 = input("Enter 1, 2 or 3.\n")
        if option1 == "1":
            ranch(items, alt)
            break
        elif option1 == "2":
            saloon(items, alt)
            break
        elif option1 == "3":
            motel(items, alt)
            break


def restart_game():
    again = input("Want to play again?\n"
                  "Enter - y or n\n").lower()
    if again == "y":
        print_pause("Restarting\n")
        print_pause("3\n")
        print_pause("2\n")
        print_pause("1\n")
        sherriff_game()
    elif again == "n":
        print_pause("Thank you for playing!")
    else:
        restart_game()


def sherriff_game():
    items = []
    alt = random.choice(["Criminal", "Outlaw", "Bank Robber"])
    intro(items, alt)
    station(items, alt)


sherriff_game()
# personal note : alt-short for alternative