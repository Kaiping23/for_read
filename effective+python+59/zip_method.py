#! /usr/bin/python python
# -*-coding:utf8-*-
# 2019.11.11 start 1.0.0 version
# __author__ = 'Jordan'

def main():
    """
    
    :return: 
    """""
    # old_method()
    #
    # use_enumerate_method()

    use_zip_method()


def use_zip_method():
    """
    zip的方式:可以平行的遍历多个迭代器，python3中相当于生成器，遍历过程中逐次产生元组，Python2中直接生成好，返回整份列表。
    :return: 
    """""
    names = ['Cecilia', 'Lise', 'Marie']
    letters = [len(n) for n in names]
    # print(letters)
    longest_name = None
    max_letters = 0
    for name, count in zip(names, letters):
        print("name:",name)
        if count > max_letters:
            longest_name = name
            max_letters = count
    print(longest_name)


def use_enumerate_method():
    """
    enumerate方法
    :return: 
    """""
    names = ['Cecilia', 'Lise', 'Marie']
    letters = [len(n) for n in names]
    longest_name = None
    max_letters = 0
    for i, name in enumerate(names):
        count = letters[i]
        if count > max_letters:
            longest_name = name
            max_letters = count
    print(longest_name)


def old_method():
    """
    传统的方法
    :return: 
    """""
    names = ['Cecilia', 'Lise', 'Marie']
    letters = [len(n) for n in names]
    longest_name = None
    max_letters = 0
    for i in range(len(names)):
        count = letters[i]
        if count > max_letters:
            longest_name = names[i]
            max_letters = count
    print(longest_name)


if __name__ == '__main__':

    main()
