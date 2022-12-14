from chord import Chord, get_supported_chord_names_list

# TODO: be able to change tuning
tuning = ["E", "A", "D", "G", "B", "e"]
space = "-"
start_delimiter = "["
end_delimiter = "]"

NUM_STRINGS = 6

tab = []
custom_chords = {}

def play(name):
    if name in custom_chords:
        tab.append(custom_chords[name])
    else:
        [chord, type] = name.split(" ")
        chord = Chord(chord, type)
        chord_method = 'play_' + type
        tab.append(getattr(chord, chord_method)())

def create_chord(shape, chord_name):
    # check if chord is already supported
    chord_names = get_supported_chord_names_list()
    if chord_name in chord_names:
        print(chord_name, "already exists in the Tablet chord library. Please use a different name.")
        raise NameError("Cannot override existing chord")
    custom_chords[chord_name] = shape

def print_tab():
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
