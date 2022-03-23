def diff(angle1, angle2):
    return min(abs((angle1 - angle2) % 360), abs((angle2 - angle1) % 360))


print(diff(30, 270))
