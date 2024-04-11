#function to check if the message is a command or a message
from flask_socketio import emit


command_list = [
    "start",
    "end",
    "score",
    "help",
    "commands",
    "feedback",
    "roleplays",
    
    ]
# remove the slash from the command and  return the first word as the command and the rest as the message
def parse_command(message:str):
    msg = ""
    command = message.split(" ")[0][1:]
    message = message.split(" ")[1:]
    msg = " ".join(message)
    return command, msg

def is_command(message):
    if message.startswith("/"):
        return True
    else:
        return False

def is_valid_command(command):
    if command in command_list:
        return True
    else:
        return False
    
def command_check(message):
    if is_command(message):
        command, msg = parse_command(message)
        if is_valid_command(command):
            return command, msg
        else:
            return "invalid command", "invalid command"
    else:
        return "message", message

#placeholder function for mock command responses
def placeholder_mock_commands(command:str, message:str):
    #this function is a placeholder for the command response function
    # we should emit a message to the socketio server
    emit("message", {"msg":f"Command: {command} Message: {message}"})
    return "Command: {command} Message: {message}"


def command_response(command:str, message:str):
    if command == "start":
        #this starts a roleplay session by prompting the AI with the nessary roleplay details
        placeholder_mock_commands(command, message)
        # this should start the roleplay with the ai 
        #AND SET THE FLAG TO TRUE ALSO SEND THE GUIDE TO THE FRONTEND
        return "Roleplay has started"
    elif command == "end":
        #this ends the roleplay session and scores the roleplay
        placeholder_mock_commands(command, message) 
        #this should end the roleplay and score the roleplay
        #and update the score box
        return "Roleplay has ended"
    elif command == "score":
        #this scores the roleplay session
        placeholder_mock_commands(command, message)
        #this should score the roleplay and update the score box

        return "Roleplay has been scored"
    elif command == "help":
        # this should display hints and tips for the user
        placeholder_mock_commands(command, message)
        # this needs another function to call to the AI to evaluate and  give some feed back
        return "Help has been requested"
    elif command == "commands":
        # this should display the list of commands
        placeholder_mock_commands(command, message)

        return "Commands have been requested"
    elif command == "feedback":
        # this should send feedback to the the user about how they are doing and update the score as well as sending 
        placeholder_mock_commands(command, message)
        return "Feedback has been requested"
    else:
        return "Invalid command"
    

#  once the command is parsed, the command is checked to see if it is a valid command.
#  if the command is valid, the command is executed and a response is returned.
