#imports random library to add random chance functionality
import random


#takes the user's message as a parameter and returns string response
def handle_response(message) -> str:
    #sets variable to lowercase version of the user's message
    p_message = message.lower()
    
    #checks if message is valid and answers accordinly
    if p_message == "!help":
        return "`I can roll a dice, say hello and say bye`"
    elif p_message == "hello":
        return "Hey there!"
    elif p_message == "bye":
        return "See you!"
    elif p_message == "roll":
        return random.randint(1, 6)
    else:
        return "I don't understand you"
