# This is a pipeline that will be split into multiple files once completed

# Migrate questions into this API's DB (mysql)
# 1. Pull all questions from Trees_API
# 2. Verify big5 questions with Jonny/Steve

# Pull big5 questions into dictionary that contains their q_ids mapped to the question_text
# Also, map each big5 question to the category of the big5 traits that this applies to.

# Also, pull answers to these questions and have a dictionary that maps each answer to a binary
# 0 or 1 value depending on whether the answer would illustrate a user has this trait (1) or doesn't (0)

# Example:
# slider_question: "I talk to a lot of different people at parties."
# - isbig5 = true
# - big5category = extraversion
# - answer_map = {"YesYesYesYesYes": 1, ..., "Yes": 1, "Indifferent": -1, "No": 0, "NoNoNoNoNo": 0}


# Steps of the Pipeline:
# 1. Generate 20-80 answer's to questions that exist within the Trees mobile application
#   a. Generate k batches (k=10?) with a varying number of answer's
# 2. Generate a list of what each question id "means" - i.e. what is the answer associated with the question supposed to reflect about the individual answering it?
#   a. Use GPT model with input of every question and every question_id to generate an output message that can easily be mapped to a dictionary of 
#      every question id paired with a short (<100 word) statement about what that question id "means"
# 3. Generate a 100-500 word statement describing what the "user's" answers mean - i.e. how can they use the app most effectively based on their 
#    answers to the question

def get_questions(number_of_questions):
    n = number_of_questions

    for i in range(n):
        # Get a question with a unique question id
        pass

    return 0