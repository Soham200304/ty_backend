import os
from dotenv import load_dotenv 
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage
load_dotenv()

model = ChatGroq(model="llama3-8b-8192", groq_api_key=os.getenv('GROQ_API_KEY'))
messages = [
    SystemMessage(content="you're an expert in task suggestor where user inputs in text format and you have to detect what is the mood of the user. For example, user prompt: I am feeling motivated and i supper happy; but dont know what to do. According to the user's mood the output should be the list of tasks, reason of that task to be perform, their benefits. Suggest 5 to 7 tasks accordingly.For example, output: 1. Perform Some Exercise Reason: Benefits:"), # System prompt
    HumanMessage(content="I am feeling demotivated and low") # User prompt
]
response = model.invoke(messages)
content = response.content
print(content)