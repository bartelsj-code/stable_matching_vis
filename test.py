class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return "Cat ({} age: {})".format(self.name, self.age)

    def __lt__(self, other_cat):
        return self.age < other_cat.age
            
def main():
    lst = []
    ages = [6,23,34,4324,142,61234,23,342,21,423,4,432,1242,32,4243,42,323,41234]
    g = 0
    for i in "asdhfasdhf":
        c = Cat(i, ages[g])
        lst.append(c)
        g += 1
    lst.sort()
    print(lst)
main()