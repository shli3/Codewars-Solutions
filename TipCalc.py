import math

def calculate_tip(amount, rating):
    rate = rating.casefold()
    if rate == "terrible":
        return 0
    elif rate == "poor":
        return math.ceil(amount * 0.05)
    elif rate == "good":
        return math.ceil(amount * 0.10)
    elif rate == "great":
        return math.ceil(amount * 0.15)
    elif rate == "excellent":
        return math.ceil(amount * 0.20)
    else:
        return "Rating not recognised"
