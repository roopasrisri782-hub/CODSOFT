import re
from datetime import datetime

class RuleBasedChatbot:
    def __init__(self):
        self.name = "SmartBot"

    def get_response(self, user_input):
        text = user_input.lower().strip()

        if re.search(r"\b(hi|hello|hey|hai)\b", text):
            return "Hello! How can I assist you today?"

        elif re.search(r"\b(how are you|how are u)\b", text):
            return "I am doing great. Thank you for asking!"

        elif re.search(r"\b(your name|who are you)\b", text):
            return f"My name is {self.name}. I am a rule-based chatbot."

        elif re.search(r"\b(time|current time)\b", text):
            return f"Current time: {datetime.now().strftime('%H:%M:%S')}"

        elif re.search(r"\b(date|today's date|today date)\b", text):
            return f"Today's date: {datetime.now().strftime('%d-%m-%Y')}"

        elif re.search(r"\b(help|commands)\b", text):
            return (
                "Available commands:\n"
                "- Hello\n"
                "- How are you\n"
                "- Your name\n"
                "- Time\n"
                "- Date\n"
                "- Bye"
            )

        elif re.search(r"\b(thank you|thanks)\b", text):
            return "You're welcome! Happy to help."

        elif re.search(r"\b(bye|exit|quit)\b", text):
            return "Goodbye! Have a wonderful day."

        else:
            return (
                "Sorry, I do not understand that query.\n"
                "Type 'help' to see available commands."
            )

def main():
    chatbot = RuleBasedChatbot()

    print("=" * 50)
    print("      RULE-BASED CHATBOT SYSTEM")
    print("=" * 50)
    print("Type 'help' for commands")
    print("Type 'bye' to exit")
    print("-" * 50)

    while True:
        user_input = input("You: ")

        response = chatbot.get_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break

if __name__ == "__main__":
    main()
