# Faiq Ali Chatbot

A command-line chatbot built with Google's Gemini API. It can start a new chat or load an existing `.txt` chat file as context, then save the current session to that file when you exit.

## Requirements

- Python 3.9 or later
- A Google Gemini API key

## Setup

1. Open a terminal in this project folder.
2. Install the required packages:

   ```bash
   python -m pip install google-genai python-dotenv
   ```

3. Create a `.env` file in the project folder and add your API key:

   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

   Keep your API key private. Do not commit the `.env` file or share it publicly.

## Run

```bash
python main.py
```

Enter your name, then enter a chat filename. You can type a name such as `faiq` (the program adds `.txt`) or an existing filename such as `faiq.txt`. If that file exists, its contents are sent to Gemini as context.

Type a message to chat. Type `quit` to end the session; the messages from that run are appended to the selected chat file.

## Notes

- Chat files are read from and written to the current working directory.
- The chatbot uses the `gemini-2.5-flash` model.
- The system prompt asks Gemini to respond politely and concisely in three lines.
