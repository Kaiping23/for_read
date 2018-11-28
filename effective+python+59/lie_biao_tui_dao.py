#! /usr/bin/env python
# -*-coding:utf8-*-
# __author__ = 'Jordan'

my_lists = [
    [[1, 2, 3], [4, 5, 6]]
]
# 列表表达式取出，内部的所有元素
flat = [x for sublist1 in my_lists
        for sublist2 in sublist1
        for x in sublist2
        ]

print(flat)

# 以上列表表达式可以转换为下面的for循环
flat = []
for sublist1 in my_lists:
    for sublist2 in sublist1:
        flat.extend(sublist2)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]

print(b)
print(c)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 要从原矩阵中把那些本身能为 3 所整除，且其所在行的各元素之和又大于等于 10 的单元格挑出来。
filtered = [[x for x in row if x % 3 == 0] for row in matrix if sum(row) >= 10]

print(filtered)

# 要读取一份文件并返回每行的字符数。若采用列表推导来做，则需把文件每一行的长度都保存在内存中。如果这个文件特别大，或是通过无休止的 network socket
# （网络套接字）来读取，那么这种列表推导就会出问题。下面的这段列表推导代码，只适合处理少量的输入值。
value = [len(x) for x in open('./test_01.py', encoding='utf-8')]
print(value)

# 列表加一个小括号变成了生成器
it = (len(x) for x in open('./test_01.py', encoding='utf-8'))
print(it)
print(next(it))
print(next(it))

# 如果要把多种手法组合起来，以操作大批量的输入数据，那最好是用生成器表达式来实现。只是要注意：由生成器表达式所返回的那个迭代器是有状态的，用过一轮之后，就不要反复使用了
roots = ((x, x ** 0.5) for x in it)
print(next(roots))
print(next(roots))

"""
总结：1.当输入的数据量较大时，列表推导可能会因为占用太多内存而出问题。
2.由生成器表达式所返回的迭代器，可以逐次产生输出值，从而避免了内存用量问题。
3. 把某个生成器表达式所返回的迭代器，放在另一个生成器表达式的 for 子表达式中，即可将二者组合起来。
4.串在一起的生成器表达式执行速度很快。
"""""
