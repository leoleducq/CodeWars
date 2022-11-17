def validate_pin(pin):
    return False if not pin.isdigit() else True if len(pin) == 4 or len(pin) == 6 else False