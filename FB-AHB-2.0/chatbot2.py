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

def long_enpough(checkpointlist):
    """if I want to append another value-question, the next one would be checking for 11, then scip and then 13 for next value etc."""
    value_for_arg = [3, -1, 6, -3, 9, -5]
    if checkpointlist[-1] in value_for_arg:
        response = "What value does your argument promote? Please pick one of the following: \n \n responsibility \n comfort \n dignity \n satisfaction \n relaxation \n family \n friendship \n professionalism \n productivity \n wealth \n knowledge \n fun \n recreation \n ambition \n safety"

        if checkpointlist[-1] == 3 or checkpointlist[-1] == -1:
            checkpointlist.extend([4,99])
            if 14 not in checkpointlist:
                response = "What value does your argument promote? A value is the underlying goal or motivation of your argument. For example the argument \"I don\'t go to the gym because it\'s expensive\" promotes the value \"wealth\" \n   Please pick one of the following:\n \n responsibility \n comfort \n dignity \n satisfaction \n relaxation \n family \n friendship \n professionalism \n productivity \n wealth \n knowledge \n fun \n recreation \n ambition \n safety"
        elif checkpointlist[-1] == 6 or checkpointlist[-1] == -3:
            checkpointlist.extend([7,99])
        elif checkpointlist[-1] == 9 or checkpointlist[-1] == -5:
            checkpointlist.extend([10,99])
        else:
            print "blubb"
    else:
        responses = ['So you know how to do more exercise! Why dont you do that?', 'Great advise! But why don\'t you do that yourself?', 'May I ask why you don\'t do that?']
        response = random.choice(responses)

        if checkpointlist[-1] == 5 or checkpointlist[-1] == -2:
            checkpointlist.append(6)
        elif checkpointlist[-1] == 8 or checkpointlist[-1] == -4:
            checkpointlist.append(9)
        else:
            print "blubb"


    return response, checkpointlist


def handle_response(statement, checkpointlist, values):
    #make list out of otions and make "if blah in list statement "
    possibilities = [3,5,6,8,9]
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
            if checkpointlist[-1] == 5:
                checkpointlist.append(-2)
                return response, checkpointlist
            if checkpointlist[-1] == 6:   #maybe here query1 too? "why dont you do that"
                response = query1(statement)
                checkpointlist.append(-3)
                return response, checkpointlist
            if checkpointlist[-1] == 8:   #same here- query1 maybe?
                response = query1(statement)
                checkpointlist.append(-4)
                return response, checkpointlist
            if checkpointlist[-1] == 9:
                checkpointlist.append(-5)
                return response, checkpointlist
        else:
            response, checkpointlist = long_enpough(checkpointlist)
            return response, checkpointlist

    if checkpointlist[-1] < 0:
        response, checkpointlist = long_enpough(checkpointlist)
        return response, checkpointlist

    if checkpointlist[-1] == 4:
        value_1 = values[-1]
        if 10 in checkpointlist:

            response = "What advise would you give a friend who also values " + value_1 + " how to be more physically active?"
        else:
            response = "Imagine now your friend who has the same value (" +value_1 + ") is also not very physically active but would like to do more sports and is asking you for advice. She gives the same reason for not being physically active you just gave - how would you counter her argument without compromising her values? For example \"I don\'t go to the gym because it\'s expensive\" could be countered with \"You don\'t need to spend money to do sports - you could go running in the park for free\" "
        checkpointlist.append(5)
        return response, checkpointlist

    if checkpointlist[-1] == 7:
        value_1 = values[-1]
        value_2 = values[-2]
        if value_1 == value_2:
            response = "Ok fair enough... but What advise would you give a friend who has the same value (" + value_1 + ") how to be more physically active in this situation without compromising her values?"

        else:
            response = "Ok fair enough... but what advise would you give a friend who has the same values (" + value_1 + " and " + value_2 + ") how to be more physically active in this situation without compromising her values?"
        checkpointlist.append(8)
        return response, checkpointlist

    if checkpointlist[-1] == 10:
        response = "ok lets stop for now. do you think your values are compatible with doing more exercise at all?"
        checkpointlist.extend([11,88])
        return response, checkpointlist

    if checkpointlist[-1] == 11:
        if statement == "yes":
            response = "how? please tell me how you could change your behaviour to exercise more but without compromising your values "
            checkpointlist.append(12)
        elif statement == "no":
            response = "why not? what is hindering you in changing your behaviour to exercise more without compromising your values?"
            checkpointlist.append(12)
        else:
            response = "sorry I didnt get that, please select yes or no"
            checkpointlist.append(88)
        return response, checkpointlist



    if checkpointlist[-1] == 12:
        #print "VALUES"
        #print values

        value_1 = values[-1]
        value_2 = values[-2]
        value_3 = values[-3]
        value_set = set([value_1, value_2, value_3])
        value_str = ', '.join(value_set)
        response = "could you sort the following values by importance to you: " + value_str + " and health. Start with the most important. Type them all in one message"
        checkpointlist.append(13)
        return response, checkpointlist

    if checkpointlist[-1] == 13:
        response = "great, thank you! do you have another major reason for not doing sports regularly? (if your time is running out - select no) "
        checkpointlist.extend([14,88])
        return response, checkpointlist


    if checkpointlist[-1] == 14:
            #checking if user wants to proceed or finish conversation
        if statement == "yes":
            response = "awesome, what is it?"
            checkpointlist.append(3) #start from beginning
        elif statement == "no":
            response = "Ok, thank you very much for your time :) \n if you found me through prolific, please click here: https://www.prolific.ac/submissions/complete?cc=JQXWIXG2 and just in case please also post your prolific ID here so I can make sure you get paid"
            checkpointlist.append(15) #finishes conversation
        else:
            response = "sorry, I didnt get that, please say yes or no"
            checkpointlist.append(88)
        return response, checkpointlist

    if checkpointlist[-1] == 15:
        response = "thanks! good bye :)"
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
        responses = ['can you expand that please :) how does this hinder you doing exercise?',
                    'that\'s not enough, elaborate please - how does this hinder you doing exercise',
                    'please tell me more... why is this preventing you from doing exercise?', 'expand please... how does this hinder you doing exercise',
                    'please expand :) why is this a reason you can\'t do more exercise?']
        resp = random.choice(responses)
        response = statement + quest + resp
        return response


    j = dict((i, statement.count(i)) for i in time)
    time_nr = sum(j.values())

    if time_nr > 0:
        responses = ['I understand you have no time, but can you expand on that please. Why not?',
                    'You say you have no time for sports, right? But why not?',
                    'But why don\'t you have time? What are you busy with?']
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

    k = dict((i, statement.count(i)) for i in neg)
    neg_nr = sum(k.values())

    if neg_nr > 0:
        responses = ['Why not?',
                    'Tell me a bit more. Why not?']
        response = random.choice(responses)
        return response

    d = dict((i, statement.count(i)) for i in expl)
    expl_nr = sum(d.values())

    if expl_nr > 0:
        #print "i should be here"
        responses = ['Okay, but what makes you say that?',
                    'Could you go into more detail? Why do you say that?',
                    'Fair enough. But what makes you say that?',
                    'Elaborate please. Why do you say that? ',
                    'A bit more detail please. What makes you say that?']
        response = random.choice(responses)
        return response




    if statement_length <= 5:
        responses = ['a bit more detail please! Why?',
                    'Why?', 'Okay, but why?',
                    'Why? Tell me :)']
        response = random.choice(responses)
        return response

    if statement_length > 5:
        responses = ['can you expand that please :) why is this a reason you can\'t do more exercise?',
                    'elaborate please...how does this hinder you doing more exercise?',
                    'please tell me more... how does this hinder you doing more exercise?',
                    'expand please...why is this a reason you can\'t do more exercise', 'please expand :) why is this a reason you can\'t do more exercise']
        response = random.choice(responses)
        return response

def query(statement):  #statement = userinput

    quest = "? "
    statement = statement.lower()

    word_tok = statement.split()
    statement_length = len(word_tok)
    if statement_length == 1:
        responses = ['can you expand that please :) how does this hinder you doing exercise?',
                    'that\'s not enough, elaborate please - how does this hinder you doing exercise',
                    'please tell me more... why is this preventing you from doing exercise?', 'expand please... how does this hinder you doing exercise',
                    'please expand :) why is this a reason you can\'t do more exercise?']
        resp = random.choice(responses)
        response = statement + quest + resp
        return response


    k = dict((i, statement.count(i)) for i in neg)
    neg_nr = sum(k.values())

    if neg_nr > 0:
        responses = ['Why not?',
                    'Tell me a bit more. Why not?']
        response = random.choice(responses)
        return response

    d = dict((i, statement.count(i)) for i in expl)
    expl_nr = sum(d.values())

    if expl_nr > 0:
        #print "i should be here"
        responses = ['Okay, but what makes you say that?',
                    'Could you go into more detail? Why do you say that?',
                    'Fair enough. But what makes you say that?',
                    'Elaborate please. Why do you say that? ',
                    'A bit more detail please. What makes you say that?']
        response = random.choice(responses)
        return response




    if statement_length <= 5:
        responses = ['a bit more detail please! Why?',
                    'Why?', 'Okay, but why?',
                    'Why? Tell me :)']
        response = random.choice(responses)
        return response

    if statement_length > 5:
        responses = ['can you expand that please :) why is this a reason you can\'t do more exercise?',
                    'elaborate please...how does this hinder you doing more exercise?',
                    'please tell me more... how does this hinder you doing more exercise?',
                    'expand please...why is this a reason you can\'t do more exercise', 'please expand :) why is this a reason you can\'t do more exercise']
        response = random.choice(responses)
        return response
