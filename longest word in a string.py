sentence = input("Enter a sentence: ")
words = sentence.split()
print(max(words, key=len))


            (or)
-------------------------------


string="revathi gude welcome  aaaaaaaaaa"
string1=string.split()
new_str=""
for word in string1:
    if len(word)>len(new_str):
        new_str=word
print(new_str)
