user_input = input("Enter 6-string guitar tuning, low to high: ")
default_tuning = ['E', 'A', 'D', 'G', 'B', 'E']
SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#']

user_tuning = user_input.split(' ')

print(user_tuning)

# convert all the notes in the user tuning to their indexes in the SCALE const
for user_note in user_tuning:
    for note in SCALE:
        if user_note == note:
            user_tuning[user_tuning.index(user_note)] = SCALE.index(note)



