def number_of_a(word):
    count = 0
    for c in word:
        if c == 'a':
            count += 1
    return count


l = ["we", "wesadfasdfsdsd", "z", "abcdef"]
print(min(l, key=number_of_a))

l.sort(key=number_of_a)
print(l)

