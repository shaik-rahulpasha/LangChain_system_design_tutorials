import warnings
warnings.filterwarnings("ignore")
import os 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.tools import tool
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


########################--------------------Tool callings -----------------------------######################################


"""
@tool
def get_weather(location: str) -> str : 
    this function return the current weather of location
    Arguments : 
        1. Takes str as input for location
    
    return "its sunny in {location}"

@tool 
def description_about_city(Location: str)-> str: 
     This function descipts the city nature and details and tourist places and food items.
     Args: 
          1. Takes location as input 
     
    return f"city {Location} has beautiful raw natured ness "


model_with_tools=model.bind_tools([get_weather, description_about_city])

model_with_tools=model.bind_tools([get_weather, description_about_city],tool_choice="any")

response=model_with_tools.invoke("get description nature in Pune")

for tool_call in response.tool_calls:
    print(f"Tool : {tool_call['name']}")
    print(f"tool args ; {tool_call['args']}")

    

    for chunk in model_with_tools.stream(
    "What's the weather in Boston and Tokyo?"
):
    # Tool call chunks arrive progressively
    for tool_chunk in chunk.tool_call_chunks:
        if name := tool_chunk.get("name"):
            print(f"Tool: {name}")
        if id_ := tool_chunk.get("id"):
            print(f"ID: {id_}")
        if args := tool_chunk.get("args"):
            print(f"Args: {args}")

# Output:
# Tool: get_weather
# ID: call_SvMlU1TVIZugrFLckFE2ceRE
# Args: {"lo
# Args: catio
# Args: n": "B
# Args: osto
# Args: n"}
# Tool: get_weather
# ID: call_QMZdy6qInx13oWKE7KhuhOLR
# Args: {"lo
# Args: catio
# Args: n": "T
# Args: okyo
# Args: "}

"""
