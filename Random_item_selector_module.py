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

