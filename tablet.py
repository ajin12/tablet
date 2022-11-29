import sys
import importlib

# source file is the first argument to the script
if len(sys.argv) != 2:
    print('usage: %s <src.tablet>' % sys.argv[0])
    sys.exit(1)

sys.path.insert(0, 'modules')

with open(sys.argv[1], 'r') as file:
    module = importlib.import_module("tablet")
    tab = []

    for line in file:
        line = line.strip()
        if not line or line[0] == '#':
            continue
        parts = line.split()

        chord = getattr(module, parts[0])(parts[1], parts[2])
        tab.append(chord)

    getattr(module, "print_tab")(tab)