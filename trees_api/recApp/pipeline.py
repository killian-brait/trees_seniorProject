# This is a pipeline that will be split into multiple files once completed

# Steps of the Pipeline:
# 1. Generate 20-80 answer's to questions that exist within the Trees mobile application
#   a. Generate k batches (k=10?) with a varying number of answer's
# 2. Generate a list of what each question id "means" - i.e. what is the answer associated with the question supposed to reflect about the individual answering it?
#   a. Use GPT model with input of every question and every question_id to generate an output message that can easily be mapped to a dictionary of 
#      every question id paired with a short (<100 word) statement about what that question id "means"
# 3. Generate a 100-500 word statement describing what the "user's" answers mean - i.e. how can they use the app most effectively based on their 
#    answers to the question


