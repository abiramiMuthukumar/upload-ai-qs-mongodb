from openai import OpenAI
from pymongo import MongoClient
import json
import certifi

OPENAI_API_KEY=''
DB_CONNECTION_STRING=''

openAIClient = OpenAI(api_key=OPENAI_API_KEY)

dbClient = MongoClient(DB_CONNECTION_STRING, tlsCAFile=certifi.where())
database = dbClient["qVaultDatabase"]

# create questions using your GPT 4 model/assistant
# use this prompt in the assistant playground:
#   Please produce 3 single best answer question based on the following content: {and here copy in your PDF content}

# an example of a list of 3qs you should create in the right format:
to_upload = """{
        "questionStack": [
                {
                        "id": 1,
                        "questionStem": "Which type of lipid is an ester of three fatty acids and glycerol and is primarily stored in adipose tissue?",
                        "questionLeadIn": "",
                        "options": ["Cholesterol", "Glycolipids", "Phospholipids", "Triacylglycerols", "Sphingomyelin"],
                        "optionsPercentage": [0, 0, 0, 100, 0],
                        "correctAnswer": "Triacylglycerols",
                        "explanation": "Triacylglycerols are esters of three fatty acids and glycerol, primarily stored in adipose tissue, serving as an energy store."
                },
                {
                        "id": 2,
                        "questionStem": "Which fatty acids have more than one double bond, such as linoleic acid, and introduce a kink into the chain reducing their ability to pack together?",
                        "questionLeadIn": "",
                        "options": ["Saturated fatty acids", "Myristic acid", "Oleic acid", "Polyunsaturated fatty acids", "Arachidonic acid"],
                        "optionsPercentage": [0, 0, 0, 100, 0],
                        "correctAnswer": "Polyunsaturated fatty acids",
                        "explanation": "Polyunsaturated fatty acids like linoleic acid have more than one double bond, introducing a kink into the chain, reducing their ability to pack together."
                }]}"""


reply_in_json = json.loads(to_upload)

reply_in_json['creator'] = "King's College London"
reply_in_json['education'] = 'Undergrad'
reply_in_json['topic'] = 'All topics'

collection = database["AI_Question_Output_2"]

collection.insert_one(reply_in_json)