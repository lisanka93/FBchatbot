import random
from collections import Counter


#NOTES: COMMENTS ON LINE 60 and 62

#explanation and negation lists
expl = ['that is', 'because', 'due to', 'since', 'that\'s', 'thats', 'hence', 'therefore']
neg = ['not', 'dont', 'arent', 'cant', 'wouldnt', 'isnt', 'don\'t', 'aren\'t', 'can\'t', 'wouldn\'t', 'isn\'t']
time = ['busy', 'time']
things = ['things', 'stuff']

'''function to handle responses. I assume that a response below 12 words is too short and chatbot will query again (once),
-1 will be added to checkpoint list, see query function (first part of if-statement). If statement long enough or chatbot
already queried once, next question is asked (second part of if-statement, after "else")'''

#append 3 check if its long enough, if no -1, ask what to advise friend append 4, if too short expand please add -2 otherwise 5
#why dont do that append 6 if 5 or -2, get response if long enough append 7 if not -3, ask what adivse would give friend append 8 if too short exand add -4 otherwise 8

# ask for more respns

def long_enpough(checkpointlist):


    if checkpointlist[-1] == 3 or checkpointlist[-1] == -1:
        response = "Imagine now your friend who has the same problem is also not very physically active but would like to do more sports and is asking you for advice. What would you tell her? "
        checkpointlist.append(4)
        return response, checkpointlist

    if checkpointlist[-1] == 4 or checkpointlist[-1] == -2:
        responses = ['So you know how to do more exercise! Why dont you do that?',  'I see you know how to do more exercise - may I ask why you don\'t do that?']
        response = random.choice(responses)
        checkpointlist.append(5)
        return response, checkpointlist


    if checkpointlist[-1] == 5 or checkpointlist[-1] == -3:

        response = "What advise would you give a friend who has the same reason as you on how to be more physically active?"
        checkpointlist.append(6)
        return response, checkpointlist

    if checkpointlist[-1] == 6:
        response = "great, thank you! do you have another major reason for not doing sports regularly. "
        checkpointlist.extend([8,88])
        return response, checkpointlist



def handle_response(statement, checkpointlist):
    #make list out of otions and make "if blah in list statement "
    possibilities = [3,4,5,6]
    #if checkpointlist[-1] == 3 or checkpointlist[-1] == 5 or checkpointlist[-1] == 6 or checkpointlist[-1] == 8 or checkpointlist[-1] ==9:
    if checkpointlist[-1] in possibilities:
        if len(statement.split()) < 12:
            #checking stages in checkpointlist and calling respective function
            response = query(statement)
            if checkpointlist[-1] == 3:
                #if 3 overwrite with query1
                response = query1(statement)
                checkpointlist.append(-1)
                return response, checkpointlist
            if checkpointlist[-1] == 4:
                checkpointlist.append(-2)
                return response, checkpointlist
            if checkpointlist[-1] == 5:   #maybe here query1 too? "why dont you do that"
                response = query1(statement)
                checkpointlist.append(-3)
                return response, checkpointlist
            if checkpointlist[-1] == 6:   #same here- query1 maybe?
                checkpointlist.append(7)
                return response, checkpointlist

        else:
            response, checkpointlist = long_enpough(checkpointlist)
            return response, checkpointlist

    if checkpointlist[-1] < 0:
        response, checkpointlist = long_enpough(checkpointlist)
        return response, checkpointlist

    if checkpointlist[-1] == 7:
        response = "great, thank you! do you have another major reason for not doing sports regularly. "
        checkpointlist.extend([8,88])
        return response, checkpointlist


    if checkpointlist[-1] == 8:
            #checking if user wants to proceed or finish conversation
        if statement == "yes":
            response = "awesome, what is it?"
            checkpointlist.append(3) #start from beginning
        elif statement == "no":
            response = "Ok, thank you very much for your time :) good bye. \n if you found me through prolific, please click here: https://www.prolific.ac/submissions/complete?cc=JQXWIXG2"
            checkpointlist.append(9) #finishes conversation
        else:
            response = "sorry, I didnt get that, please say yes or no"
            checkpointlist.append(88)
        return response, checkpointlist

    if checkpointlist[-1] == 9:
        response = "byeee"
        return response, checkpointlist







#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""the function is invoked if the user response was not long enough and the chatbot asks to expand,
if statement very short, answers a bit difference than with a bit longer statements, if answer inclused negation
or explanation, chatbot response differs too"""

def query1(statement):  #statement = userinput

    quest = "? "
    statement = statement.lower()

    word_tok = statement.split()
    statement_length = len(word_tok)
    if statement_length == 1:
        responses = ['can you expand that please :) why so?',
                    'that\'s not enough, elaborate please',
                    'please tell me more...', 'expand please...',
                    'please expand :)']
        resp = random.choice(responses)
        response = statement + quest + resp
        return response


    j = dict((i, statement.count(i)) for i in time)
    time_nr = sum(j.values())

    if time_nr > 0:
        responses = ['I understand you have no time, but can you expand on that please. Why not, what do you usually do when you have time?',
                    'You say you have no time for sports, right? But why not - what do you do in your free time?',
                    'But why don\'t you have time? What do you do instead?']
        response = random.choice(responses)
        return response

    z = dict((i, statement.count(i)) for i in things)
    thing_nr = sum(z.values())

    if thing_nr > 0:
        responses = ['I understand you prefer other things. Like what? Please expand..',
                    'I understand you like doing other things than sports - like what?',
                    'You say you like doing other things - can you name some examples please?']
        response = random.choice(responses)
        return response

    d = dict((i, statement.count(i)) for i in expl)
    expl_nr = sum(d.values())

    if expl_nr > 0:
        print "i should be here"
        responses = ['Okay, but what makes you say that?',
                    'Could you go into more detail? Why do you say that?',
                    'Fair enough. But what makes you say that?',
                    'Elaborate please. Why do you say that? ',
                    'A bit more detail please. What makes you say that?']
        response = random.choice(responses)
        return response

    k = dict((i, statement.count(i)) for i in neg)
    neg_nr = sum(k.values())

    if neg_nr > 0:
        responses = ['Why not?',
                    'Tell me a bit more. Why not?']
        response = random.choice(responses)
        return response






    if statement_length <= 5:
        responses = ['a bit more detail please! Why?',
                    'Why?', 'Okay, but why?',
                    'Why? Tell me :)']
        response = random.choice(responses)
        return response

    if statement_length > 5:
        responses = ['can you expand that please :) why so?',
                    'elaborate please...',
                    'please tell me more...',
                    'expand please...', 'please expand :)']
        response = random.choice(responses)
        return response

def query(statement):  #statement = userinput

    quest = "? "
    statement = statement.lower()

    word_tok = statement.split()
    statement_length = len(word_tok)
    if statement_length == 1:
        responses = ['can you expand that please :) why so?',
                    'that\'s not enough, elaborate please',
                    'please tell me more...', 'expand please...',
                    'please expand :)']
        resp = random.choice(responses)
        response = statement + quest + resp
        return response

    d = dict((i, statement.count(i)) for i in expl)
    expl_nr = sum(d.values())

    if expl_nr > 0:
        print "i should be here"
        responses = ['Okay, but what makes you say that?',
                    'Could you go into more detail? Why do you say that?',
                    'Fair enough. But what makes you say that?',
                    'Elaborate please. Why do you say that? ',
                    'A bit more detail please. What makes you say that?']
        response = random.choice(responses)
        return response



    k = dict((i, statement.count(i)) for i in neg)
    neg_nr = sum(k.values())

    if neg_nr > 0:
        responses = ['Why not?',
                    'Tell me a bit more. Why not?']
        response = random.choice(responses)
        return response



    if statement_length <= 5:
        responses = ['a bit more detail please! Why?',
                    'Why?', 'Okay, but why?',
                    'Why? Tell me :)']
        response = random.choice(responses)
        return response

    if statement_length > 5:
        responses = ['can you expand that please :) why so?',
                    'elaborate please...',
                    'please tell me more...',
                    'expand please...', 'please expand :)']
        response = random.choice(responses)
        return response
