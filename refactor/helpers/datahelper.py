
import os
import json
# list the available roleplays 
def list_roleplays()->list:
    roleplay_file_location = "refactor/data/roleplays/"
    #open and list the files in the roleplay folder
    roleplay_files = os.listdir(roleplay_file_location)
    return roleplay_files

# read selected roleplays yaml or json file
def read_roleplay_file(roleplay:str)->dict:
    roleplay_file_location = "refactor/data/roleplays/"
    roleplay_file = roleplay_file_location + roleplay
    roleplay_dict = {}
    if roleplay_file.endswith(".yaml"):
        with open(roleplay_file, 'r') as file:
            import yaml
            roleplay_dict = yaml.load(file, Loader=yaml.FullLoader)
    elif roleplay_file.endswith(".json"):
        with open(roleplay_file, 'r') as file:
            import json

            roleplay_dict = json.load(file)
    else:
        return "Roleplay not found"
    return roleplay_dict


# create a roleplay dictionary from the roleplay 
def create_roleplay_dict(roleplay:str)->dict:
    if roleplay.endswith(".yaml") and roleplay in list_roleplays():
        roleplay_dict = read_roleplay_file(roleplay)
        return roleplay_dict
    elif roleplay.endswith(".json") and roleplay in list_roleplays():
        roleplay_dict = read_roleplay_file(roleplay)
        return roleplay_dict
    else:
        return "Roleplay not found"
    
# save session
def save_session(session):
    session_file_location = "refactor/static/data/session_data/"
    session_file = session_file_location + "session" + ".json"
    with open(session_file, 'w') as file:
        json.dump(session, file)

# load session
def load_session():
    session_file_location = "refactor/static/data/session_data/"
    session_file = session_file_location + "session" + ".json"
    session_dict = {}
    with open(session_file, 'r') as file:
        session_dict = json.load(file)
    return session_dict

