from google import genai
from google.genai import types
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
client=genai.Client()
history=[]

# Printing The Chatbot's Name
print("\t\t\t--------------------")
print("\t\t\t| FAIQ ALI CHATBOT |")
print("\t\t\t--------------------")

# Info about user and the chat
user_name=input("What's Your Name:\n")
print(f"Hi, {user_name} how can I help you\n")
chat_name=input("""Give a suitable name to your chat\n \t \t OR \n 
else open up your previous chat by writing the exact file's name for context\n:""").strip()

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
        print("Type Quit to leave\n")

        user_input = str(input("Ask Me!\n\t\t"))

        if user_input.lower() == "quit":

            break

        else:    

            print(f"Thinking\n{user_name} is asking me for this:{user_input}")

            response = chat.send_message(f"User's Question: {user_input}, History: {history}" )

            current_history.append(f"{user_name}:{user_input}")

            history.append(f"{user_name}:{user_input}")

            print(f"\n {response.text}")

            current_history.append(f"AI:{response.text}")

            history.append(f"AI:{response.text}")

    except Exception as e :

        print(e) 
        

with open (f"{chat_name}","a") as file:

    for i in (current_history):

        file.write(f"\n{i}\n")

   





