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

    for line in file:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        parts = line.split()

        # TODO: make sure params are valid
        if "play" in parts:
            if len(parts) == NUM_STRINGS + 1:
                name_or_shape = [int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]), int(parts[6])]
            else:
                name_or_shape = " ".join(parts[1:])
            getattr(module, parts[0])(name_or_shape)
        elif "create_chord" in parts:
            shape = [int(parts[1]), int(parts[2]), int(parts[3]), int(parts[4]), int(parts[5]), int(parts[6])]
            name = " ".join(parts[7:])
            getattr(module, parts[0])(shape, name)
        elif "add_text" in parts:
            text = " ".join(parts[1:])
            getattr(module, parts[0])(text)
        elif any(part in ["create_section", "end_section", "repeat"] for part in parts):
            getattr(module, parts[0])(parts[1])

    getattr(module, "print_tab")()