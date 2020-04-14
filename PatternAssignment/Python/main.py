import abc

class BreakfastMenu: #list representation
     #creation of list
    breakfastM = []


    def __init__(self, name, price, gf):
        self.name = name
        self.price = price
        self.gf = gf
        self.__class__.breakfastM.append(self)




class LunchMenu: 
    pass




class Iteratable: #creates the iterator obj
    def __init__(self, VALUE):
        self.VALUE = VALUE

    def __iter__(self):
        return Iterator(self.VALUE)


class Iterator: #traverses a structure
    def __init__(self, VALUE):
        self.VALUE = VALUE
        self.index = 0
    
    def __iter__(self):
        return self


    def __next__(self):
        if CONDITION:
            VALUE = self.VALUE
            self.index = self.index + 1
            return VALUE
        else:
            raise StopIteration()
        


item_1 = BreakfastMenu("Eggs", 2, True)
item_2 = BreakfastMenu("Pancakes", 4, False)
item_3 = BreakfastMenu("Fruit Cup", 3, True)

