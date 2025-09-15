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



# Function to change the background color
def change_background(color):
    root.configure(bg=color)

# Button to change background to light blue
bl_back = tk.Button(inp_frame, 
                    text="", 
                    bg="lightblue", 
                    fg="white", 
                    command=lambda: change_background("lightblue"))  # Use lambda to pass color
bl_back.grid(row=0, column=6, padx=5)

bl_back = tk.Button(inp_frame, 
                    text="", 
                    bg="gold", 
                    fg="white", 
                    command=lambda: change_background("gold"))  # Use lambda to pass color
bl_back.grid(row=1, column=6, padx=5)

bl_back = tk.Button(inp_frame, 
                    text="", 
                    bg="white", 
                    fg= "black", 
                    command=lambda: change_background("white"))  # Use lambda to pass color
bl_back.grid(row=2, column=6, padx=5)

# Reseting the context if the user wants
def reset():
    global context
    context = ""
    chat_window.delete("1.0", tk.END)
    chat_window.insert(tk.END, "Llama3: Chat history has been reset. How can I help you!\n\n")

# Save chat as a file if the user wants
def save():
    with open("chat_history.txt", "w") as file:
        file.write(chat_window.get("1.0", tk.END))
    chat_window.insert(tk.END, "Llama3: Chat History Saved!")




# Reset Button
res_button = tk.Button(inp_frame, text = "Reset History",  bg = "red", command = reset)
res_button.grid(row = 1, column = 0, padx = 5)

# Save Button
save_button = tk.Button(inp_frame, text = "Save History", bg = "light green", command = save)
save_button.grid(row = 1, column = 1, padx = 5)

# Start the Tkinter event loop
root.mainloop()


 




