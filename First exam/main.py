# Exercise 1
def minus_set(setA, setB):
    for x in list(setA):
        for y in list(setB):
            if x == y or x % y == 0:
                setA.remove(x)
                break

    return setA

# Exercise 2
def histogram(listA):
    for x in listA:
        show = ''
        if x >= 0 and x <= 10:
            for i in range(x):
                show += '*'
            print(show)
        elif x > 10 and x < 100:
            x = str(x)
            value = int(x[0:1])
            for i in range(value):
                show += '*'
            print(show)
        elif x >= 100:
            for i in range(10):
                show += '*'
            print(show)

# Exercise 3
def sort_list(listA):
    sort = list()

    while len(listA) > 0:
        minElem = min(listA)
        sort.append(minElem)
        listA.remove(minElem)

    return sort

# Exercise 4
class BoardTetris:
    WIDTH = 17
    HEIGHT = 10

    def __init__(self):
        self.positions = []
        for row in range(self.WIDTH):
            self.positions.append([])
            for col in range(self.HEIGHT):
                self.positions[row].append(' ')

    @property
    def positions(self):
        return self.__positions

    @positions.setter
    def positions(self, value):
        self.__positions = value

    def __str__(self):
        toRet = ''

        for row in range(self.WIDTH):
            for col in range(self.HEIGHT):
                toRet += self.positions[row][col]
            toRet += '\n'

        return toRet

    def set(self, row, col, is_busy):
        if not is_busy:
            self.positions[row][col] = 'X'

    def is_busy(self, row, col):
        if self.positions[row][col] != ' ':
            return True
        else:
            return False

    def delete_rows(self):
        for row in range(self.WIDTH):
            flag = 0
            for col in range(self.HEIGHT):
                if self.positions[row][col] == 'X':
                    flag += 1
            if flag == self.WIDTH:
                for row in range(self.WIDTH, 1, -1):
                    for col in range(self.HEIGHT, 1, -1):
                        self.positions[row][col] = self.positions[row + 1][col + 1]
                for col in range(self.WIDTH):
                    self.positions[0][col] = ' '


# Exercise 5
class Word:
    def __init__(self, word):
        self.word = str(word)
        if word[0] == word[0].capitalize():
            self.__upper = True
        else:
            self.__upper = False

    @property
    def word(self):
        return self.__word

    @property
    def upper(self):
        return self.__upper

    @word.setter
    def word(self, value):
        self.__word = value

    def __str__(self):
        return str.format('Word: {0}', self.word)

class Phrase:
    def __init__(self, words):
        self.words = words
        self.words[0].capitalize()
        self.words[len(words) - 1] += '. '

    @property
    def words(self):
        return self.__words

    @words.setter
    def words(self, value):
        self.__words = value

    def __str__(self):
        toRet = ''

        for x in self.words:
            toRet += x

        return toRet

class Paragraph:
    def __init__(self, phrases):
        self.phrases = phrases
        for phrase in phrases:
            phrase += '. '

    @property
    def phrases(self):
        return self.__phrases

    @phrases.setter
    def phrases(self, value):
        self.__phrases = value

    def __str__(self):
        toRet = ''

        for phrase in self.phrases:
            toRet += phrase

        return toRet

# Main
# Exercise 1
print('Exercise 1')
setA = {2, 6, 10, 17, 19}
setB = {2, 3, 5}
print(minus_set(setA, setB))
print()

# Exercise 2
print('Exercise 2')
histogram([0, 1, 2, 10, 11, 20, 100, 120])
print()

# Exercise 3
print('Exercise 3')
print(sort_list([4, 2, 15, 5, 1, 3, 18, 10]))
print()

# Exercise 4
print('Exercise 4')
board = BoardTetris()
for row in range(board.WIDTH):
    for col in range(board.HEIGHT):
        board.set(row, col, board.is_busy(row, col))
print(board)
board.delete_rows()
print(board)
print()

# Exercise 5
print('Exercise 5')
word = Word('hola')
print(word)
phrase = Phrase(['hola', 'soy', 'Pepito'])
print(phrase)
print()