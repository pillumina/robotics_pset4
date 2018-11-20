def get_line(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return


def generate_new_path(start, end):
    result = []
    dx, dy = end[0] - start[0], end[1] - start[1]
    if dx == 0:
        result = [(start[0], start[1] + i) for i in range(1, dy + 1)]
    else:
        for i in range(1, abs(dx) + 1):
            node = (start[0] + int(i * abs(dx) / dx), start[1] + int(i * dy / abs(dx)))
            result.append(node)
    return result

result =generate_new_path((1,1), (10, 10))

print(result)