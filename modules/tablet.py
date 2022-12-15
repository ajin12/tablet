from chord import ABBR, Chord, get_supported_chord_names_list
from enum import Enum

# TODO: be able to change tuning
tuning = ["E", "A", "D", "G", "B", "e"]
space = "-"
indent_len = 5
max_abbr_len = 4
NUM_SPACES = max_abbr_len + 1 # leave enough room for labeling chords
start_delimiter = "["
end_delimiter = "]"

NUM_STRINGS = 6

class TabType(Enum):
    Text = "text"
    Chord = "chord"
    Lyric = "lyric"

tab = []
custom_chords = {}
current_section = None
last_lyric = None

def play(name_or_shape, lyric_index = None):
    match type(name_or_shape).__name__:
        case "str":
            if name_or_shape in custom_chords:
                tab.append({ 
                    "type": TabType.Chord, 
                    "value": custom_chords[name_or_shape],
                    "section": current_section,
                    "lyric_index": lyric_index,
                })
            else:
                [chord, chord_type] = name_or_shape.split(" ")
                chord_obj = Chord(chord, chord_type)
                chord_method = 'play_' + chord_type
                shape = getattr(chord_obj, chord_method)()
                tab.append({ 
                    "type": TabType.Chord,
                    "value": shape,
                    "section": current_section,
                    "abbr": chord + ABBR[chord_type],
                    "lyric_index": lyric_index,
                })
        case "list": # custom shape
            tab.append({
                "type": TabType.Chord,
                "value": name_or_shape,
                "section": current_section,
                "lyric_index": lyric_index,
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

def add_lyric(lyric):
    tab.append({
        "type": TabType.Lyric,
        "value": lyric,
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
    global last_lyric

    def reset_lines():
        lines = [""] * NUM_STRINGS
        for i, string in enumerate(tuning):
            lines[i] += string + " " + start_delimiter + space + space
        return lines, " " * indent_len, 0, 0, True, True

    def print_lines(lines):
        print(chord_label_line)
        for line in lines[::-1]:
            line += space + space + end_delimiter
            print(line)
    
    lines, chord_label_line, curr_char_pos, last_abbr_len, is_first_chord, is_empty = reset_lines()

    for item in tab:
        match item["type"]:
            case TabType.Text | TabType.Lyric:
                if not is_empty:
                    print_lines(lines)
                    print()

                if item["type"] == TabType.Text:
                    print(item["value"])
                    last_lyric = None
                else:
                    print(" " * indent_len + item["value"])
                    last_lyric = item["value"]

                lines, chord_label_line, curr_char_pos, last_abbr_len, is_first_chord, is_empty = reset_lines()
            case TabType.Chord:
                num_spaces = 0
                if item["lyric_index"]:
                    if not last_lyric:
                        print("Lyric not found. Did you mean to add a lyric before calling play?")
                        raise ValueError("Lyric not found")

                    lyric_index = item["lyric_index"] - 1
                    target_char_pos = len(" ".join(last_lyric.split()[0:lyric_index])) + 1
                    num_spaces = target_char_pos - curr_char_pos - 1
                    curr_char_pos = target_char_pos

                    if is_first_chord and lyric_index > 0:
                        num_spaces += 1
                        is_first_chord = False
                elif not is_empty:
                    num_spaces = NUM_SPACES
                elif is_first_chord:
                    is_first_chord = False
                
                # add line for chord labels
                if "abbr" in item:
                    chord_label_line += " " * (num_spaces - is_empty - last_abbr_len + 1) + item["abbr"]
                    last_abbr_len = len(item["abbr"])
                else:
                    chord_label_line += " " * (num_spaces - last_abbr_len + 1)
                    last_abbr_len = 0
                
                for i, note in enumerate(item["value"]):
                    for _ in range(num_spaces):
                        lines[i] += space

                    if note == -1:
                        lines[i] += space
                    else:
                        lines[i] += str(note)

                    is_empty = False

    if not is_empty:
        print_lines(lines)
