#!/usr/bin/python3
if __name__ == "main__":
    import hidden_4
    hidden4dir = dir(hidden_4)
    skip = "__"
    for i in range(0, len(hidden4dir)):
        if skip not in hidden4dir[i]:
            print(hidden4dir[i])
