from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=api_key,
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
    "Answer the following question clearly: {question}"
)

chain = prompt | model

question = input("Enter your question: ")

response = chain.invoke({
    "question": question
})

print(response.content)