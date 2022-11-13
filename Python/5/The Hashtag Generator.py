def generate_hashtag(s):
    if len(s) == 0 or len(s) > 140:
        return False
    else:
        return '#' + ''.join([word.capitalize() for word in s.split()])