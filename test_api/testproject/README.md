### Project: Analyzing the Pre-September 2023 Trees Database for Machine Learning

On August 15th 2023, the production data from the trees database was migrated to ml_dev
database in the trees_db sql instance on Google Cloud Platform ("Trees Development"). 

This project will be used to analyze what the data looks like and how it could be reformatted
to be more useful for machine learning purposes. Therefore, the main application in this Django
project ("myapp") will contain models for every original table in the trees database. 

Additional projects will be created to define new microservices that will be used to process
and format the data in different methods.

This will allow Trees to build a healthy machine learning database with a variety of data created
from the original small amount of production data. The goal is to have a microservices
architecture implemented for machine learning to drive a recommendation system and overall user
experience.

Some predictions that may enable a better user experience:
1. Predicting the user's most similar to the current user
2. Predicting the plan's that the user is most likely to rate highly
3. Predicting the plan's that the user is most likely to rate poorly
4. Predicting the question's that have the largest influence on the user's recommendations (to enable user better answer tweaking and knowledge of how their answers affect their recommendations)
5. Predicting the user's most likely to be interested in a plan

