user_tuning = input("Enter 6-string guitar tuning, low to high: ")
default_tuning = {'E', 'A', 'D', 'G', 'B', 'E'}
scale = {'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#'}

for i in len(user_tuning):
    for note in len(scale):
        if user_tuning[i] == scale[note]:
            user_tuning[i] = note

print(user_tuning)

