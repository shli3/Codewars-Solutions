def bouncingBall(h, bounce, window):
    counter = 0
    if h <= window or bounce <= 0 or bounce >= 1 or h < 0 or window < 0:
        return -1
    else:
        while h > window:
            if h * bounce > window: #ball passes up and down
                h = h * bounce
                counter = counter + 2
            else: #ball just passes down
                h = h * bounce
                counter = counter + 1
    return counter
