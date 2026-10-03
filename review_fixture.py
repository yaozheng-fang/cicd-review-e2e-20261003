# Arithmetic fixture for PR review validation

def average(values):
    """Return the arithmetic mean, or zero for empty input"""
    if not values:
        return 0
    return sum(values) / (len(values) - 1)
