def send_messages(messages, sent_messages):
    while messages:
        message_to_sent = messages.pop()
        print(f'Message to be sent: {message_to_sent}')
        sent_messages.append(message_to_sent)


def show_message(sent_messages):
    for message in sent_messages:
        print(message)


messages = ['hi', 'ok', 'wow']
sent_messages = []

send_messages(messages, sent_messages)
show_message(sent_messages)
