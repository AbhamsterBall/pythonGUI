# class father():
#     def __init__(self):
#         attr = 1;
# class child(father):
#     def __init__(self):
#         super(child, self).__init__()
#         print(self.attr)
# if __name__ == '__main__':
#     child().__init__()
# class Cat:
#     def __init__(self):
#         self.name="猫"
#         self.age=4
#         self.info=[self.name,self.age]
# #self.__info=[self.name,self.age] #私有属性不能被子类继承
#         self.index=-1
#     def run(self): #实例方法
#         print(self.name,"在跑动")
#     def getName(self):
#         return self.name
# class Bosi(Cat):
#     def setName(self,newName):
#         self.name=newName #子类中的属性改变 父类的属性不改变 __init__自动调用
#     def eat(self):
#         print(self.name,"在吃东西")
#         print(self.age)
#
# if __name__ == '__main__':
#     bs = Bosi()
#     print(bs.name)
#     print(bs.age)
#     bs.run()
#     bs.setName("加菲猫")
#     bs.eat()
#     print(bs.info)  # 报错
#     print(bs.name)
import tkinter as tk

class MyGUI:
    def __init__(self, root):
        self.labels = []
        self.entries = []

        for i in range(5):
            label = tk.Label(root, text=f"Label {i}")
            label.pack()
            self.labels.append(label)

            entry = tk.Entry(root)
            entry.pack()
            self.entries.append(entry)

        update_button = tk.Button(root, text="Destroy and Update", command=self.destroy_and_update)
        update_button.pack()

    def destroy_and_update(self):
        # 销毁标签
        # for label in self.labels:
        #     label.destroy()
        #
        # # 销毁输入框
        # for entry in self.entries:
        #     entry.destroy()
        [i for i in map(lambda i: i.destroy(), self.labels)]
        [i for i in map(lambda i: i.destroy(), self.entries)]

        # 更新界面
        root.update_idletasks()  # 更新界面

root = tk.Tk()
my_gui = MyGUI(root)
root.mainloop()


