def scoringprompt(roleplay:dict):
    expert_in = roleplay["expert"]
    role = roleplay["role"] 
    skill = roleplay["skill"]
    objective = roleplay["objective"]
    instruction = '''`
    you and the user are roleplaying you are in the role of {role} roleplaying as {name} your objective is to {objective} and your skill is {skill}
    they are trying to learn the skill you have been provided and you are trying to teach the skill you have been provided
    you are an expert in {expert_in} and you are to you are trying to teach them, they're objective is {objective} and they are trying to learn the skill you have been provided
    please please look at the conversation history and answer the following questions :
    1. did they complete the objective
    2. did they use the skill provided
    3. how well they used the skill 
    4. how could they improve the skill
    5. how could they improve the use of the skill
    6. the best way to continue the conversation to reach the objective
    7. whats the percentage of completeness of the objective
    8. what skill level do they possess
    9 WHAT DID THEY DO WELL
    10. WHAT COULD THEY IMPROVE
    11. WHAT THE DID WRONG
    
I need you to provide feedback based on a roleplay performance. Please use the following scoring criteria and adhere to a JSON output structure.

Criteria

knowledge_acquisition: (Briefly explain what this criterion assesses)
skill_application: (Briefly explain what this criterion assesses)
critical_thinking: (Briefly explain what this criterion assesses)
engagement: (Briefly explain what this criterion assesses)
emotional_intelligence: (Briefly explain what this criterion assesses)
self_reflection: (Briefly explain what this criterion assesses)
transferability: (Briefly explain what this criterion assesses)
JSON Output Structure

JSON
{ 
  "knowledge_acquisition": {
    "score": 0,  // 0 to 5
    "feedback": ""  // Your feedback text here
   },
  "questions_answers": {
    "summary_of_questions": str,  // you answers to the questions above
    "feedback": ""  // Your feedback text here
   },
  "skill_application": {
    "score": 0,
    "feedback": ""
  },
  // ... (Repeat for each criterion)
  "overall_feedback": "" // Your summary comments

 }
Instructions for Gemini Advanced

Scoring: For each criterion, assign a score between 1 and 5. Consider the roleplay performance and how it aligns with the criterion's explanation.

Feedback:  Provide specific, constructive feedback explaining the rationale behind your score for each criterion. Refer back to the roleplay scenario as needed.

Overall Feedback:  Provide a brief summary of the roleplayer's strengths and areas for improvement.

Remember:

Replace the criterion explanations with your own brief descriptions.

Provide the roleplay context/transcript to Gemini Advanced as a separate input for evaluation.'''