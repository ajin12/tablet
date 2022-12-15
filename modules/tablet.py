from chord import Chord, get_supported_chord_names_list
from enum import Enum

# TODO: be able to change tuning
tuning = ["E", "A", "D", "G", "B", "e"]
space = "-"
start_delimiter = "["
end_delimiter = "]"

NUM_STRINGS = 6

class TabType(Enum):
    Text = "text"
    Chord = "chord"

tab = []
custom_chords = {}
current_section = None

def play(name_or_shape):
    match type(name_or_shape).__name__:
        case "str":
            if name_or_shape in custom_chords:
                tab.append({ 
                    "type": TabType.Chord, 
                    "value": custom_chords[name_or_shape],
                    "section": current_section,
                })
            else:
                [chord, chord_type] = name_or_shape.split(" ")
                chord = Chord(chord, chord_type)
                chord_method = 'play_' + chord_type
                shape = getattr(chord, chord_method)()
                tab.append({ 
                    "type": TabType.Chord,
                    "value": shape,
                    "section": current_section,
                })
        case "list": # custom shape
            tab.append({
                "type": TabType.Chord,
                "value": name_or_shape,
                "section": current_section,
            })

def create_chord(shape, chord_name):
    # check if chord is already supported
    chord_names = get_supported_chord_names_list()
    if chord_name in chord_names:
        print(chord_name, "already exists in the Tablet chord library. Please use a different name.")
        raise NameError("Cannot override existing chord")
    custom_chords[chord_name] = shape

def add_text(text):
    tab.append({
        "type": TabType.Text,
        "value": text,
        "section": current_section, 
    })

def create_section(section_name):
    global current_section

    if current_section:
        print("Nested sections are unsupported. Please end", current_section, "first.")
        raise NotImplementedError("Cannot create nested sections")
    current_section = section_name

    tab.append({
        "type": TabType.Text,
        "value": "[%s]" % section_name,
        "section": section_name,
    })

def end_section(section_name):
    global current_section

    if current_section != section_name:
        print("Section name does not match. Did you mean to end", current_section + "?")
        raise NameError("Section name does not match")
    current_section = None

def repeat(section_name):
    section_items = [item for item in tab if item["section"] == section_name]
    if not section_items:
        print("No section named", section_name, "exists.")
        raise NameError("Section does not exist")
    for item in section_items:
        tab.append(item)

def print_tab():
    def reset_lines():
        lines = [""] * NUM_STRINGS
        for i, string in enumerate(tuning):
            lines[i] += string + " " + start_delimiter + space + space
        is_empty = True
        return lines, is_empty

    def print_lines(lines):
        for line in lines[::-1]:
            line += end_delimiter
            print(line)
    
    lines, is_empty = reset_lines()

    for item in tab:
        match item["type"]:
            case TabType.Text:
                if not is_empty:
                    print_lines(lines)
                    print()

                print(item["value"] + "\n")

                lines, is_empty = reset_lines()
            case TabType.Chord:
                for i, note in enumerate(item["value"]):
                    if note == -1:
                        lines[i] += space + space + space
                    else:
                        lines[i] += str(note) + space + space
                    is_empty = False

    if not is_empty:
        print_lines(lines)
