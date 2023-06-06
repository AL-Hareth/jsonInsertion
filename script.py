import sys

output_file = open('./output.json', "a")

n = int(sys.argv[1])
dict = {}

if output_file.tell() == 0:
    output_file.write('[')
else:
    output_file.truncate(output_file.tell()-2)
    output_file.write(',')

for i in range(n):
    key = input("Key: ")
    value = input("Its value: ")
    dict[f'{key}'] = value

dictionary_string = '\n\t' + str(dict).replace('\'', '"') + ','

output_file.write(dictionary_string)

output_file.truncate(output_file.tell()-1)
output_file.write('\n]')
