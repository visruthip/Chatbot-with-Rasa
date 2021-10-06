# Resturant-Search-Chatbot-With-RASA

## Intoduction
A chatbot is a robot with an Artificial Intelligence (AI) which can have a conversation with a human interlocutor. It can be used in many different situations and have various roles like answering customer queries, automating repetitive tasks, and more. A chatbot can also handle queries pertaining to a particular domain or type of task. For example, a ‘weather bot’ can only predict weather. It cannot book a table at a restaurant or set up an alarm. Similarly, a restaurant discovery bot can only help you find restaurants in several cities; it might not be able to answer general questions such as "Who is the prime minister of India?".

With the advancements in machine learning (ML), deep learning (DL) and natural language processing (NLP), traditional conversational chatbots have now become advanced and are called as contextual chatbots. A contextual chatbot understands the context of the conversation by observing the pattern of communication between itself and the user. It not only keeps track of the current state of the conversation, but also of what has been said before. These advanced chatbots remember what a user asked or said previously, and deliver a more relevant answer according to that information.

Instead of relying on a bunch of if/else statements, a contextual chatbot uses an ML model trained on example conversations to decide what to do next.
Conversational system has primarily two components:
1. Natural Language Understanding, or NLU
2. Dialogue Management System
which carries out the overall conversation

The first layer of a conversational system, Natural Language Understanding (NLU), interprets the free text provided by the user. It basically takes an unstructured text phrase or sentence, understands what the user probably intends to say, extracts entities from the text phrase or sentence, and converts it into structured data.

Rasa NLU and Rasa Core (APIs) are two open-source libraries for building conversational agents. Rasa NLU is the tool used for intent classification and entity extraction.

_________________________________________________________________________________________________________________________________________________


## Problem Statement:

An Indian startup named 'Foodie'(Name is just for reference) wants to build a conversational bot (chatbot) which can help users discover restaurants across several Indian cities.

The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience. The project brief provided to you is as follows.


### Inputs:

1. Foodie works only in Tier-1 and Tier-2 cities,while for tier-3 cities, it should reply back with something like "We do not operate in that area yet".The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience.

2. Cuisine Preference: Take the cuisine preference from the customer. The bot should list out the following six cuisine categories (Chinese, Mexican, Italian, American, South Indian & North Indian) and the customer can select any one out of that.

3. Average budget for two people: Segment the price range (average budget for two people) into three price categories: lesser than 300, 300 to 700 and more than 700. 

Finally, the bot should ask the user whether he/she wants the details of the top 10 restaurants on email. If the user replies 'yes', the bot should ask for user’s email id and then send it over email with the list of top 5 restaurants in a sorted order (descending) of the average Zomato user rating (on a scale of 1-5, 5 being the highest). Else, just reply with a 'goodbye' message. 


## Goals of this Project
For chatbot ‘Foodie’:
1. NLU training: used rasa train to create more training examples for entities and intents.
2. Build actions for the bot: Actions to extract the features such as the average price for two people and restaurant’s user rating, Also for sending emails from Python.
3. Creating more stories: Rasa Core’s dialogue management system. Rasa Core uses a variant of Recurrent Neural Networks (RNNs), which are 'sequence models', called LSTMs (Long Short-Term Memory), to learn dialogue flow.


## The bot will function as follows:

    User:  hi
    Bot: hey there! How may i help you
    User:  Can you fine me a restaurant
    Bot:In what location?
    Your input ->  Hyderabad
    Bot:? what kind of cuisine would you like? (Use arrow keys)
    » 1: Chinese (Chinese)
     2: Mexican (Mexican)
     3: Italian (Italian)
     4: American (American)
     5: South Indian (South Indian)
     6: North Indian (North Indian)
     Type out your own message...
    User: 1: Chinese (Chinese)
    Bot: ? What price range are you looking at? (Use arrow keys)
    » 1: Lesser than Rs. 300 (Less than 300)
     2: Rs. 300 to 700 (300 to 700)
     3: More than 700 (More than 700)
     Type out your own message...
    User:  1: Lesser than Rs. 300 (Less than 300)
    Bot:-----Found The Great Indian Food Truck in Hari Nagar, Jail Road, New Delhi has been rated 3.0
    Bot:? Do you want me to send the top 10 restaurants names to your email id? (Use arrow keys)
    » 1: yes (yes)
     2: no (no)
     Type out your own message...
    User:  1: yes (yes)
    Bot:Please provide your email-id(mention only email-id)
    User: Your input ->  testmail.nlp2021@gmail.com
    Bot:Bye-bye

## Prerequisites
Download and install anaconda: https://docs.anaconda.com/anaconda/install/ <br />
RASA tutorial : https://rasa.com/docs/rasa/installation/<br />
Rasa Training data: https://rasa.com/docs/rasa/nlu-training-data

### Versions used for this Chatbot project(more version information details are listed at bottom of this file)
rasa==2.8.0<br />
spacy==3.1.0

## To run the files:
open anaconda prompt and activate rasa
The rasa init command creates all the files that a Rasa project needs and trains a simple bot on some sample data.

![image](https://user-images.githubusercontent.com/79132138/136177460-71060838-33ab-415d-bd00-a38d39670c90.png)

After completing the goals of the project, refer below commands:

- rasa train nlu # to train data in data/nlu.md file.
- rasa shell nlu # to test nlu data.
Check the confidence
- rasa train core  # to train the rasa core model.
- rasa run actions #To fetch results from zomato api, we run actions.
- rasa shell  # for testing few cases for rasa core model.
- rasa interactive. #Create stories in interactive mode and export them, which will be available in data/stories.md (or) we can manually add stories.



## Output folder

### Image shows the bot result, the communication b/w user and bot
![1 Bot result2](https://user-images.githubusercontent.com/79132138/136154760-888fb507-4d08-48b7-9884-415c8003df39.JPG)


### Image shows the top rated restaurants email, with the Location, budget and cusine selected by user
![2 mail](https://user-images.githubusercontent.com/79132138/136154777-18ea5291-e468-47d7-86d5-c14c17fd8674.JPG)

<br />
<br />
<br />
<br />



_________________________________________________________________________________________________________________________________________________
## Versions used for Chatbot project(for reference only)


absl-py==0.13.0
aio-pika==6.8.0
aiofiles==0.7.0
aiohttp==3.7.4
aiormq==3.3.1
APScheduler==3.7.0
astunparse==1.6.3
async-generator==1.10
async-timeout==3.0.1
attrs==21.2.0
backcall==0.2.0
bidict==0.21.2
blis==0.7.4
boto3==1.18.1
botocore==1.21.1
cachetools==4.2.2
catalogue==2.0.4
certifi==2021.5.30
cffi==1.14.6
chardet==3.0.4
click==7.1.2
cloudpickle==1.6.0
colorama==0.4.4
colorclass==2.2.0
coloredlogs==15.0.1
colorhash==1.0.3
cryptography==3.4.7
cycler==0.10.0
cymem==2.0.5
debugpy==1.3.0
decorator==4.4.2
dm-tree==0.1.6
dnspython==1.16.0
docopt==0.6.2
en-core-web-md @ https://github.com/explosion/spacy-models/releases/download/en_core_web_md-3.1.0/en_core_web_md-3.1.0-py3-none-any.whl
fbmessenger==6.0.0
future==0.18.2
gast==0.3.3
google-auth==1.33.0
google-auth-oauthlib==0.4.4
google-pasta==0.2.0
greenlet==1.1.0
grpcio==1.38.1
h11==0.9.0
h5py==2.10.0
httpcore==0.11.1
httplib2==0.19.1
httptools==0.2.0
httpx==0.15.4
humanfriendly==9.2
idna==2.10
importlib-metadata==3.10.1
ipykernel==6.0.2
ipython==7.25.0
ipython-genutils==0.2.0
jedi==0.18.0
Jinja2==3.0.1
jmespath==0.10.0
joblib==1.0.1
jsonpickle==2.0.0
jsonschema==3.2.0
jupyter-client==6.1.12
jupyter-core==4.7.1
kafka-python==2.0.2
Keras-Preprocessing==1.1.2
kiwisolver==1.3.1
Markdown==3.3.4
MarkupSafe==2.0.1
matplotlib==3.3.4
matplotlib-inline==0.1.2
mattermostwrapper==2.2
multidict==5.1.0
murmurhash==1.0.5
networkx==2.5.1
numpy==1.18.5
oauth2client==4.1.3
oauthlib==3.1.1
opt-einsum==3.3.0
packaging==20.9
pamqp==2.3.0
pandas==1.3.0
parso==0.8.2
pathy==0.6.0
pickleshare==0.7.5
Pillow==8.3.1
preshed==3.0.5
prompt-toolkit==2.0.10
protobuf==3.17.3
psycopg2-binary==2.9.1
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.20
pydantic==1.8.2
pydot==1.4.2
Pygments==2.9.0
PyJWT==2.1.0
pykwalify==1.8.0
pymongo==3.10.1
pyparsing==2.4.7
pyreadline==2.1
pyrsistent==0.18.0
pyTelegramBotAPI==3.8.1
python-crfsuite==0.9.7
python-dateutil==2.8.2
python-engineio==4.2.0
python-socketio==5.3.0
pytz==2021.1
pywin32==301
pyzmq==22.1.0
questionary==1.9.0
rasa==2.8.0
rasa-sdk==2.8.0
redis==3.5.3
regex==2021.7.6
requests==2.25.1
requests-oauthlib==1.3.0
requests-toolbelt==0.9.1
rfc3986==1.5.0
rocketchat-API==1.16.0
rsa==4.7.2
ruamel.yaml==0.16.13
ruamel.yaml.clib==0.2.6
s3transfer==0.5.0
sanic==20.12.3
Sanic-Cors==0.10.0.post3
sanic-jwt==1.5.0
Sanic-Plugins-Framework==0.9.5
scikit-learn==0.24.2
scipy==1.7.0
sentry-sdk==1.2.0
six==1.16.0
sklearn-crfsuite==0.3.6
slackclient==2.9.3
smart-open==5.1.0
sniffio==1.2.0
spacy==3.1.0
spacy-legacy==3.0.8
SQLAlchemy==1.4.21
srsly==2.4.1
tabulate==0.8.9
tensorboard==2.5.0
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.0
tensorflow==2.3.3
tensorflow-addons==0.13.0
tensorflow-estimator==2.3.0
tensorflow-hub==0.12.0
tensorflow-probability==0.13.0
termcolor==1.1.0
terminaltables==3.1.0
thinc==8.0.7
threadpoolctl==2.2.0
tornado==6.1
tqdm==4.61.2
traitlets==5.0.5
twilio==6.50.1
typeguard==2.12.1
typer==0.3.2
typing-extensions==3.10.0.0
tzlocal==2.1
ujson==4.0.2
urllib3==1.26.6
wasabi==0.8.2
wcwidth==0.2.5
webexteamssdk==1.6
websockets==8.1
Werkzeug==2.0.1
wincertstore==0.2
wrapt==1.12.1
yarl==1.6.3
zipp==3.5.0
<br />
<br />
<br />
<br />

Now we can deploy the chatbot through Slack or any other channel.

## Thank you for reaching out to me on Github😃

