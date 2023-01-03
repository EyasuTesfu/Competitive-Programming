# poblem link: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
def wrap(string, max_width):
    _list = []
    for i in range(0, len(string), max_width):
        _list.append(string[i:i+max_width])
    return "\n".join(_list)
