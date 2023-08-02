from textblob import TextBlob

# print(dir(textblob))
# help(textblob)

input = input("enter a text")
obj = TextBlob(input)
print(obj.correct())
