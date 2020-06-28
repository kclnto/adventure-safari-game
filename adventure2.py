import time
import sys
import random
import os

animal = ["lion", "hippo", "domestic cat",
          "mysterious stranger that wasn't on the tour", "black mamba",
          "unicorn", "kangaroo", "cheetah", "zebra", "rhino", "elephant",
          "water buffalo", "leopard"]
status = ["1. Run away", "2. Sacrifice an innocent bystander",
          "3. Stand your ground and fight", "4. Do nothing"]
health = 100
ailments = []


def print_pause(string):
    os.system('clear')
    sys.stdout.flush()
    print(string)
    time.sleep(4)


def health_change(number):
    global health
    health = health + number
    print_pause("Health: "+str(health)+"% remaining.")
    if health <= 0:
        print_pause("Your health points are all gone so you died!")
        print_pause("It goes without saying, but...")
        print_pause("YOU LOSE.")
        play_again()


def intro():
    print_pause("Your South African safari has been the trip of a lifetime so "
                "far!")
    print_pause("Today's adventure is an nighttime walking tour through a "
                "private game reserve...\n")


def choice_1():
    print_pause("As the safari guide begins his safety warnings, a cool breeze"
                " picks up.")
    print_pause("A lion roars in the distance.")
    print_pause("You can't help but get chills down your spine.")
    print_pause("The safari guide finishes by saying that you've been "
                "informed of the risks, so now their company has no liability "
                "in the event of your grave bodily injury or death.")
    while True:
        response_1 = input("Now he asks, 'Well, are you ready to go?'\n"
                           "...Are you?\n\nPress 1 for yes. Press 2 to give "
                           "into fear and leave.\n")
        if response_1 == "1":
            health_change(0)
            choice_2()
        elif response_1 == "2":
            print_pause("The group laughs histerically as you walk away in "
                        "shame. You'll never forget the humiliation. Your trip"
                        " is ruined.\n")
            print_pause("YOU LOSE.")
            play_again()
        else:
            print_pause("The guide tells you that's not an answer. Yes or no.")


def choice_2():
    print_pause("You begin the walk at the back of the group.\nYou can either"
                " very conspicuously push ahead of a few people and move to"
                " the middle, or stay where you are.\n")
    while True:
        response_2 = input("Press 1 to push ahead of a few people. Press 2 to"
                           " stay in the back.\n")
        if response_2 == "1":
            print_pause("You get some dirty looks, but you'd rather stay on "
                        "the safe side and not be the last in line.")
            choice_3()
        elif response_2 == "2":
            print_pause("It turns out a lioness has been stalking the group, "
                        "and as the last in line, you make the easiest target"
                        " for her.")
            print_pause("You lose a foot, but manage to get away.")
            print_pause("You lose 25 health points and hobble back to the rest"
                        " of the group.")
            health_change(-25)
            ailments.append("lost a foot")
            carry_on()


def choice_3():
    for each in [1, 2, 3]:
        encounter = random.choice(animal)
        print_pause("You see a "+encounter+"!")
        if encounter == "hippo":
            print_pause("It mows you down immediately and leaves you for dead."
                        " Your entire body is black and blue.")
            print_pause("No wonder hippos are the deadliest animals in "
                        "Africa.")
            print_pause("You lose 85 health points and are very close to death"
                        " now.")
            health_change(-85)
            animal.remove("hippo")
            ailments.append("serious internal bleeding,")
            carry_on()
        elif encounter == "unicorn":
            print_pause("You think 'Wow! I thought those were a myth!'\n")
            print_pause("But you can't get your camera out in time to prove "
                        "their existence once and for all.")
            print_pause("Silent tears stream down your cheeks.")
            print_pause("You rejoin the group as the only one that saw the "
                        "unicorn...")
            animal.remove("unicorn")
            carry_on()
        elif encounter == "kangaroo":
            print_pause("You are confused because those are supposed to only "
                        "be found in Australia.\n")
            print_pause("You rub your eyes and get back to the group.")
            animal.remove("kangaroo")
            carry_on()
        else:
            animal.remove(encounter)
            action()
    outro()


def carry_on():
    endure = input("Do you dare to continue on the safari?\n"
                   "Press 1 to continue. Press 2 to cut the safari short.\n")
    if endure == "2":
        print_pause("Where is your courage and sense of adventure?\n"
                    "You're not going to get anywhere in life with an attitude"
                    " like that.")
        print_pause("YOU LOSE.")
        play_again()
    elif endure != "1":
        print_pause("What does that mean?")
        carry_on()


def action():
    print_pause("What action do you take? You can:\n\n")
    print("\n".join(status))
    result = input("\nWhat option do you choose?\n")
    if result == "2":
        print_pause("You are so panicked that you decide to sacrifice the "
                    "elderly woman in front of you.")
        print_pause("You pull her down to the ground and sprint ahead.")
        print_pause("You look behind you, and the tactic worked!")
        print_pause("You are traumatized for life, but you run to catch up to"
                    " the group.")
        print_pause("You lose 20 health points due to newly acquired PTSD.\n"
                    "And going forward, you won't have any more innocent "
                    "bystanders to sacrifice.")
        health_change(-20)
        ailments.append("acquired PTSD")
        status.remove("2. Sacrifice an innocent bystander")
        carry_on()
    elif result == "1":
        print_pause("You run far into the African bush, but you managed to get"
                    " away!")
        print_pause("You are forced to execute a full-on sprint to get back to"
                    " the group, and you're pretty out of shape.")
        print_pause("You lose 10 health points due to extreme fatigue and you"
                    " won't be able to run anymore.")
        health_change(-10)
        ailments.append("suffered extreme fatigue")
        status.remove("1. Run away")
        carry_on()
    elif result == "3":
        print_pause("That turned into a long, bloody battle!")
        print_pause("You didn't lose, but you didn't win either- "
                    "it retreated.")
        print_pause("There are wounds all over your body.")
        print_pause("That took a lot out of you, and you won't be able to "
                    "fight again.")
        print_pause("You lose 50 health points due to your injuries.")
        health_change(-50)
        ailments.append("gnarly battle wounds")
        status.remove("3. Stand your ground and fight")
        carry_on()
    elif result == "4":
        print_pause("Turns out that wasn't very threatening, but you have a"
                    " feeling you won't get that lucky again.\n")
        print_pause("You rejoin the group.")
        status.remove("4. Do nothing")
        carry_on()
    else:
        action()


def outro():
    print_pause("Your safari comes to an end without further incident.")
    print_pause("It needlessly dangerous, and you're pretty sure "
                "your guide was texting the entire time.")
    if ailments != []:
        print_pause("You have "+", ".join(ailments)+"... so you didn't get "
                    "through the safari unscathed.")
    print_pause("But you did complete the tour and survive!")
    print_pause("And you'll leave a one star review when you get back to the"
                " hotel.")
    print_pause("YOU WIN!")
    play_again()


def play_again():
    one_more = input("Would you like to play again?\nPress 1 to take another"
                     " recklessly dangerous safari walk. Press 2 to call it a"
                     " day.\n")
    if one_more == "1":
        global health
        health = 100
        global ailments
        ailments = []
        global animal
        animal = ["lion", "hippo", "domestic cat",
                  "mysterious stranger that wasn't on the tour", "black mamba",
                  "unicorn", "kangaroo"]
        global status
        status = ["1. Run away", "2. Sacrifice an innocent bystander",
                  "3. Stand your ground and fight", "4. Do nothing"]
        play_game()
    elif one_more == "2":
        exit()
        exit()
    else:
        print_pause("That's not an option.")
        exit()
        play_again()


def play_game():
    intro()
    choice_1()


play_game()
