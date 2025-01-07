from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below

Here is the conversation history: {context}

Question: {question}

Answer"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI Chatbot! Type 'exit' to quit.")
    while True:
        inp = input("You: ")
        if inp.lower() == "exit":
            break

        result = chain.invoke({"context":context, "question": inp})
        print("Bot:", result)
        context += f"\nUser: {inp}\nAI: {result}"

if __name__ == '__main__':
    handle_conversation()
