import re
def to_camel_case(text):
    text = re.split(r"[\-\_]",text)
    return text[0]+"".join([i.title() for i in text if i != text[0]])