#-*- coding:utf-8 -*-
"""一些生成器方法，生成随机数，手机号，以及连续数字等"""

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from utils.config import DATA_PATH

import random
from faker import Factory

fake = Factory().create('en_US')

def random_phone_number():
    return fake.phone_number()

def random_name():
    return fake.name()

def random_address():
    return fake.address()

def random_email():
    return fake.email()

def random_ipv4():
    return fake.ipv4()

def random_str(min_chars=0, max_chars=8):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)

def factory_generate_ids(starting_id=1, increment=1):
    """返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment."""
    def generate_started_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment
    return generate_started_ids

def factory_choice_generator(values):
    """返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。"""
    def choice_generator():
        my_list = list(values)
        while True:
            yield random.choice(my_list)
    return choice_generator


if __name__ == '__main__':
    f = open(DATA_PATH + '\\data.txt', 'w')

    print(random_name(),random_address(),random_email(),random_ipv4(),random_str(min_chars=6, max_chars=8))
    for i in range(1, 12):
        AreaCode = ['+84','+86','+852','+81','+82','+65','+886','+1']
        choice_AreaCode = next(factory_choice_generator(AreaCode)())
        UserType = ['AgentAdmin','AgentUser','VHAccountant','VHAgencyManager','VHUser']
        choice_UserType = next(factory_choice_generator(UserType)())
        data = random_name() +' ,  '+  choice_AreaCode + ' ,  '+ random_email() + '  , '+ random_phone_number() + '  , '+ choice_UserType
        f.write(data)
        f.write("\n")
    f.close()

"""
    id_gen = factory_generate_ids(starting_id=0, increment=2)()
    for i in range(5):
        print(next(id_gen))

    choices = ['John', 'Sam', 'Lilly', 'Rose']
    choice_gen = factory_choice_generator(choices)()
    for i in range(5):
        print(next(choice_gen))
"""    
