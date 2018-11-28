#!/usr/bin/env python

import random, string


def gen_random_num_str():
    s = string.ascii_letters + string.digits
    print(s)
    n = {''.join(random.choices(s, k=8)) for i in range(60000)}
    type1 = type(n)
    print("n的类型是：", type1)
    print("n的长度是：", len(n))
    print(len(n))
    with open('a.csv', 'w') as f:
        for i in n:
            # 默认换行print(i, end='\r'),不换行就是：print(i,end='')
            print(i, end='-')
            f.write(i + '\n')


if __name__ == '__main__':
    gen_random_num_str()

# import itertools
#
#
# def gen_register_code():
#     """Generate the registration code randomly"""
#     mylist = ("".join(x) for x in
#               itertools.product("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=8))
#     for i in range(60000):
#         print(next(mylist))
#
#
# if __name__ == "__main__":
#     gen_register_code()
