def friend(x):
    return list(filter(None,[friend if len(friend) ==4 else "" for friend in x]))