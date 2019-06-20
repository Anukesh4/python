class Basic:
    def __init__(self,name):
        self.name=name
    def show(self):
        print ('Basic--name:%s'%self.name)
obj1=Basic('Anukesh')
obj1.show()
dir(Basic)
dir(obj1)
