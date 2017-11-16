from flask import Flask, request
import requests

from no_value_chatbot import *
from quick_replies import *

app = Flask(__name__)

#access token of ArgHealthBot Application in Facebook
ACCESS_TOKEN = "EAACJjQRK0ucBAOciSfRmcOafWc448ZBtZCa3XDcZAPahtpPPGBvQztZChuv1kzc9ZC9GjukmVMh7JUiprv3Bo9lEHlgzZB5mDZBp1JrLZBPVlBSy5Hx4crJQ8IqxrSJAr9OxfsaKf83ZAHDTF7J35j7yKgbL0IiRYYaA5Q2EK0zmE4wZDZD"
# set of unique user id's
user_ids =  set()

#stored by key_id of user
chatlogs = {} #relevant answers form user
checkpointlists = {} #checkpoints to guide conversation a certain way

# dont change following code:
@app.route('/', methods=['GET'])
def handle_verification():
    return request.args['hub.challenge']

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)

def quick_reply_yesno(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {
        "text": msg,
        "quick_replies": yes_no
    }
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)


def quick_reply_smtnever(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {
        "text": msg,
        "quick_replies": smt_never
    }
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)

##########################################################################

@app.route('/', methods=['POST'])
def handle_incoming_messages():
    print chatlogs
    data = request.json

    try:
        sender = data['entry'][0]['messaging'][0]['sender']['id']  #unicode, should i typecast it into string or int? lets see...
        message = data['entry'][0]['messaging'][0]['message']['text']

    except KeyError:
        #should never get here
        sender = 'defaultsender'
        message = 'defaultmessage'


    print checkpointlists
    #converting message to string for easier NLP analysis later
    message = message.lower().encode('utf-8')
    #sender as string just in case
    key_id = str(sender)

    #if the sender is not found in userIds set, create key in dictionary and add message to log (value)
    if key_id not in user_ids:
        chatlogs[key_id] = [message]
        checkpointlists[key_id] = ["blubb"] #instantiating

        bot_reply = "Hey there! Welcome to ArgHealthBot. Thanks for taking part in this study! I am interested in your current exercise routine and want to hear arguments and values that explain your choice as well as counterarguments. Please familiarise yourself with the terms and conditions and instructions of this experiment at: http://www.homepages.ucl.ac.uk/~ucablc3/study.html. If you agree to them, just type anything :)"

        #add user to set
        user_ids.add(key_id)
        reply(sender, bot_reply)
        chatlogs[key_id].append(bot_reply)
        return "ok"
    else:
        #otherwise just append the message to the already existing key in the dictionry
        chatlogs[key_id].append(message)


# *******************************  START CONVERSATION WITH ARGHHEALTHBOT ************************************

    #if code doesnt work delete this if-statement
    if checkpointlists[key_id][0] == 1 or checkpointlists[key_id][0] == 2:

        bot_reply, checkpointlists[key_id] = handle_response(message, checkpointlists[key_id])




        if checkpointlists[key_id][-1] != 88:   #and is not end of thing for yes and no - elif statement needed for yes_no
            reply(sender, bot_reply)
            return "ok"


        else:
            quick_reply_yesno(sender,bot_reply)
            checkpointlists[key_id].remove(88)

            return "ok"



    #user stats chat, chatbots says hello, user agrees - so its length 3
    if len(chatlogs[key_id]) is 3:
        bot_reply = "great, lets get started. How often do you do exercise?  "
        quick_reply_smtnever(sender, bot_reply)
        chatlogs[key_id].append(bot_reply)
        return "ok"

    if len(chatlogs[key_id]) is 5 or checkpointlists[key_id][0] == "fail":

        if message == "sometimes":
            bot_reply = "Okay. What is the main reason why you only sometimes do sports. Please give only one reason for now"
            checkpointlists[key_id] = [1]
            checkpointlists[key_id].append(3)

        elif message == "never":
            bot_reply = "Okay. What is the main reason why you never do sports. Please give only one reason for now"
            checkpointlists[key_id] = [2]
            checkpointlists[key_id].append(3)

        else:
            bot_reply = "sorry I didnt get you, please select sometimes or never"
            checkpointlists[key_id] = ["fail"]
            quick_reply_smtnever(sender, bot_reply)
            return "ok"

        reply(sender, bot_reply)
        chatlogs[key_id].append(bot_reply)
        return "ok"




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5556)
