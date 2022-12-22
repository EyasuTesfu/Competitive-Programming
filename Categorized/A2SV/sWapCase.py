def swap_case(s):
    _list = []
    for i in range(len(s)):
        if s[i].isalnum():
            if s[i].islower():
                _list.append(s[i].upper())
            elif s[i].isupper():
                _list.append(s[i].lower())
            else:
                _list.append(s[i])
        else:
            _list.append(s[i])

    return "".join(_list)
