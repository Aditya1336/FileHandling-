file = open('youtube.txt','w')

try:
    file.write('Youtube app')
finally:
    file.close()

with open('youtube.txt','r') as file:
    print(file.read())