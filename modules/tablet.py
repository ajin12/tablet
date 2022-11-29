from chord import Chord

# TODO: be able to change tuning
tuning = ["E", "A", "D", "G", "B", "e"]
space = "-"
start_delimiter = "["
end_delimiter = "]"

NUM_STRINGS = 6


def play(chord, type):
    chord = Chord(chord)
    chord_method = 'play_' + type
    return getattr(chord, chord_method)()

def print_tab(tab):
    lines = [""] * NUM_STRINGS

    for i, string in enumerate(tuning):
        lines[i] += string + " " + start_delimiter + space + space

    for chord in tab:
        for i, note in enumerate(chord):
            if note == -1:
                lines[i] += space + space + space
            else:
                lines[i] += str(note) + space + space
    
    for line in lines[::-1]:
        line += end_delimiter
        print(line)
