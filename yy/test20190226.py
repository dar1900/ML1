class Apple(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __getattr__(self, name):
        return self.name

    def __setattr__(self, name, value):
        self.__dict__[name] = 'apple - {}'.format(value)


a = Apple('A', '20g')
print(a.__dict__)
print(a.name,'*'*10,a.size)