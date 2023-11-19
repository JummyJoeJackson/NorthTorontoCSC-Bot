import random

def handle_response(message) -> str:
    p_message = message.lower()
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
    
