string = "This is a sentence. This is another sentence. This is a third sentence."
char = "."

first_word = ""
words = 0

sentence_periods = []
sentence_list = []

for i in range(len(string)):
    if string[i] == char:
        sentence_periods.append(i)

print(sentence_periods)

last_period = -2

for i in sentence_periods:
    sentence_list.append(string[last_period+2:i+1])
    last_period = i

i = 0
for sentence in sentence_list:
    index = sentence.find(" ")
    first_word = sentence[0:index]
    words = sentence.count(' ') + 1
    i += 1
    print("Sentence", i, "-", "Words:", words, "First Word:", first_word)

