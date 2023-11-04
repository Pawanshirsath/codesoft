import random
import tkinter as tk

# Define a dictionary of rules and responses
rules = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thanks!", "I'm just a bot, but I'm here to help!"],
    "what's your name": ["I'm a chatbot.", "I don't have a name, but you can call me ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Have a great day!"],
}

# Function to generate a response
def get_response(user_input):
    user_input = user_input.lower()
    
    for key in rules:
        if key in user_input:
            return random.choice(rules[key])
    
    return "I'm sorry, I don't understand that."

# Function to handle user input
def send_message():
    user_input = user_entry.get()
    user_entry.delete(0, tk.END)
    response = get_response(user_input)
    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, "You: " + user_input + "\n")
    chat_history.insert(tk.END, "ChatBot: " + response + "\n\n")
    chat_history.config(state=tk.DISABLED)

# Create the GUI
root = tk.Tk()
root.title("Rule-Based Chatbot")

# Chat history display
chat_history = tk.Text(root, height=10, width=40, state=tk.DISABLED)
chat_history.pack()

# User input entry
user_entry = tk.Entry(root, width=40)
user_entry.pack()

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()
