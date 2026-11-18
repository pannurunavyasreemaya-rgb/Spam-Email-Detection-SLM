
import ollama

print("=" * 45)
print("       SPAM DETECTION - OLLAMA CHAT")
print("=" * 45)

print("Type your message or email below.")
print("Type 'exit' to stop.\n")

while True:
    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Chat ended.")
        break

    response = ollama.chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a spam detection assistant. "
                    "Analyze the user's message and explain "
                    "whether it appears to be Ham or Spam. "
                    "Do not claim certainty."
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    print("\nAssistant:", response["message"]["content"])
    print("-" * 45)
