import os
import openai
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

print("Testing Basic LangChain Setup...\n")
# Initialize LLM
#os.environ["OPENAI_API_KEY"]="" # Replace with your actual 
os.environ["OPENAI_API_KEY"]=""

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
# Test 1: Simple query
messages = [HumanMessage(content="Say 'Hello from Google Colab! Agentic AI is working!' in a cheerful way.")]
response = llm.invoke(messages)
print(f"Test 1 - LLM Response: {response.content}\n")
# Test 2: Math calculation
messages = [HumanMessage(content="Calculate: What is 25 multiplied by 4, then add 10 to the result?")]
response = llm.invoke(messages)
print(f"Test 2 - Math Response: {response.content}\n")
print("Setup successful!")
