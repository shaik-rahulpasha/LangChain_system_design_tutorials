import warnings
warnings.filterwarnings("ignore")
import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature="0.1", # 0.1 more of determinstic and as number goes it becomes creative
    timeout=30,
    max_tokens=1000,
    max_retries=3)


#other roles are 
#developer framework specific 
#fucntion 
#tool
conversation=[
    
       { "role":"system",   "content":"Your are helpful assistance  translates from english to telugu pronunciation in english language !"},
       { "role":"user",     "content":" How your doing?"},
       { "role":"assistant","content":"Meeru ela unnaru ?"},
       { "role":"user",     "content":"did you have lunch?"}
]

#response=model.invoke("why do parrots talk?")
#response=model.invoke(conversation)


###############------------------streams--------------#######################################

## example 1

"""
for chunk in model.stream("why do parrots talk?"):
    print(chunk.text, end="|",flush=True)

"""
##for real time response will use thsi 



##example 2 
"""
full = None 
for chunk in model.stream("why parrots do talk?"):
    full= chunk if full is None else full+chunk
    print(full.text)
print(full.content_blocks)

"""



#print(response.content)



#########################------------------batching--------------------------------################################### 
"""
responses=model.batch([
    "what is ai engineer",
    "what is quantum computing",
    "how does fish swims"
])
for response in responses:
    print(response.content)
"""


"""
for response in model.batch_as_completed([
    "Why do parrots have colorful feathers?",
    "How do airplanes fly?",
    "What is quantum computing?"
]):
    print(response)
"""

