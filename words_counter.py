import sys

input_strings = ("").join(sys.stdin.readlines()).casefold()
synt = ",!:.?;-"


for out in input_strings:
    if out in synt:
        input_strings = input_strings.replace(out, "")
    if out == "\n":
        input_strings = input_strings.replace(out, " ")

correct_input_strings = input_strings.split(" ")

for lenght, value in enumerate(correct_input_strings):
    if len(value) < 3:
        correct_input_strings.pop(lenght)

dict_values = {}
list_values = []

for word in correct_input_strings:
    if word not in list_values:
        list_values.append(word)
        dict_values[word] = 1
    else:
        dict_values[word] += 1

key_sort = sorted(dict_values)
value_sort = sorted(dict_values.values())
value_sort = value_sort[::-1]
count = int(value_sort[0])
dict_sort1 = {}

for sort_symb in key_sort:
    dict_sort1[sort_symb] = dict_values[sort_symb]

dict_result = {}

while count > 0:
    for key, value in dict_sort1.items():
        if value == count:
            dict_result[key] = value
        else:
            continue
    count -= 1

count_2 = 0
print("\n10 самых часто встречающихся слов в тексте:\n")
for top_key, top_value in dict_result.items():
    if count_2 < 10:
        print(f"{top_key}: {top_value}")
        count_2 += 1
    else:
        break
