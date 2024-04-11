#A PROMPT TO RETURN JSON ONLY 
instruct = '''
Your response should be in JSON format.
with no other text in the response.
the response should be in the following format:
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
    reply with the JSON response only
    replacing none of the keys and filling in the values as needed

'''