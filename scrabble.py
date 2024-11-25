### MSCS3917
### HW7
### Yuxin Zhang

class Scrabble:
    def __init__(self):
        self.hashtable = {}

    def ADDhashtable(self, word):
        sortedword = ''.join(sorted(word))
        if sortedword in self.hashtable:
            self.hashtable[sortedword].append(word)
        else:
            self.hashtable[sortedword] = [word]

    def queryanagrams(self, word):
        sortedword = ''.join(sorted(word))
        return self.hashtable.get(sortedword, [])

scrabble = Scrabble()

words = ["tar", "rat", "art", "tart", "star", "stare"]
for word in words:
    scrabble.ADDhashtable(word)

anagrams = scrabble.queryanagrams("tar")
print(anagrams)  
