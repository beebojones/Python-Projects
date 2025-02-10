import random

class SlotMachine:
    def __init__(self):
        self.symbols = ['Cherry', 'Lemon', 'Orange', 'Plum', 'Bell', 'Bar']
        self.balance = 100
        self.consecutive_wins = 0

    def spin(self, bet):
        if bet > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= bet

        reels = [random.choice(self.symbols) for _ in range(3)]
        print(f"You spun: {reels[0]} | {reels[1]} | {reels[2]}")

        if reels[0] == reels[1] == reels[2]:
            payout = bet * 10
            self.balance += payout
            print(f"Congratulations, you won ${payout}!")
            self.consecutive_wins += 1
            if self.consecutive_wins == 2:
                print("The Manager of the Casino appears and starts keeping an eye on you...")
        elif reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
            payout = bet * 2
            self.balance += payout
            print(f"Congratulations, you won ${payout}!")
            self.consecutive_wins += 1
            if self.consecutive_wins == 2:
                print("The Manager of the Casino appears and starts keeping an eye on you...")
        else:
            print("Better luck next time.")
            self.consecutive_wins = 0

    def play(self):
        while True:
            print(f"\nBalance: ${self.balance}")
            if self.balance == 0:
                print("You stare into the slot machine and think of your family...")
                bet_the_house = input("Do you want to 'Bet the House'? (Y/N): ").upper()
                if bet_the_house == "Y":
                    print("Your wife appears with tears in her eyes... Haven't you done enough to this family")
                    break
                elif bet_the_house == "N":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            else:
                bet = input(f"Enter your bet (1-{self.balance}), or type 'quit' to exit: ")
                if bet.lower() == 'quit':
                    break
                try:
                    bet = int(bet)
                    if bet < 1 or bet > self.balance:
                        print(f"Invalid bet. Please enter a number between 1 and {self.balance}.")
                    else:
                        self.spin(bet)
                except ValueError:
                    print("Invalid input. Please enter a number or type 'quit' to exit.")

    def main_menu(self):
        while True:
            print("\n**Slot Machine Game**")
            print("------------------------")
            print("P - Play the game")
            print("Q - Quit the game")
            choice = input("Enter your choice: ").upper()
            if choice == "P":
                self.play()
            elif choice == "Q":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game = SlotMachine()
    game.main_menu()
