def _camel(s):
    return s != s.lower() and s != s.upper()

def camel(s):
    if not _camel(s):
        return False
    # exclude some outliers
    if s.startswith("__") and s.endswith("__"):
        return False
    if "_" not in s:
        return False
    if s.startswith("_") and "_" not in s[1:] and not camel(s[1:]):
        return False
    return True

def to_snake_case(not_snake_case):
    final = ''
    while not_snake_case.startswith("_"):
        final += "_"
        not_snake_case = not_snake_case[1:]
    for i in range(len(not_snake_case)):
        item = not_snake_case[i]
        if i < len(not_snake_case) - 1:
            next_char_will_be_underscored = (not_snake_case[i+1] == "_"  \
                    or not_snake_case[i+1] == " " \
                    or not_snake_case[i+1].isupper())
        if (item == " " or item == "_") and next_char_will_be_underscored:
            continue
        elif (item == " " or item == "_"):
            final += "_"
        elif item.isupper():
            final += "_"+item.lower()
        else:
            final += item
    return final

def strip_back_to_jumpscale_or_digitalme(fname):
    for search in ['Jumpscale', 'DigitalMe']:
        x = fname.find("Jumpscale")
        if x != -1:
            return fname[x:]
    return None

def camelCase(st):
    output = ''.join(x for x in st.title() if x.isalnum())
    return output[0].lower() + output[1:]
