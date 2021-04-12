def decode(seq):
    atoz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""

    for num in seq:
        result += atoz[num-1]
    return result


def encode(str):
    atoz = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    for char in str:
        result.append(atoz.index(char)+1)

    return result


seq = encode("RAMRAJ")
print(seq)
print(decode(seq))


# to write information/data into a file, use encoding method.
# read and decode, to see the information/data in the file.
