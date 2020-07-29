# coding=utf-8
"""
猫狗队列
宠物，狗，猫的类如下：
...
实现一种狗猫队列的结构，要求如下：
用户可以调用add方法将cat类或dog类的实例放入队列中；
用户可以调用pollAll方法，将队列中所有的实例按照进队列的先后顺序依次弹出；
用户可以调用pollCat方法，将队列中的cat类的实例按照进队列的先后顺序依次弹出；
用户可以调用isEmpty方法，检查队列中是否还有dog或cat的实例；
用户可以调用isDogEmpty方法，检查队列中是否有dog类的实例；
用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例
"""

class Pet:
    type = ""
    def __init__(self, type):
        self.type = type

    def getPetType(self):
        return self.type

class Dog(Pet):
    def __init__(self):
        super("dog")

class Cat(Pet):
    def __init__(self):
        super("cat")

class PetQueue:
    dog_array, cat_array, index = [], [], 0

    def add(self, pet):
        if pet.type == "dog":
            self.dog_array.append((pet, self.index))
        else:
            self.cat_array.append((pet, self.index))
        self.index += 1

    def pollAll(self):
        pets = []
        while self.dog_array and self.cat_array:
            dog, dog_index = self.dog_array.pop(0)
            cat, cat_index = self.cat_array.pop(0)
            if dog_index < cat_index:
                pets.append(dog)
            else:
                pets.append(cat)

        while self.dog_array:
            dog, dog_index = self.dog_array.pop(0)
            pets.append(dog)

        while self.cat_array:
            cat, cat_index = self.cat_array.pop(0)
            pets.append(cat)
        return pets

    def pollDog(self):
        return [self.dog_array.pop(0)[0] for i in range(len(self.dog_array))]

    def pollCat(self):
        return [self.cat_array.pop(0)[0] for i in range(len(self.cat_array))]

    def isEmpty(self):
        return len(self.dog_array) == 0 and len(self.cat_array) == 0

    def isDogEmpty(self):
        return len(self.dog_array) == 0

    def isCatEmpty(self):
        return len(self.cat_array) == 0

