first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Задача 1
first_result = [len(string) for string in first_strings if len(string) >= 5]

# Задача 2
second_result = [(first_string, second_string)
                 for first_string in first_strings
                 for second_string in second_strings
                 if len(first_string) == len(second_string)]

# Задача 3
third_result = {string: len(string)
                for string in first_strings + second_strings
                if len(string) % 2 == 0}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
