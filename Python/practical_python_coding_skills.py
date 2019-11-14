# 1.字符串倒转
# 以下代码段使用 Python 切片操作反转字符串。
# reverse a string using slicing
my_string = 'ABCDE'
reversed_string = my_string[::-1]
assert reversed_string == 'EDCBA'


# 2.首字母大写
# 以下代码段可用于将字符串转换为标题首字母大写。这是使用 title（）方法完成的。
# using title() function of string class
my_string = 'this is my title'
new_string = my_string.title()
assert new_string == 'This Is My Title'


# 3.在字符串中查找唯一元素
# 以下代码段可用于查找字符串中所有的唯一元素。我们使用集合中唯一元素。
my_string = 'aaabbbcccddeefffffff'
# converting string to a set
temp_set = set(my_string) # note : elements in set() are not ordered

# stitching set into a string using join
new_string = ''.join(temp_set)

# 4.n次打印字符串或列表
# 可以对字符串或列表使用乘法（*）。我们可以将它们任意复制。
n = 3 # number of repetitions
my_string = 'abcd'
my_list = [1, 2, 3]

assert my_string * n == 'abcdabcdabcd'
assert my_list * n == [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 一个有趣的用例是定义一个具有恒定值的列表——假设为零。
my_list = [0] * n # n denotes the length of the required list
assert my_list == [0, 0, 0]

# 5.列表推导式
# 列表推导式为我们提供了一种在其他列表基础上创建列表的好方法。
# 以下代码段通过将旧列表的每个元素乘以 2 来创建新列表。
# multiplying each element in a list by 2
my_list = [1, 2, 3, 4]
new_list = [i * 2 for i in my_list]
assert new_list == [2, 4, 6, 8]


# 6.变量交换
# 在两个变量之间交换值而不使用另一个变量
a = 1
b = 2
a, b = b, a
assert a == 2
assert b == 1


# 7.将字符串拆分为子字符串列表
# 我们可以使用字符串类中的.split（）方法将字符串拆分为子字符串列表，还可以将要分割的分隔符作为参数传递
string_1 = 'This is a sample'
string_2 = 'sample/ string'

# default separator ' '
split_list_1 = string_1.split()
assert split_list_1 == ['This', 'is', 'a', 'sample']

split_list_2 = string_2.split('/')
assert split_list_2 == ['sample', ' string']


# 8.将字符串列表组合成单个字符串
# join() 将作为参数传递的字符串列表组合为单个字符串
list_of_strings = ['This', 'is', 'a', 'string']
new_string = ','.join(list_of_strings)
assert new_string == 'This,is,a,string'

# 9.检查回文字符串
my_string = 'abcba'
is_palindrome = my_string == my_string[::-1]


# 10.使用Python Counter类统计列表中的元素
# Python 计数器跟踪容器中每个元素的频率， Counter()返回一个字典，其中元素作为键，频率作为值。
# finding frequency of each element in a list
from collections import Counter

my_list = ['a', 'b', 'b', 'c', 'c', 'c', 'd', 'd', 'd', 'd']
count = Counter(my_list)

assert count == {'a': 1, 'b': 2, 'c': 3, 'd': 4}
assert count['d'] == 4

assert count.most_common(1) == [('d', 4)] # most frequent element


# 11.查找两个字符串是否为字母异位词
# 字母异位词是通过重新排列不同单词的字母而形成的单词
from collections import Counter
str_1, str_2 = 'anagram', 'nagaram'
cnt_1, cnt_2 = Counter(str_1), Counter(str_2)
is_anagram = (cnt_1 == cnt_2)


# 12.使用 try-except-else 块
# 使用try/except块可以轻松完成Python中的错误处理，向该块添加 else 语句可能会很有用，
# 在 try 块中没有引发异常的情况下运行。
a, b = 1, 0
try:
    c = a / b
except ZeroDivisionError:
    print('Error : division by 0')
else:
    print('no exception raised') # if no exception, else will run
finally:
    print('run this always')


# 13.使用枚举获取索引/值对
my_list = ['a', 'b', 'c', 'd', 'e']
for index, value in enumerate(my_list):
    print(index, value)


# 14.检查对象的内存使用情况
import sys
n = 21
print(sys.getsizeof(n))


# 15.合并两个字典
# 在Python2中，我们使用了update()方法来合并两个字典， Python3.5使这一过程变得更加简单
# 在下面给出的脚本中，两个字典被合并。在相交的情况下，使用第二个字典中的值
dict_1 = {'a': 9, 'b': 6}
dict_2 = {'b': 4, 'c': 8}
combined_dict = {**dict_1, **dict_2}
assert combined_dict == {'a': 9, 'b': 4, 'c': 8}

# 16.执行一段代码所需的时间
# 以下代码片段使用库函数来计算执行代码所需的时间消耗。
import time

start_time = time.time()

# execute code
for i in range(1000):
    # do something
    pass

end_time = time.time()
time_taken = end_time - start_time # 默认为秒


# 17.从列表中随机取样
import random
my_list = ['a', 'b', 'c', 'd', 'e']
num_samples = 2

samples = random.sample(my_list, num_samples)
print(samples) # e.g. ['a', 'e']

# 秘密库生成随机样本进行加密， 以下代码段仅适用于 Python 3
import secrets
secure_random = secrets.SystemRandom()

my_list = ['a', 'b', 'c', 'd', 'e']
num_samples = 2

samples = secure_random.sample(my_list, num_samples)

print(samples) # two random values


# 18.数字化
# 以下代码段会将整数转换为数字列表。
num = 123456

# using map
list_of_digits = list(map(int, str(num)))
assert list_of_digits == [1, 2, 3, 4, 5, 6]

# using list comprehension
list_of_digits = [int(i) for i in str(num)]
assert list_of_digits == [1, 2, 3, 4, 5, 6]


# 19.检查唯一性
# 以下函数将检查列表中的所有元素是否唯一
def unique(l):
    if len(l) == len(set(l)):
        print('All elements are unique')
    else:
        print('List has duplicates')
