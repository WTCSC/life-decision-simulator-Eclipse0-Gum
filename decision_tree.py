import time
import sys

# Helper functions
def dramatic_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_choice(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        else:
            print("Invalid choice. Options:", ", ".join(options))

def game_over(message="You have met an untimely end. Game Over."):
    dramatic_print("\n" + "="*40)
    dramatic_print(message)
    dramatic_print("GAME OVER".center(40, "-"))
    dramatic_print("="*40 + "\n")
    dramatic_print("Better Luck Next Time =)")
    time.sleep(1.5)
    exit()

# Scenes
def wake_up_scene():
    dramatic_print("You wake up in the middle of an apocalypse, you look around as you realize you're in your pjs, beneath a burnt blanket and laying in your destroyed limited edtion taco bell bed.")
    time.sleep(1.5)
    choice = get_choice("Do you get up or go back to sleep? (get up/sleep) ", ["get up", "sleep"])
    if choice == "sleep":
        game_over("You decide to go back to sleep only to be mauled by a mutated dog in your slumber. And turned into a dog treat for the rest of eternity.")
    else:
        bag_scene()

def bag_scene():
    dramatic_print("You get out of bed and begin to walk around, trying to control your panic in this sudden dying world.")
    time.sleep(1.5)
    dramatic_print("You come across a mysterious bag during your aimless walking.")
    time.sleep(1.5)
    choice = get_choice("Do you open the bag or leave it? (open/leave) ", ["open", "leave"])
    if choice == "open":
        dramatic_print("You open the bag and suddenly get sucked into a new world, it's colorful and beautiful.")
        time.sleep(1.5)
        dramatic_print("However your moment is ruined as the planet suddenly explodes with you.")
        game_over("To make matters worse you get evaporated from a passing meteor.")
    else:
        run_scene()

def run_scene():
    dramatic_print("You decide to leave the bag and continue moving forward.")
    time.sleep(1.5)
    dramatic_print("You come across a group of survivors and decide to join their journey.")
    time.sleep(1.5)
    dramatic_print("During your walk to safety a sudden massive statue of your mom appears from the sky...")
    dramatic_print("She points at you and requests your group to take you out. You immediately start running for your life as the group begins chase.")
    time.sleep(1.5)
    dramatic_print("You spot a random sandal on the ground. A weapon perhaps?")
    choice = get_choice("Do you go for the sandal or keep running? (sandal/run) ", ["sandal", "run"])
    if choice == "run":
        game_over("You leave the sandal only to trip and fall. You get beaten to death and toasted for dinner.")
    else:
        voice_scene()

def voice_scene():
    dramatic_print("You decide to pick up the sandal and are suddenly overwhelmed with the power of every Hispanic parent ever.")
    dramatic_print("You throw it and it takes out the survivors and it breaks the statue into many pieces. Coming out supreme.")
    dramatic_print("You celebrate and just as you stop a glowing Light appears, it takes you in a divine tone.")
    dramatic_print("The mysterious voice says your name and begins to talk about your bravery...")
    dramatic_print("Then offers you to jon it in the heavens to become almighty.")
    choice = get_choice("Do you want to accept or decline? (accept/decline) ", ["accept", "decline"])
    if choice == "accept" or choice == "decline":
        dramatic_print("Before you could answer, a crowd of mutated zombies, people and animals come out of nowhere...")
        dramatic_print("Within minutes you're overpowered and you lose your sandal, forcing you to run.")
        final_scene()

def final_scene():
    dramatic_print("The mysterious voice speaks to you, to make the choice now: either keep running or accept the offer and wipe out the horde.")
    time.sleep(1.5)
    choice = get_choice("What is your final decision? (accept offer/forfeit offer) ", ["accept offer", "forfeit offer"])
    if choice == "forfeit offer":
        dramatic_print("You keep running to find weapons laying on the ground, grabbing an axe and prepare to fight...")
        game_over("But the horde ascends to godhood and evaporates you in seconds.")
    else:
        dramatic_print("You accept the offer, now beginning to radiate a bright light.")
        dramatic_print("You test out your new found powers, soaring through the sky and obliterating the horde.")
        dramatic_print("You ascend to the heavens... but are shocked to find out the voice was Dr. House.")
        dramatic_print("He tells you that you are now his test subject for new medicine for the rest of eternity.")

# Start the story
wake_up_scene()
