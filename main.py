with open('./Input/Names/invited_names.txt') as names_file:
    names_list = names_file.read().splitlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter = letter_file.read()

for name in names_list:
    new_letter = letter.replace('[name]', name)
    with open(f'./Output/ReadyToSend/letter_for_{name}', mode='w') as send_file:
        send_file.write(new_letter)