from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import tkinter as tk
from tkinter import scrolledtext

''' Create GUI for the Ai Chatbot '''

# Create main tkinter window
root = tk.Tk() # makes an instance of tk as the root window
root.title("Ai Chabot using Ollama (llama3)")

# Set the window size
root.geometry("500x500")

# Create the input frame
inp_frame = tk.Frame(root) # Frame the root window for the input
inp_frame.pack(padx=10, pady=10) # make space around the frame to improve readability

# Input box for user
message = tk.Entry(inp_frame, width = 50) # form the message box in the input frame
message.grid(row = 0, column = 0, padx = 5) #set the message box at the bottom of the screen with some padding

# Format the chat window to allow for scrolling
chat_window = scrolledtext.ScrolledText(
    root, 
    wrap=tk.WORD, 
    width=50, 
    height=20, 
    state="normal",
    font = ("Times New Roman", 12) # Create the text and its dimensions
)

chat_window.pack(padx=10, pady=10)
chat_window.insert(tk.END, "Llama3: Hello! How can I help you today?\n\n")  # Initial bot message

''' Create Ai functionality and sending messages'''

# Define the langchain chatbot template and chain it
template = """
Answer the question below

Here is the conversation history: {context}

Question: {question}

Answer"""

model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

context = "" # Create context varibale to be updated

# function to go through the conversation and generate a response
def handle_conversation(inp):
    global context  # Create global context so python knows we are editing the intended context
    result = chain.invoke({"context":context, "question": inp})
    context += f"\nUser: {inp}\nAI: {result}"
    return result

def send_message():
    inp = message.get() # take the inputed message from the window
    if inp.strip():     # respond to any input, remove any unecessary spaces
        # Display user input in the window
        chat_window.insert(tk.END, f"You: {inp}\n\n") # Insert everything into the window
        message.delete(0,tk.END) # Ensures the whole input is erased

        # Get the chatbot's response and display it
        response = handle_conversation(inp) # Runs the handel conversation function
        chat_window.insert(tk.END, f"Llama3: {response}\n\n") # Insert the whole response

        # Scroll to the bottom of the chat window
        chat_window.see(tk.END)


''' Sending functionality '''
# Make send button
send = tk.Button(inp_frame, text = "->", command = send_message)
send.grid(row=0, column=1, padx=5)

# Start the Tkinter event loop
root.mainloop()
