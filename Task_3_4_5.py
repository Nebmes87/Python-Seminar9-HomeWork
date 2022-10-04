# 1. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый элемент списка является и ключом и значением. 
# Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.

lst = ['Илья', 35, 'Python', 6, 9.22]


def to_dict(lst):
   return {x: x for x in lst}


print(to_dict(lst))

# или
lst=["1","2","3","4"]
dictionary={}


def to_dict(lst):
    for i in range(len(lst)):
        dictionary[lst[i]] = lst[i]
    return(dictionary)


to_dict(lst)
print(to_dict(lst))



# 2. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs), 
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь my_dict,
# состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

my_dict = {'first_one': 'we can do it'}

def biggest_dict(**kwargs):
   my_dict.update(**kwargs)

biggest_dict(a=1, b=2, c=3, d=4)
biggest_dict(surname='Иванов', name='Иван', age=40, post='director')
print(my_dict)



# 3. Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь, который в качестве ключей будет принимать данные числа 
# (т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence), 
# принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел. 

from collections import Counter

def count_it(sequence):
    return dict(Counter([int(num) for num in sequence]).most_common(3))

print(count_it('12345612223458995447855596558554422355'))
print(count_it('66665555558888888877777772221111145522354'))

# или
import random
length= int(input ('сколько элементов в строке? '))
rand_num = [random.randint(0,9) for i in range(length)]

def count_it(sequence):
   d = {}
   for i in range(9):
      num_of_i = 0
      for e in sequence:
         if i == e:
            num_of_i = num_of_i + 1
      d[i] = num_of_i
      d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
   print(d)
   d_1 = {}
   for i, (k, v) in enumerate(d.items()):
      if i == 3: break
      d_1[k] = v
   return d_1


print(rand_num)
print (count_it(rand_num))