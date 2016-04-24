# Exercise 97
file = open("file.txt", "rU")
lines = file.readlines()
file.close()

result = list()
for line in lines:
    l = line.split("|")
    numbers = l[1].split(" ")

    values = list()
    for x in numbers:
        values.append(int(x))

    for y in values:
        result.append(l[0][y - 1])

    result.append("\n")

res = ''.join(result)

print(res.format("{0} \n {1}", res[0], res[1]))

# Exercise 116
code = {
    'A': '.-',     'B': '-...',    'C': '-.-.',
    'D': '-..',    'E': '.',       'F': '..-.',
    'G': '--.',    'H': '....',    'I': '..',
    'J': '.---',   'K': '-.-',     'L': '.-..',
    'M': '--',     'N': '-.',      'O': '---',
    'P': '.--.',   'Q': '--.-',    'R': '.-.',
    'S': '...',    'T': '-',       'U': '..-',
    'V': '...-',   'W': '.--',     'X': '-..-',
    'Y': '-.--',   'Z': '--..',    '1': '.----',
    '2': '..---',  '3': '...--',   '4': '....-',
    '5': '.....',  '6': '-....',   '7': '--...',
    '8': '---..',  '9': '----.',   '0': '-----',
    '.': '.-.-.-', ',': '--..--',  ':': '---...',
    ';': '-.-.-.', '?': '..--..',  '!': '-.-.--',
    '"': '.-..-.', "'": '.----.',  '+': '.-.-.',
    '-': '-....-', '/': '-..-.',   '=': '-...-',
    '_': '..--.-', '$': '...-..-', '@': '.--.-.',
    '&': '.-...',  '(': '-.--.',   ')': '-.--.-'
}

file = open("fileMorse.txt", "rU")
lines = file.readlines()
file.close()

translate = ""
for line in lines:
    words = line.split("  ")
    for x in words:
        word = x.split(" ")
        for c in word:
            for k, v in code.items():
                if v == c:
                    translate += k

print(translate)

# Exercise 30
file = open("fileSet.txt", "rU")
lines = file.readlines()
file.close()

for line in lines:
    both = line.split(";")
    set1 = set(both[0].split(","))
    set2 = set(both[1].split(","))
    print(set1.intersection(set2))

# Exercise 173
file = open("fileRep.txt", "rU")
lines = file.readlines()
file.close()

for line in lines:
    l = list(line)

    result = ""
    i = 0
    while i < len(l) - 1:
        if l[i] != l[i + 1]:
            result += l[i]
        i += 1

    result += l[i]

    print(result)