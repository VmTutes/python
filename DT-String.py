str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

text = "Python is awesome"
length = len(text)
print("wow length", length)

text = "Python is awesome"
uppercase = text.upper()
lowercase = text.lower()
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

text = "Python is awesome"
new_text = text.replace("awesome", "great")
print("Modified text:", new_text)

text = "*%$Some spaces around      "
stripped_text = text.lstrip()
print("Stripped text:", stripped_text)

text = "Python is awesome"
vm = "is"
if vm in text:
    print(vm, "found in the text")

    
text = "Python.awesome"
words = text.split(".")[1]
print("Words:", words)    