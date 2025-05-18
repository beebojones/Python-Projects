import random
import time

def magic_8_ball():
    print("Welcome to the Legally Different Magic 8-Ball!")
    print("Ask me your questions... and I'll tell you no lies. Or you could waste both out time and type 'quit' to exit.")
    print("Let us begin again...\n")
    
    magic_8_ball_responses = [
        "I'm doing that thing where the die gets stuck or whatever and none of the sides with my responses on them are 'tecnically' pointing towards you. So, this doesn't count. For legal reasons, I'll need you to ask me again.",
        "What are you going to do with her?",
        "As they say, if you have to ask, you can't afford it.",
        "I'm not sure you can handle the truth... It's no by the way.",
        "Yeah, but your goin will be sore.",
        "Sure. My only ask is that you simply pay off my student loans. Do you happen to have 87 million dollars?",
        "Let me check my crystal ball... Oh, wait. That's so embarrassing... That's a snow globe. Let's just say yes.",
        "...here's always a chance, darling.",
        "I'm going to pretend I didn’t hear that.",
        "No comment. Wait... No. What did you say? Yes. No.",
        "Yes, but that's natural at your age I would imagine"
    ]

    while True:
        user_question = input("What's your question? ")

        if user_question.strip().lower() in ["quit", "exit"]:
            print("Alright, alright. Come back when you need more questionable advice.")
            break
        
        # Brief pause before giving the answer
        time.sleep(2)  # Pause for 2 seconds
        print("Hold still.")
        time.sleep(2)  # Pause for 2 seconds
        print("I'm thinking.")
        print("")
        time.sleep(2)  # Pause for 2 seconds

        answer = random.choice(magic_8_ball_responses)
        print(f"Magic 8-Ball says: {answer}\n")
        time.sleep(2)  # Pause for 2 seconds
        
if __name__ == "__main__":
    magic_8_ball()
