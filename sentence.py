sentence_list = []
indices = [0]
sentence = "I wonder how this will work."

for idx, char in enumerate(sentence):
    if char == ' ':
        indices.append(idx + 1)
sentence_list = sentence.split(' ')

print(sentence_list)
print(indices)