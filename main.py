user_input = input("Enter 6-string guitar tuning, low to high, seperated by spaces: ")
SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

user_tuning = user_input.split(' ')

for user_note in user_tuning:
    for note in SCALE:
        if user_note == note:
            user_tuning[user_tuning.index(user_note)] = SCALE.index(note)

user_tuning = [int(n) for n in user_tuning]

steps = input("Enter number of steps to transpose up or down (negative or positive): ")
steps = int(steps)

for i in range(len(user_tuning)):
    user_tuning[i] = user_tuning[i] + steps
    if user_tuning[i] > 11:
        user_tuning[i] = user_tuning[i] - 11
    if user_tuning[i] < 0:
        user_tuning[i] = user_tuning[i] + 12

for user_note in user_tuning:
    for note in SCALE:
        if user_note == SCALE.index(note):
            user_tuning[user_tuning.index(user_note)] = note

print("New tuning: " + user_tuning[0] + " " + user_tuning[1] + " " + user_tuning[2] + " " + user_tuning[3] + " " + user_tuning[4] + " " + user_tuning[5])