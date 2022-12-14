from chord import Chord, get_supported_chord_names_list

# TODO: be able to change tuning
tuning = ["E", "A", "D", "G", "B", "e"]
space = "-"
start_delimiter = "["
end_delimiter = "]"

NUM_STRINGS = 6

tab = []
custom_chords = {}

def play(name_or_shape):
    match type(name_or_shape).__name__:
        case "str":
            if name_or_shape in custom_chords:
                tab.append(custom_chords[name_or_shape])
            else:
                [chord, chord_type] = name_or_shape.split(" ")
                chord = Chord(chord, chord_type)
                chord_method = 'play_' + chord_type
                tab.append(getattr(chord, chord_method)())
        case "list": # custom shape
            tab.append(name_or_shape)

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
