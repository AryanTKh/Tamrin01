def fspace(input_text):
    words = filter(None, input_text.split(' '))
    rd = ' '.join(words)
    return rd

text = input()

outt = fspace(text)
modified = outt
x = 0
h = 0
for i in outt:
    texxx = modified[x:]
    if(i == "@"):
        h += 1
        modified = modified[:x-h+1] + modified[x-h+1:].replace('#', '', 1)
    x += 1


print("Formatted Text: "+modified.replace("\\n","\n"))
