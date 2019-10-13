words = open('word_list.txt', 'r').read().split()

good_words = []
for word in words:
    if len(word) < 4:
        continue
    if not word.isalpha():
        continue
    good_words.append(word)
            
with open('good_words.txt', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(good_words))
