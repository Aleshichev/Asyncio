text = "aa bb cc aa bb aa"

counter = {}

def word_counter():
    while True:
        word = yield from word_accumulator()  # await
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
            
def word_accumulator():
    word = ""
    while True:
        char = yield
        if char == ' ':
            return word
        else:
            word += char
            
wc = word_counter()
next(wc)
print("back")
for char in text:
    wc.send(char)
wc.send(" ")    

print(counter)