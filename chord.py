from enum import Enum

from utils import raise_enum_type_error

class ChordFamily(Enum):
    A = "A"
    ASharp = "A#"
    BFlat = "Bb"
    B = "B"
    C = "C"
    CSharp = "C#"
    DFlat = "Db"
    D = "D"
    DSharp = "D#" 
    EFlat = "Eb"
    E = "E"
    F = "F"
    FSharp = "F#"
    GFlat = "Gb"
    G = "G"
    GSharp = "G#"
    AFlat = "Ab"

class ChordType(Enum):
    MAJOR = "major"
    MINOR = "minor"
    DOMINANT7 = "dominant7"
    MINOR7 = "minor7"
    DIMINISHED = "diminished"
    AUGMENTED = "augmented"
    MAJOR6 = "major6"
    MINOR6 = "minor6"
    SUSPENDED4 = "suspended4"

class Chord:
    def __init__(self, family, type):
        if family not in ChordFamily._value2member_map_:
            raise_enum_type_error("Unrecognized chord family", family, ChordFamily)
        if type not in ChordType._value2member_map_:
            raise_enum_type_error("Unsupported chord type", family, ChordType)

        self.family = family
        self.type = type

    def play_major(self):
        match self.family:
            case "A":
                return [-1, 0, 2, 2, 2, 0]
            case "A#" | "Bb":
                return [-1, 1, 3, 3, 3, -1]
            case "B":
                return [-1, -1, 4, 4, 4, 2]
            case "C":
                return [-1, 3, 2, 0, 1, 0]
            case "C#" | "Db":
                return [-1, 4, 3, 1, 2, -1]
            case "D":
                return [-1, -1, 0, 2, 3, 2]
            case "D#" | "Eb":
                return [-1, 6, 5, 3, 4, -1]
            case "E":
                return [0, 2, 2, 1, 0, 0]
            case "F":
                return [-1, -1, 3, 2, 1, 1]
            case "F#" | "Gb":
                return [-1, -1, -1, 3, 2, 2]
            case "G":
                return [3, 2, 0, 0, 0, 3]
            case "G#" | "Ab":
                return [4, 6, 6, 5, -1, -1]
    
    def play_minor(self):
        match self.family:
            case "A":
                return [-1, -1, 2, 2, 1, 0]
            case "A#" | "Bb":
                return [-1, 1, 3, 4, 2, 1]
            case "B":
                return [-1, -1, 4, 4, 3, 2]
            case "C":
                return [-1, 3, 1, 0, 4, 3]
            case "C#" | "Db":
                return [-1, -1, 2, 1, 2, 0]
            case "D":
                return [-1, -1, 0, 2, 3, 1]
            case "D#" | "Eb":
                return [-1, -1, -1, 3, 4, 2]
            case "E":
                return [0, 2, 2, 0, 0, 0]
            case "F":
                return [-1, -1, 3, 1, 1, 1]
            case "F#" | "Gb":
                return [-1, 4, 4, 2, 2, 2]
            case "G":
                return [-1, -1, 0, 3, 3, 3]
            case "G#" | "Ab":
                return [-1, -1, 6, 4, 4, 4]
    
    def play_dominant7(self):
        match self.family:
            case "A":
                return [0, 0, 2, 0, 2, 0]
            case "A#" | "Bb":
                return [1, 1, 3, 1, 3, 1]
            case "B":
                return [2, 2, 4, 2, 4, 2]
            case "C":
                return [0, 3, 2, 3, 1, 0]
            case "C#" | "Db":
                return [1, 2, 3, 1, 2, 1]
            case "D":
                return [-1, 0, 0, 2, 1, 2]
            case "D#" | "Eb":
                return [-1, 1, 1, 3, 2, 3]
            case "E":
                return [0, 2, 2, 1, 3, 0]
            case "F":
                return [1, 3, 1, 2, 1, 1]
            case "F#" | "Gb":
                return [2, 4, 2, 3, 2, 2]
            case "G":
                return [3, 2, 0, 0, 0, 1]
            case "G#" | "Ab":
                return [4, 3, 1, 1, 1, 2]

    def play_minor7(self):
        match self.family:
            case "A":
                return [-1, 0, 2, 0, 1, 0]
            case "A#" | "Bb":
                return [1, 1, 3, 1, 2, 1]
            case "B":
                return [-1, 2, 0, 2, 0, 2]
            case "C":
                return [-1, 1, 1, 3, 1, 3]
            case "C#" | "Db":
                return [0, 2, 2, 4, 2, 4]
            case "D":
                return [-1, 0, 0, 2, 1, 1]
            case "D#" | "Eb":
                return [-1, 1, 1, 3, 2, 2]
            case "E":
                return [0, 2, 0, 0, 0, 0]
            case "F":
                return [1, 3, 1, 1, 1, 1]
            case "F#" | "Gb":
                return [2, 4, 2, 2, 2, 2]
            case "G":
                return [3, 5, 3, 3, 3, 3]
            case "G#" | "Ab":
                return [0, 0, 2, 2, 1, 3]

    def play_diminished(self):
        match self.family:
            case "A":
                return [5, 6, 7, 5, 4, 5]
            case "A#" | "Bb":
                return [0, 1, 2, 3, 2, 0]
            case "B":
                return [1, -1, 3, 4, 3, 1]
            case "C":
                return [-1, -1, 4, 5, 4, 2]
            case "C#" | "Db":
                return [0, -1, 2, 0, 2, 3]
            case "D":
                return [1, -1, 3, 1, 3, 1]
            case "D#" | "Eb":
                return [2, -1, 4, 2, 4, 2]
            case "E":
                return [3, -1, 5, 3, 5, 3]
            case "F":
                return [1, 2, 3, 1, 0, 1]
            case "F#" | "Gb":
                return [2, 0, 4, 2, 1, 2]
            case "G":
                return [3, 4, 0, 3, 2, 3]
            case "G#" | "Ab":
                return [4, 5, 0, 4, 3, 4]

    def play_augmented(self):
        match self.family:
            case "A":
                return [1, 0, 3, 2, 2, 1]
            case "A#" | "Bb":
                return [2, -1, 4, 3, 3, 2]
            case "B":
                return [3, -1, 5, 4, 4, 3]
            case "C":
                return [0, 3, 2, 1, 1, 0]
            case "C#" | "Db":
                return [-1, 0, 3, 2, 2, 1]
            case "D":
                return [2, -1, 4, 3, 3, 2]
            case "D#" | "Eb":
                return [3, 2, 1, 0, 0, 3]
            case "E":
                return [0, -1, 2, 1, 1, 0]
            case "F":
                return [1, -1, 3, 2, 2, 1]
            case "F#" | "Gb":
                return [2, -1, 4, 3, 3, 2]
            case "G":
                return [3, 2, 1, 0, 0, 3]
            case "G#" | "Ab":
                return [0, 3, 2, 1, 1, 0]

    def play_major6(self):
        match self.family:
            case "A":
                return [0, 0, 2, 2, 2, 2]
            case "A#" | "Bb":
                return [1, 1, 3, 3, 3, 3]
            case "B":
                return [2, 2, 4, 4, 4, 4]
            case "C":
                return [0, 3, 2, 1, 1, 0]
            case "C#" | "Db":
                return [1, 1, 3, 1, 2, 1]
            case "D":
                return [-1, 0, 0, 2, 0, 2]
            case "D#" | "Eb":
                return [-1, 1, 1, 3, 1, 3]
            case "E":
                return [0, 2, 2, 1, 2, 0]
            case "F":
                return [-1, 3, 3, 5, 3, 5]
            case "F#" | "Gb":
                return [-1, 4, 4, 6, 4, 6]
            case "G":
                return [3, 2, 0, 0, 0, 0]
            case "G#" | "Ab":
                return [4, 3, 1, 1, 1, 1]
    
    def play_minor6(self):
        match self.family:
            case "A":
                return [2, 0, 2, 2, 1, 2]
            case "A#" | "Bb":
                return [-1, -1, 3, 3, 2, 3]
            case "B":
                return [-1, 2, 0, 1, 3, 2]
            case "C":
                return [-1, 3, 1, 2, 1, 3]
            case "C#" | "Db":
                return [0, 4, 2, 3, 2, 4]
            case "D":
                return [-1, 0, 0, 2, 0, 1]
            case "D#" | "Eb":
                return [-1, 1, 1, 3, 1, 2]
            case "E":
                return [0, 2, 2, 0, 2, 0]
            case "F":
                return [1, 3, 3, 1, 3, 1]
            case "F#" | "Gb":
                return [-1, 4, 4, 6, 4, 5]
            case "G":
                return [0, 1, 0, 0, 3, 0]
            case "G#" | "Ab":
                return [-1, -1, 1, 1, 0, 1]
    
    def play_suspended4(self):
        match self.family:
            case "A":
                return [0, 0, 2, 2, 3, 0]
            case "A#" | "Bb":
                return [1, 1, 1, 3, 4, 1]
            case "B":
                return [2, 2, 4, 4, 5, 2]
            case "C":
                return [3, 3, 3, 0, 1, 1]
            case "C#" | "Db":
                return [4, 4, 6, 6, 7, 4]
            case "D":
                return [-1, 0, 0, 2, 3, 3]
            case "D#" | "Eb":
                return [-1, 1, 1, 1, 4, 4]
            case "E":
                return [0, 2, 2, 2, 0, 0]
            case "F":
                return [1, 1, 3, 3, 1, 1]
            case "F#" | "Gb":
                return [2, 2, 4, 4, 2, 2]
            case "G":
                return [3, 3, 0, 0, 1, 3]
            case "G#" | "Ab":
                return [4, 4, 6, 6, 4, 4]
    