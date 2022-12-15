import sys
import importlib

from modules.tablet import NUM_STRINGS

# source file is the first argument to the script
if len(sys.argv) != 2:
    print('usage: %s <src.tablet>' % sys.argv[0])
    sys.exit(1)

sys.path.insert(0, 'modules')

with open(sys.argv[1], 'r') as file:
    module = importlib.import_module("tablet")

    pdf_name = None

    for line in file:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        parts = line.split()

        # TODO: make sure params are valid
        if "play" in parts:
            has_lyric_index = "lyric" in line
            
            if len(parts) >= NUM_STRINGS + 1:
                name_or_shape = [int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]), int(parts[6])]
            else:
                if has_lyric_index:
                    name_or_shape = " ".join(parts[1:-1])
                else:
                    name_or_shape = " ".join(parts[1:])
            
            lyric_index = None
            if has_lyric_index:
                lyric_index = int(line.split("lyric:")[1])
            getattr(module, parts[0])(name_or_shape, lyric_index)
        elif "create_chord" in parts:
            shape = [int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]), int(parts[6])]
            name = " ".join(parts[7:])
            getattr(module, parts[0])(shape, name)
        elif any(part in ["add_text", "add_lyric"] for part in parts):
            text = " ".join(parts[1:])
            getattr(module, parts[0])(text)
        elif any(part in ["create_section", "end_section", "repeat"] for part in parts):
            getattr(module, parts[0])(parts[1])
        elif "export_pdf" in parts:
            pdf_name = " ".join(parts[1:])

    getattr(module, "print_tab")()

    if pdf_name:
        getattr(module, parts[0])(pdf_name)