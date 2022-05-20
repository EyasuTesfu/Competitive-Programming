

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#
def countingValleys(steps, path):
    valley = 0
    mountain = 0
    up, down = 0, 0
    for i in range(steps):
        if up > down:
            if path[i] == 'U':
                up += 1
            else:
                down += 1
                if up == down:
                    mountain += 1
                    up, down = 0, 0
        elif down > up:
            if path[i] == 'U':
                up += 1
                if up == down:
                    valley += 1
                    up, down = 0, 0
            else:
                down += 1

        elif up == down != 0:
            if path[i] == 'U':
                up += 1
            else:
                down += 1
    return valley
#
#
# more compact but the same thing below


def countingValleys(steps, path):
    altitude = valley = 0
    for step in path:
        altitude += 1 if step == 'U' else -1
        if step == 'U' and altitude == 0:
            valley += 1
    return valley
