
import os
import openai
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

print("Testing Basic LangChain Setup...\n")
# Initialize LLM
#os.environ["OPENAI_API_KEY"]="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" # Replace with your actual key

#Naresh Key
os.environ["OPENAI_API_KEY"]="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"

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