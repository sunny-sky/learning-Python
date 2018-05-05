#一个矩形类
#若为square属性赋值，那么说明是正方形，值就是正方形的边长，宽高相等

class Rectangle:
    def __init__(self,width=0,height=0):
        self.width = width
        self.height = height

    def __setattr__(self,name,value):
        if name == 'square':
            self.width = value
            self.height = value
        else:
            #self.__dict__[name] = value   也行
            super().__setattr__(name,value)

    def getArea(self):
        return self.width * self.height
