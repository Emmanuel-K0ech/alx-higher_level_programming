def magic_string():
    string_1 = "BestSchool"
    magic_string.counter = getattr(magic_string, 'counter', 0) + 1
    return string_1 + (", BestSchool" * magic_string.counter)
