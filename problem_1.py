def reverse_string(s):
    reverse = ""
    for i in range(len(s) - 1, -1, -1):
        reverse = reverse + s[i]
    return reverse

