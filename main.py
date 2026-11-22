from google import genai
from google.genai import types
from dotenv import load_dotenv
from pathlib import Path
import pyfiglet
from colorama import Fore, Style, init

load_dotenv()

client=genai.Client()

# History For The Chat Along With The Context
history=[]

print("\n\n\n")

# For Pyfiglet 
init(autoreset=True)

banner = pyfiglet.figlet_format("FAIQ ALI CHATBOT", font="ansi_shadow")
print(Fore.CYAN + banner)

print(Style.BRIGHT + "                 A Chatbot With History")

print(Style.DIM + "A command-line chatbot built with Google's Gemini API.")
print(Style.DIM + "Start a new chat or load an existing .txt file as context,")
print(Style.DIM + "and automatically save the session when you exit.\n")

# Info about user and the chat
user_name=input("\nWhat's Your Name:\n\n")
print(f"\n\nHi, {user_name} how can I help you\n")
chat_name=input("""\nGive a suitable name to your chat\n\n \t \t OR \n 
Else open up your previous chat by writing the exact file's name for context:\n\n""").strip()

# Define system prompt configuration
system_prompt = (
    """You are a polite teacher responding to the user politely, answering in a way 
      that a 10-year-old can understand. Answer clearly, concisely, and to the point 
       without any fluff in just three lines."""
)

# Context variable
context=[]

# Initialize chat ONCE outside the loop to keep context
chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(system_instruction=system_prompt)
)

# Checking if the user is inserting the file name 
if not chat_name.endswith(".txt"):

    chat_name = Path(f"{chat_name}.txt")

    if chat_name.is_file():

        with open(f"{chat_name}","r") as existed_file:

            reading=existed_file.readlines()

            context.append(reading)
            
    else:

        with open(f"{chat_name}","a") as file:

            pass       

else:

    chat_name = Path(f"{chat_name}")

    if chat_name.is_file():

        with open(f"{chat_name}","r") as existed_file:

            reading=existed_file.readlines()

            context.append(reading)
            
    else:

        with open(f"{chat_name}","a") as file:

            pass 

# History Variable      
history=[]

# Checking if context is not none
if not context:

    pass

else:

    response=chat.send_message(f"This is the Chat Context {context}") 

    history.append(context)

# Current History
current_history = []

while True:

    try:

        # Asking for the user's input
        print("\nType Quit to leave\n")

        user_input = str(input(f"Ask Me {user_name}!\n\n\t"))

        if user_input.lower() == "quit":

            break

        else:    

            print(f"Thinking...\n[{user_name}] is asking me for this: {user_input}")

            response = chat.send_message(f"User's Question: {user_input}, History: {history}" )

            current_history.append(f"{user_name}:{user_input}")

            history.append(f"{user_name}:{user_input}")

            print(f"\n[AI]:{response.text}")

            current_history.append(f"AI:{response.text}")

            history.append(f"AI:{response.text}")

    except Exception as e :

        print(e) 
        

with open (f"{chat_name}","a") as file:

    for i in (current_history):

        file.write(f"\n{i}\n")

   





