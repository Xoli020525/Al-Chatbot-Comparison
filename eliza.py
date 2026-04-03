import re
import random

rules = [
    (r'hello|hi|hey', [
        "Hello! How are you today?",
        "Hi there! What’s on your mind?",
        "Hello, how can I help you?"
    ]),
    
    (r'my name is (.*)', [
        "Nice to meet you, %1.",
        "Hello %1, how are you feeling today?",
        "Why do you tell me your name is %1?"
    ]),
    
    (r'i feel (.*)', [
        "Why do you feel %1?",
        "Do you often feel %1?",
        "What makes you feel %1?"
    ]),
    
    (r'i am (.*)', [
        "How long have you been %1?",
        "Why are you %1?",
        "How does being %1 affect you?"
    ]),
    
    (r'because (.*)', [
        "Is that the real reason?",
        "Are there any other reasons?",
        "Does that explain everything?"
    ]),
    
    (r'my mother (.*)', [
        "Tell me more about your mother.",
        "How does your mother influence you?",
        "Does your mother often %1?"
    ]),
    
    (r'i need (.*)', [
        "Why do you need %1?",
        "Would it really help you to get %1?",
        "What would happen if you didn’t get %1?"
    ]),
    
    (r'quit', [
        "Goodbye! Take care."
    ]),
    
    (r'(.*)', [
        "Please tell me more.",
        "That’s interesting. Go on.",
        "Can you explain that further?",
        "How does that make you feel?"
    ])
]

def respond(user_input):
    user_input = user_input.lower()
    
    for pattern, responses in rules:
        match = re.fullmatch(pattern, user_input)
        if match:
            response = random.choice(responses)
            for i in range(1, len(match.groups()) + 1):
                response = response.replace(f"%{i}", match.group(i))
            return response

def get_eliza_response(user_input: str) -> str:
    return respond(user_input)


def chat():
    print("ELIZA: Hello! Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You: ")
        reply = respond(user_input)
        print("ELIZA:", reply)
        
        if user_input.lower() == "quit":
            break

if __name__ == "__main__":
    chat()