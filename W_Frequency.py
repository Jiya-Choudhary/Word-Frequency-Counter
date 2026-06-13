print("Word Frequency Counter")
Text = input ("Enter Text:")
cleaned_text = Text.lower()
for punctuation in [".",",",";",":","!","?"]:
    cleaned_text=cleaned_text.replace(punctuation,"")
words = cleaned_text.split()
word_counts={}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print("Frequency of Words using Dictionary")
print(word_counts)
Sorted_words=sorted(word_counts.items(), key=lambda item: item[1] , reverse=True)
top_5={word: count for word, count in Sorted_words[:5]}
print("Top 5 most Frequent words:")
print(top_5)