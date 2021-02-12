f = open("for_lesson_5.txt", "a")
data_for_file = ['Milk\n', 'Bread\n', 'Sugar\n', 'Salad']
f.writelines(data_for_file)
f.close()