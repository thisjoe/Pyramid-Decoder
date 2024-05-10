def decode(message_file):
    # Input file
    with open(message_file, "r") as file:
        lines = file.readlines()

    hidden_message = []

    # Create pyramid with cataloged words from .txt file
    for line in lines:
        number, word = line.strip().split()
        hidden_message.append(word)

    # Decoding the message
    decoded_message = ''
    word_index = 0
    for i in range(1, len(hidden_message) + 1):
        if word_index < len(hidden_message):
            decoded_message += hidden_message[word_index] + ' '
            word_index += i

    return decoded_message.strip()

decoded = decode('coding_qual_input.txt')
print(decoded)