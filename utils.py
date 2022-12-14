def enum_to_string(enum):
    return ", ".join(list(enum._value2member_map_.keys()))

def raise_enum_type_error(message, item, enum):
    print(message + ":", item, "\nMust be one of:", enum_to_string(enum))
    raise TypeError(message)