# Personal Voice Assistant

This is a Python-based voice assistant I built. It uses speech recognition to listen to what I say and a text-to-speech engine to talk back to me. It's designed to be a casual digital buddy that can help with basic tasks and keep a conversation going.

### Cool Features
*   **Time-Aware Greeting:** When it starts up, it actually checks the clock. It'll say "Good morning," "Good afternoon," or "Good evening" depending on when I run it.
*   **Memory:** It asks for my name at the start and remembers it, occasionally using it in conversation to feel more personal.
*   **Context Awareness:** If I tell it to "search for cats" and then later say "open it," it remembers that the search results were the last thing opened and opens them again.
*   **Small Talk & Jokes:** It's not just a robot; it can tell jokes, handle compliments, and respond to basic questions like "how are you" with randomized answers so it doesn't sound repetitive.
*   **Error Handling:** If I don't say anything or the mic doesn't pick me up, it won't crash. It handles those silent moments naturally.

### Supported Commands
- "What time is it?"
- "Open Google" / "Open YouTube" / "Open Chrome"
- "Search for [anything]"
- "Open it" (re-opens the last link)
- "Tell me a joke"
- Small talk: "Who are you?", "How are you?", "Are you real?", "Thank you"
- "Exit", "Stop", or "Bye"

### How to get it running
Just follow these two steps in your terminal:

pip install -r requirements.txt
python assistant.py
