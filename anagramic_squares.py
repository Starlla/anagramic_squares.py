my_file = open("p098_words.txt", "r")
content = my_file.read()
word_list = [x.strip('"') for x in content.split(',')]
print(word_list)
my_file.close()
max_length = 0

dicts = {}

for word in word_list:
    if len(word) > max_length:
        max_length = len(word)
    char_list = list(word)
    char_list.sort()
    if str(char_list) not in dicts.keys():
        dicts[str(char_list)] = [word]
    else:
        dicts[str(char_list)].append(word)
dicts2= {}
maxLenAnagram = 0
for k, v in dicts.items():
    if len(v) > 1 and len(v[0]) > 4:
        dicts2[k] = v
        print(str(k) + " " + str(v))
        if len(v[0])> maxLenAnagram:
            maxLenAnagram =len(v[0])

print(dicts2)
print(maxLenAnagram)
print(max_length)

for k, v in dicts2.items():
    if len(v[0]) == maxLenAnagram:
        print(str(k) + " " + str(v))


