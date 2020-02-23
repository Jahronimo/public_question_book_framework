# question_book_framework

"""
I would like to make a script to randomly selects x number of questions from 4 big major sections and around 140 subsections
 and display them ready for a book of questions. to help people think about problems a little different. 

 for personalized experiences, users are show questions with randomised strings from lists of different aspects of the questions.  update the questions accordingly 
 
right now I want to make sure the structure is correct before starting to add in masses of questions. 


i am having trouble with the randomise function line 76. I have randomised the questions being selected from each list within each sections.
although i have not got each element within the class different_question_properties:


I had it working and was using a for loop but broke it an lost track of what i need to do.

please help by implimenting the randomised elements.
i am half sure i need to add these into the randomise function. 
there are just below.

R_INTRO = str(random.choices(Question_elements.personal_introductions_to_questions))[2:-2]
R_TOPIC = str(random.choices(Question_elements.topic_of_interest))[2:-2]
R_TIME = str(random.choices(Question_elements.time_scales))[2:-2]
R_ANSWER = str(random.choices(Question_elements.how_to_answer_questions))[2:-2]
R_NEG_EMOTIONS =str(random.choices(Question_elements.negitive_emotions))[2:-2]
R_POS_EMOTIONS =str(random.choices(Question_elements.places_to_focus_on))[2:-2]
R_PLACES =str(random.choices(Question_elements.places_to_focus_on))[2:-2]
R_PEOPLE =str(random.choices(Question_elements.groups_of_people))[2:-2]


"""