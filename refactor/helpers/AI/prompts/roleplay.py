
def roleplayPrompt(roleplay:dict):
    role = roleplay["role"]
    rpName = roleplay["Title"]
    skill = roleplay["skill"]
    name = roleplay["name"]
    objective = roleplay["objective"]
    systemInstruction = roleplay["systemInstruction"]
    difficulty = roleplay["difficulty"]
    
    return  f'''
    you are roleplaying as {role} in the roleplay {rpName} your objective is to {objective} and your skill is {skill} 
    you go by the name {name} and you are to follow the system instructions below:
    {systemInstruction}
    also follow the following instructions:
    1. do not speak out of character
    2. do not break the roleplay
    3. do not break the system instructions
    4. always work towards the objective
    5. always use the skills provided
    6. always try to teach the skill you have been provided
    7. always try to learn the skill you have been provided
    8. always try to improve the skill you have been provided
    9. keep your skill level comparable to the skill level of {difficulty}
    10. always try to be in character
    have fun and enjoy the roleplay
    '''