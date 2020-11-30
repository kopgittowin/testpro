#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）'''


class Animal:
    name: str = 'Animal Name'
    color: str = 'default Color'
    age: float = 0
    gender: str = 'null'

    def __init__(self, name, color, age, gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def Call(self):
        print(f'{self.name} is Calling ')

    def Run(self):
        print(f'{self.name} is Runing ')


'''创建子类【猫】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=短毛，
添加一个新的方法， 会捉老鼠，
复写父类的‘【会叫】的方法，改成【喵喵叫】
调用 name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。'''


class Cat(Animal):
    hair: str = 'short'
    b_or_g: str

    def __init__(self, name, color, age, gender, hair):

        self.hair = hair
        super().__init__(name, color, age, gender)
        # print('构造函数执行')
        if self.gender == 'female':
            b_or_g = 'girl'
        else:
            b_or_g = 'boy'
        print(f'the cat {self.name} ,is a {b_or_g},{self.age} years old,'
              f'it is {self.color},it has {self.hair} hair ')

    def Call(self):
        print(f'{self.name} is meowing ')

    def Catch(self):
        print(f'{self.name} has catch a mouse ')


'''创建子类【狗】，继承【动物类】，
复写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发=长毛，
添加一个新的方法， 会看家，
复写父类的【会叫】的方法，改成【汪汪叫】
调用 name== ‘main’：
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】。
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】'''


class Dog(Animal):
    hair: str = 'long'
    b_or_g: str

    def __init__(self, name, color, age, gender, hair):

        self.hair = hair
        super().__init__(name, color, age, gender)
        # print('构造函数执行')
        if self.gender == 'female':
            b_or_g = 'girl'
        else:
            b_or_g = 'boy'
        print(f'the dog {self.name} ,is a {b_or_g},{self.age} years old,'
              f'it is {self.color},it has {self.hair} hair ')

    def Call(self):
        print(f'{self.name} is barking ')

    def Watch(self):
        print(f'{self.name} can watch the house ')


if __name__ == '__main__':
    C_cat1 = Cat('kitty', 'white', 5, 'female', 'long')
    C_cat1.Call()
    C_cat1.Catch()
    D_dog1 = Dog('Rocky', 'yellow', 3, 'male', 'short')
    D_dog1.Call()
    D_dog1.Watch()
