def count_messages(messages):
    message_counts = {}
    for message in messages:
        username, text = message.split(": ", 1)
        if username in message_counts:
            message_counts[username] += 1
        else:
            message_counts[username] = 1
            
    for user, count in message_counts.items():
        print(f"{user}: {count} messages")

messages = [
    "alice: Hi, how are you?",
    "bob: I'm good, thanks!",
    "alice: Glad to hear that.",
    "carol: Hey everyone!",
    "bob: Hi Carol!"
]

count_messages(messages)
