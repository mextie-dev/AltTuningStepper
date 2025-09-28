user_input = input("Enter 6-string guitar tuning, low to high: ")
default_tuning = ['E', 'A', 'D', 'G', 'B', 'E']
scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#']

user_tuning = user_input.split(' ')

print(user_tuning)

for i in range(user_tuning):
    for note in range(scale):
        if user_tuning[i] == scale[note]:
            user_tuning[i] = note

print(user_tuning)

