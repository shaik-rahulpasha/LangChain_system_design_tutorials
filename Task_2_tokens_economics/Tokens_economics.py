import warnings 
warnings.filterwarnings("ignore")

import os 
from  langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    max_retries=3,
    api_key=os.getenv("GOOGLE_API_KEY"),
    temperature="0.7",
    timeout=30,
    max_tokens=1000
)
message="how human understands emotions"
print(model.get_num_tokens(message))


"""
1. limit the tokesn as hard way 
2. auto trim the message of older messages 
3. summarize through another model call 
4. output tokens limiting 

"""