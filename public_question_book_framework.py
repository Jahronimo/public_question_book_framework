#script containing questions contained within four bigger sections...  
#reflective, observational, actionable and reviewing progress.
# Within four sections there are 140 different subsection 
#branches of subjects for focused questions.
#including randomised variables making millions of combinations of questions.
#each reader can have their own completely unique book made.

# book structuring line organiser.
question_sections_edge_dividers_for_bottom_of_page = "_"*150 + "\n"

#_____editiable global variables________________________________________________
#number of questions within each subsections.
num_question_to_display = 8

#user details. within class to collapse information more cleanly.
class personal_details:
    first_name,last_name, = "jahronimo", "ellis"
    age, date_of_birth = 29, "28/04/1990"
    address = "83 newick road, Brighton, UK"
    postcode = "BN1 9JJ"
    phone_number = "07572935460"
    email = "Jahronimo1@hotmail.com"
    user_password = "horse_run_pasword_examples"
    """
    print("first_name: "
    "{}\nlast_name: "
    "{}\nAge: "
    "{}\ndate_of_birth: "
    "{}\nAddress: "
    "{}\npostcode: "
    "{}\nphone_number: "
    "{}\nemail: "
    "{}\nuser_password: "
    "{}".format(
        first_name,last_name, 
        age,date_of_birth, 
        address,postcode, 
        phone_number, 
        email, user_password))
    print (question_sections_edge_dividers_for_bottom_of_page)
    """
user_details = personal_details()

print (user_details.first_name)
#personal_details()

#_______________________________________________________________________________
#lists of variables to make more question variety. 
#within class to collapse information more cleanly.

class different_question_proprties:
    # different interchangeable elements that build up a question.
    intros_to_questions = [
    "Hello " + str(user_details.first_name) + ',',
    str(user_details.first_name) +' i have question for you',
    str(user_details.first_name) +' its question time!, ',
    'I hope your ok' + str(user_details.first_name)]

    #variables randomly alternative between and make more variation.

    topic_of_interest = [
    'designing a suitable book cover',
    'publishing the book',
    'promoting the book effectively',
    'collecting funding'
    ]

    time_scales = [
    "hour",
    "12 hours",
    "24 hours",
    "3 days",
    "week",
    "two weeks",
    "month"
    ]

    negitive_emotions = [
    'Worry', 
    'Stress',
    'Fear', 
    'Impatience'
    'Hate',
    'Anxiety'
    ]

    possitive_emotions = [
    'Enthusiastic',
    'Creative',
    'Empowered',
    'Free',
    'Optimistic',
    'Thankful'
    ]

    places_to_focus_on = [
    "in my house",
    "in my room",
    "on my way to work"
    ]

    groups_of_people = [
    "close friends", 
    "family",
    "work colleagues",
    "child"
    ]

    how_to_answer_questions = [
    'write 10 points of what you can do now',
    'write down 10 answers and start with and act upon the two best solutions',
    'spend 5-10 minutes preparing to make the biggest change you can now!', 
    "maybe contact someone and ask them if they agree with what your thinking!",
    "spend a minimum of 30 mins moving forward with the insight to this answer"
    ]
Question_elements = different_question_proprties()

#______THE BOOK FRAMEWORK_______________________________________________________
def TOP_PAGE_INFORMATION():
    #______________________________________________________________________________________________________________
    #printing title at the top of page.
    print (("Title: what do you think?").upper())

    print (("generated here will be a list of"),
    (num_question_to_display), ("questions with the subject interest of your choice regarding").upper(), (Question_elements.topic_of_interest))
    print (question_sections_edge_dividers_for_bottom_of_page)
    #______________________________________________________________________________________________________________
TOP_PAGE_INFORMATION()

import random
def Randomise(questions_lists):
    import random
    import secrets                           
    secure_random = secrets.SystemRandom()# creates a secure random object.
    group_of_items = questions_lists
    num_qustion_t_select = num_question_to_display                       
    list_of_random_items = secure_random.sample(group_of_items, num_qustion_t_select)
    # randomly selecting from strings within each question list
    for each_question in range (0, num_qustion_t_select):
    # I think this is where i need to add in some information but don't understand.
        
        #printing some kind of structure with numbers of question and space to answer.
        print (("Q."),(each_question + 1),((list_of_random_items[each_question])))
        print (("A."),(each_question + 1),("_______________________"))
        print ("\n")


#currently this randomly selects from lists and turns into a string
R_INTRO = str(random.choices(Question_elements.intros_to_questions))[2:-2]
R_TOPIC = str(random.choices(Question_elements.topic_of_interest))[2:-2]
R_TIME = str(random.choices(Question_elements.time_scales))[2:-2]
R_ANSWER = str(random.choices(Question_elements.how_to_answer_questions))[2:-2]
R_NEG_EMOTIONS =str(random.choices(Question_elements.negitive_emotions))[2:-2]
R_POS_EMOTIONS =str(random.choices(Question_elements.places_to_focus_on))[2:-2]
R_PLACES =str(random.choices(Question_elements.places_to_focus_on))[2:-2]
R_PEOPLE =str(random.choices(Question_elements.groups_of_people))[2:-2]


#_______________________________________________________________________________
#MAIN PARENT calling all other functions, everything else.
class bookbase(object):

    def all(self):

        #This function is to call and print all four sections of the book.. 
        #look within each function of sections to see each topic 
        #being called to each section. 

        #reflective
        Self_Assessment().print()        
        #obervational
        observation_section().print()
        #actionaable
        action_section().print()
        #revieiwing progress.
        review_section().print()

        print (question_sections_edge_dividers_for_bottom_of_page)
        Self_Assessment().print()
        Self_Assessment().Self_Assessment_1()
        Self_Assessment().Self_Assessment_questions_about_fear()
        Self_Assessment().Self_Assessment_questions_about_hope()
            #Self_Assessment().print()
        print (question_sections_edge_dividers_for_bottom_of_page)
            #Self_Assessment().Self_Assessment_questions_about_fear()

        observation_section().print()
        action_section().print()
        review_section().print()
        Sub2().print()
        Self_Assessment().print()
        Self_Assessment().Self_Assessment_questions_about_hope()
        print (question_sections_edge_dividers_for_bottom_of_page)

#_______________________________________________________________________________

class Self_Assessment(bookbase):
    def print(self):
        #function calls everything/Self_Assessment section 
        print (question_sections_edge_dividers_for_bottom_of_page)
        print (("Self_Assessment," 
        "Reflective self-analysis, "
        "past and present, "
        "actions and results,"
        "defining a problem and it's direct causes, "
        "indirect causes and effects, "
        "feelings, and thoughts.").upper())

        print (question_sections_edge_dividers_for_bottom_of_page)
        Self_Assessment().define_the_problem_Self_Assessment()
        Self_Assessment().Self_Assessment_1()
        Self_Assessment().Self_Assessment_questions_about_fear()
        Self_Assessment().Self_Assessment_questions_about_hope()


    def define_the_problem_Self_Assessment(self):

        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("define_the_problem_Self_Assessment")
        print ("here can include a little information")
        print ("\n")

        questions_lists = [
        (f"{R_INTRO} What might be the biggest problem regarding {R_TOPIC}?" 
        f"how to solve it within less than {R_TIME}? ,{R_ANSWER}"),

        (f"{R_INTRO} What have you been making more difficult than it should be"
        f"regarding {R_TOPIC}?, {R_ANSWER}"),

        (f"{R_INTRO} What types of things has been stopping you from reaching "
        f"your goals in the last {R_TIME} regarding {R_TOPIC}?" 
        f"{R_ANSWER}"),

        (f"{R_INTRO}, When Regarding {R_TOPIC}, Have you met your expectations"
        f"(why or why not?) {R_ANSWER}"),

        (f"{R_INTRO} Where are you struggling most regarding {R_TOPIC}? "
        f"how to reduce that struggle to be no problem in the next {R_TIME}?" 
        f"{R_ANSWER}"),

        (f"{R_INTRO} What problems have I been facing within the last {R_TIME} "
        f"regarding {R_TOPIC}? {R_ANSWER}"),

        (f"{R_INTRO} Where is my biggest problems "
        f"regarding {R_TOPIC}? {R_ANSWER}"),

        (f"{R_INTRO} What tasks have I been doing that doesn't contribute "
        f"towards my goal regarding {R_TOPIC}? {R_ANSWER}"),

        (f"{R_INTRO} Who is causing me most problems regarding {R_TOPIC}?"
        f" making it harder then they should be?"
        f" {R_ANSWER}"),

        (f"{R_INTRO} What are my most common problems "
        f"regarding {R_TOPIC}? {R_ANSWER}"),

        (f"{R_INTRO} Is a problem I am facing even worth solving "
        f"regarding {R_TOPIC}? {R_ANSWER}"),

        (f"{R_INTRO} What is my often main focus regarding {R_TOPIC}?, "
        f"is this pushing me towards my main objective or away from it?"),

        (f"{R_INTRO} When do I have the biggest feeling of {R_POS_EMOTIONS} "
        f"regarding{R_TOPIC}? {R_ANSWER}"), 

        (f"{R_INTRO} When am I most often feeling {R_NEG_EMOTIONS}"
        f"regarding {R_TOPIC}?,"
        f" how could i use this to my advantage? {R_ANSWER}"), 

        (f"{R_INTRO} When do you have the biggest feeling of {R_POS_EMOTIONS} "
        f"regarding{R_TOPIC}? {R_ANSWER}"), 

        (f"{R_INTRO} how do i react when feeling {R_NEG_EMOTIONS} "
        f" is this helping me regarding {R_TOPIC}?, {R_ANSWER}"),

        (f"{R_INTRO} Does a problem I am facing need an immediate solution "
        f"regarding {R_TOPIC}? or can it wait? {R_ANSWER}".format(R_INTRO,R_TOPIC,R_ANSWER)),

        (f"{R_INTRO} Have I ever been warned or told of any problems "
        f"that I might face regarding {R_TOPIC}? What could be the truth to it? "
        f"{R_ANSWER}"),

        (f"{R_INTRO} What problems regarding {R_TOPIC} have I been refusing to acknowledge "
        f"and identify? {R_ANSWER}"),

        (f"{R_INTRO} what are perceived as an obstacle towards hitting my goal "
        f"regarding {R_TOPIC}?  {R_ANSWER}"),

        (f"{R_INTRO} When do you feel your most aware of a critical problem "
        f"regarding {R_TOPIC}? {R_ANSWER}"),

        (f"{R_INTRO} Who can seem to give me insight from what they have done "
        f"or said, to taking the next positive step regarding {R_ANSWER}?"
        f" {R_INTRO}"),

        (f"{R_INTRO} Where is causing me unnecessary Stress "
        f"regarding {R_TOPIC}? {R_ANSWER}"),

        (f"{R_INTRO} what is causing me necessary positive Stress regarding {R_TOPIC}?"
        f" {R_INTRO}"),

        (f"{R_INTRO} Where are you inefficiently focusing on regarding {R_TOPIC}?"
        f" {R_ANSWER}"),

        (f"{R_INTRO} What am I doing that is counter productive regarding {R_TOPIC}?"
        f" {R_ANSWER}"),

        (f"{R_INTRO} Where is my goal being badly defined regarding {R_TOPIC}?"
        f"What sorts of problems is this creating?"
        f" {R_ANSWER}"),

        (f"{R_INTRO} How can I identify and create less daily problematic "
        f"resistances regarding {R_TOPIC}? "
        f"What should now be done? {R_ANSWER}"),
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)


    def Self_Assessment_1(self):

        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("Self_Assessment_1 ")
        print ("here can include a little information")
        print ("\n")

        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)), 
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)

        """           dont touch ---- templete to study
        print("if looking for answers, what will happen when I ask the right questions regarding {}?".format(Question_elements.topic_of_interest))
        print("Would I like to import regarding {}".format(Question_elements.topic_of_interest))
        print("I am aware there are thing to be improved upon regarding {}?".format(Question_elements.topic_of_interest))
        # example of multiple formattings using the same string
        print("this is showing {} multiple formattings of the same string {}".format(Question_elements.topic_of_interest,Question_elements.topic_of_interest))
        # example of multiple formattings with different strings
        print("{} is the first, {} is the second".format('1', '2'))
        # example of multiple formattings and declaring
        print("{first} is the first, {third} is the second, {second} is the last".format(first='1', second='2', third='3'))
        #Self_Assessment().Self_Assessment_1()
        print (question_sections_edge_dividers_for_bottom_of_page)
        """


    def Self_Assessment_questions_about_fear(self):
        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("Self_Assessment_questions about fear ")

        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)


    def Self_Assessment_questions_about_hope(self):
        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("Self_Assessment_questions about fear ")

        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),        
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)
#_______________________________________________________________________________


class observation_section(bookbase):
    def print(self):
        print('My direct parents are:', ', '.join([
            cls.__name__ for cls in type(self).__bases__]))
        all_parents = type(self).__mro__
        all_parents = all_parents[all_parents.index(observation_section) + 1:]
        print('All my parents are:', ', '.join([
            cls.__name__ for cls in all_parents]))

        observation_section().test_observational_questions_aboutgeneral_health()
        observation_section().test_observational_questions_aboutdaily_exercises()
        observation_section().test_observational_questions_aboutstart_with_the_end()
        observation_section().test_observational_questions_aboutalternative()
        observation_section().test_observational_questions_abouthigh_and_low_intensity()
        observation_section().test_observational_questions_about100_percent()
        observation_section().test_observational_questions_aboutresponsibility()


    def observational_questions_about_fear(self):
        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("section name ")


        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),        
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)


    def test_observational_questions_aboutgeneral_health(self):
        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("section name ")

        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),        
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)


    def test_observational_questions_aboutdaily_exercises(self):
        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("section name ")

        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),        
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)


    def test_observational_questions_aboutstart_with_the_end(self):
        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("section name ")

        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),        
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)


    def test_observational_questions_aboutalternative(self):
        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("section name ")

        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),        
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)


    def test_observational_questions_abouthigh_and_low_intensity(self):
        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("section name ")

        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),        
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)


    def test_observational_questions_about100_percent(self):
        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("section name ")

        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),        
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)


    def test_observational_questions_aboutresponsibility(self):
        print (question_sections_edge_dividers_for_bottom_of_page)
        print ("section name ")

        questions_lists = [
        ("{} who         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} What         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} Where         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),  
        ("{} When         regarding {}? {}".format(R_INTRO,R_TOPIC,R_ANSWER)),        
        ]

        Randomise(questions_lists)
        print (question_sections_edge_dividers_for_bottom_of_page)


#_______________________________________________________________________________


class action_section(bookbase):
    def print(self):
        print('My direct parents are:', ', '.join([
            cls.__name__ for cls in type(self).__bases__]))
        all_parents = type(self).__mro__
        all_parents = all_parents[all_parents.index(action_section) + 1:]
        print('All my parents are:', ', '.join([
            cls.__name__ for cls in all_parents]))
#_______________________________________________________________________________

class review_section(bookbase):
    def print(self):
        print('My direct parents are:', ', '.join([
            cls.__name__ for cls in type(self).__bases__]))
        all_parents = type(self).__mro__
        all_parents = all_parents[all_parents.index(review_section) + 1:]
        print('All my parents are:', ', '.join([
            cls.__name__ for cls in all_parents]))
#_______________________________________________________________________________


class Sub2(Self_Assessment):
    def print(self):
        print('My direct parents are:', ', '.join([
            cls.__name__ for cls in type(self).__bases__]))
        all_parents = type(self).__mro__
        all_parents = all_parents[all_parents.index(Sub2) + 1:]
        print('All my parents are:', ', '.join([
            cls.__name__ for cls in all_parents]))
        print ("potato")


#Self_Assessment().eat_healthily_Self_Assessment_questions_()

#personal_details()
#Self_Assessment().print()
Self_Assessment().define_the_problem_Self_Assessment()
#Self_Assessment().Self_Assessment_1()
#Self_Assessment().Self_Assessment_questions_about_fear()
#Self_Assessment().print()
#bookbase().all()

#observation_section().observational_questions_about_fear()

#Self_Assessment().eat_healthily_Self_Assessment_questions_()