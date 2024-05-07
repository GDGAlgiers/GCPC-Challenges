def sol(s):
    words = s.replace("Ctrl + C", "#c").replace("Ctrl + V", "#v").replace("Ctrl + X", "#x").split()
    out = ""
    copied = ""

    for i in range(len(words)):
        if words[i] == "#c":
            copied = out
        elif words[i] == "#v":
            out += copied
        elif words[i] == "#x":
            copied = out if i < len(words) - 1 else out[:-1]
            out = ""
        else:
            out += words[i] + (" " if i < len(words) - 1 else "")

    return out

# result
inline = input("")
print(sol(inline))
