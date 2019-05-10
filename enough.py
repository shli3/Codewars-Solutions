#"Will there be enough space?"
def enough(cap, on, wait):
    roomLeft = cap - on
    if roomLeft < wait:
        cantFit = roomLeft - wait
        return -cantFit
    
    else: return 0