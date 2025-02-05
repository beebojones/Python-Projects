# Characters
wizard = "Wizard"
elf = "Elf"
human = "Human"

# Character Health Points
wizard_hp = 70
elf_hp = 100
human_hp = 200

# Character Damage
wizard_damage = 150
elf_damage = 100
human_damage = 50

# Enemies Health Points
dragon_hp = 300
non_human_baby_hp = 10 

# Enemies Damage
dragon_damage = 25
non_human_baby_damage = 1000

def play_game():
    while True:
        print("1) Wizard")
        print("2) Elf")
        print("3) Human")
        print("4) Exit")
        print("Choose your character:")
        character = input().strip()

        if character in ["1", "Wizard", "wizard"]:
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if character in ["2", "Elf", "elf"]:
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if character in ["3", "Human", "human"]:
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        if character in ["4", "Exit", "exit"]:
            exit()
        print("Unknown character, please choose again.")

    while True:
        print("1) Dragon")
        print("2) Non-Human Baby")
        print("3) Exit")
        print("Choose your enemy:")
        enemy = input().strip()

        if enemy in ["1", "Dragon", "dragon"]:
            enemy = "Dragon"
            enemy_hp = dragon_hp
            enemy_damage = dragon_damage
            break
        elif enemy in ["2", "Non-Human Baby", "non-human baby"]:
            enemy = "Non-Human Baby"
            enemy_hp = non_human_baby_hp
            enemy_damage = non_human_baby_damage
            break
        elif enemy in ["3", "Exit", "exit"]:
            exit()
        else:
            print("Unknown enemy. Please choose again.")

    while True:
        print("\nChoose your action:")
        print("1) Attack")
        print("2) Defend")
        action = input().strip()

        if action in ["1", "Attack", "attack"]:
            enemy_hp -= my_damage
            print(f"\nThe {character} damaged the {enemy}!")

        elif action in ["2", "Defend", "defend"]:
            my_hp -= (enemy_damage / 2)
            print(f"\nThe {character} is defending against the {enemy}!")
        else:
            print("Unknown action. Please choose again.")
            continue

        # Check if the non-human baby dies before it can attack
        if enemy == "Non-Human Baby" and enemy_hp <= 0:
            print(f"\nThe {enemy} has been defeated! Good for you, I guess. Do you feel like a big, powerful, grown-up now?")
            break

        # Enemy's turn to attack
        if enemy_hp > 0:
            my_hp -= enemy_damage
            print(f"The {enemy} damaged the {character}!")

        # Display current health points
        print(f"\nYour HP: {my_hp}")
        print(f"Enemy HP: {enemy_hp}")

        # Check for battle end conditions
        if my_hp <= 0:
            print(f"\nThe {character} has lost the battle!")
            break
        if enemy_hp <= 0:
            print(f"\nYou've won! You smile proudly as you hold {enemy}'s head in your hand.")
            break

while True:
    play_game()
    print("\nDo you want to play again? (yes/no)")
    play_again = input().strip().lower()
    if play_again not in ["yes", "y"]:
        print("Thanks for playing! Goodbye!")
        break
