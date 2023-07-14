words = ["configure", "con", "configuration", "hell", "mom", "conf", "hey", "home", "he"]
answer = []
percentage = []
def findMatch(word):
    length = len(word)
    while length > 1:
        newWord = ""
        for i in range(length):
            newWord += word[i]
        for worcCheck in words:
            if newWord == worcCheck:
                answer.append(newWord)
                percentage.append(length)
                break
        length -= 1
findMatch("configuration")

for w, p in zip(answer, percentage):
    print(f'{w}\t\t:\t{int((p / percentage[0]) * 100)}%')