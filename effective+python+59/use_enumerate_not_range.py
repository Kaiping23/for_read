#! /usr/bin/python python
# -*-coding:utf8-*-
# 2019.11.11 start 1.0.0 version
# __author__ = 'ping'
from random import randint


def main():
    """
    尽量用enumerate而不使用range

    :return:
    """""
    # rang_method()
    for_test()


def rang_method():
    """
    虽然range方法很好用。
    :return: 
    """""
    random_bits = 0
    for i in range(64):
        ac = randint(0, 1)
        if ac:
            print("ac:", ac)
            random_bits |= 1 << i
            print(random_bits)
        else:
            print("ac:", ac)
            print("-------------")


def for_test():
    flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
    for flavor in flavor_list:
        print('{} is delicious'.format(flavor))

    # 原来这样做的：

    for i in range(len(flavor_list)):
        flavor = flavor_list[i]
        print('{}:{}'.format(i + 1, flavor))

    # 现在这样
    for i, flavor in enumerate(flavor_list):
        print("{}:{}".format(i + 1, flavor))

    # 也可以这样
    for i, flavor in enumerate(flavor_list, 10):
        print("{}:{}".format(i, flavor))


if __name__ == '__main__':
    """
    enumerate函数提供了一种精简的写法，可以在便利迭代器时获得索引。
    可以给enumerate提供第二个参数，替代range与小标访问相结合的序列.
    """""
    main()
