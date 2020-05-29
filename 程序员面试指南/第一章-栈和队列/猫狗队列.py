# coding=utf-8
'''
实现一种狗猫队列的的结构，要求如下：
* 用户可以调用add方法将cat类或dog类的实例放入队列中
* 用户可以调用pollAll方法，将队列中所有的实例按照进队列的先后顺序依次弹出
* 用户可以调用pollDog方法，将队列中dog类的实例按照进队列的先后顺序依次弹出
* 用户可以调用pollCat方法，将队列中cat类的实例按照进队列的先后顺序依次弹出
* 用户可以调用isEmpty方法，检查队列中是否还有dog或cat的实例
* 用户可以调用isDogEmpty方法，检查队列中是否有dog类的实例
* 用户可以调用isCatEmpty方法，检查队列中是否有cat类的实例
'''
class Pet:
    def __init__(self, type):
        self.type = type

    def getPetType(self):
        return self.type


class Dog(Pet):
    def __init__(self):
        super().__init__("Dog")


class Cat(Pet):
    def __init__(self):
        super(Cat, self).__init__("Cat")


class PetEnterqQueue:
    def __init__(self, pet, index):
        self.pet = pet
        self.index = index

    def getPet(self):
        return self.pet

    def getIndex(self):
        return self.index

    def getEnterPetType(self):
        return self.pet.getPetType()


class DogCatQueue:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.index = 0

    def add(self, pet):
        if pet.getPetType() == "Dog":
            self.dog_queue.append(PetEnterqQueue(pet, self.index))
        else:
            self.cat_queue.append(PetEnterqQueue(pet, self.index))
        self.index += 1

    def pollAll(self):
        if self.dog_queue or self.cat_queue:
            if self.dog_queue[0].getIndex() < self.cat_queue[0].getIndex():
                return self.dog_queue.pop(0).getPet()
            else:
                return self.dog_queue.pop(0).getPet()
        elif self.dog_queue:
            return self.dog_queue.pop(0).getPet()
        elif self.cat_queue:
            return self.dog_queue.pop(0).getPet()
        else:
            raise Exception("queue is empty")

    def pollDog(self):
        if self.dog_queue:
            return self.dog_queue[0].getPet()
        else:
            raise Exception("queue is empty")

    def pollCat(self):
        if self.cat_queue:
            return self.cat_queue[0].getPet()
        else:
            raise Exception("queue is empty")

    def isempty(self):
        return not self.dog_queue and not self.cat_queue

    def isDogQueueEmpty(self):
        return not self.dog_queue

    def isCatQueueEmpty(self):
        return not self.cat_queue





















