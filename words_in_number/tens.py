tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
        90: 'ninety'}


def ten(numbers):
    """Return tens values on request"""
    for key, value in tens.items():
        if key == int(numbers):
            return value.title()
