# 添加 删除
import sqlite3
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from tkinter.filedialog import *

import traceback

class window:
    def __init__(self, win):  # 立即执行
        # print("iniit" + str(win))
        # if win != None: #  父类第一次加载的时候没有值
        self.win = win
        self.panel1 = Frame(win)
        self.panel2 = Frame(win)
        self.panel1.grid(row=0, column=0)
        self.panel2.grid(row=10, column=0)

        self.initUI()

    def initUI(self):  # 不是立即执行
        win = self.panel1
        self.entry0 = Entry(win, width=20)
        self.entry1 = Entry(win, width=20)
        self.dview = Treeview(win, columns=('id', 'name'), show='headings')
        self.choice = ['test.db', 'test0.db', 'test1.db']
        self.comboVar = StringVar()
        self.comboTVar = StringVar()
        self.combo = Combobox(win, textvariable=self.comboVar, values=self.choice, width=10)
        self.comboT = Combobox(win, textvariable=self.comboTVar, width=10)
        self.conn = sqlite3.connect("test.db")  # 自动在当前目录下建立库
        self.cursor = self.conn.cursor()  # 创建游标对象
        self.var3 = self.cursor.fetchall()
        self.menu = Menu(win)
        p2 = self.panel2
        self.text = Text(p2)
        self.labels = []
        self.entries = []

class db(window):
    def __init__(self, win, dbName='test.db', tableName='user'):  # __init__方法里面加载不到
        super().__init__(win)
        self.dbName = dbName
        self.tableName = tableName
        print(4)
        self.ini()

    def ini(self):
        self.UI(self.panel1, self.entry0, self.entry1, self.dview, self.combo, self.comboVar,\
                self.menu)
        self.data()

    def updateTable(self, tableName):
        global cursor
        dview = self.dview
        var = cursor.execute("select * from " + tableName)
        for i in dview.get_children():
            dview.delete(i)
        for i in var:
            dview.insert('', END, value=i)

    def adddata(self):
        global conn, cursor, var3
        # entry0 = self.entry0;
        # entry1 = self.entry1;
        dview = self.dview
        print(self.entries)
        print([i.get() for i in self.entries])
        if "" in [i.get() for i in self.entries]:
            showinfo("空", "插入数据不能为空")
        else:
            data = tuple([i.get() for i in self.entries])
            str = ""
            for i in self.entries: str += ", ?"
            cursor.execute("insert into " + self.tableName + " values (" + str[1:] + ")", data)
            conn.commit()
            var = cursor.execute("select * from " + self.tableName)
            for i in dview.get_children():
                dview.delete(i)
            for i in var:
                dview.insert('', END, value=i)


    def update(self):

        dview = self.dview;
        win = self.win;
        # entry0 = self.entry0
        if dview.focus() == '':  # ！！！！！！！！！！！！！！！！！！！！
            showerror('提示', "您未选择行")
        else:
            def updatedata():
                print(self.updateEntry.__str__())
                data = [i.get() for i in self.updateEntry]
                data.append(self.d_id)
                # data[-1], data[0] = data[0], data[-1]
                data = tuple(data)
                print(data)
                str = ""
                for i in self.labels:
                    if i.cget("text") != "id": str += i.cget("text") + "=?, "
                cursor.execute("update " + self.tableName + " set " + str[0 : -2] + " where id=?",
                               data)  # id值不允许改变，所以不能获取值
                conn.commit()
                self.updateTable(self.tableName)
                smwin.destroy()

            values = dview.focus()

            smwin = Toplevel(win)
            smwin.geometry(f"+300+400")
            d_id = dview.item(values)['values'][0]
            # Label(smwin, text="名字").grid(row=0, column=2)
            # entry1 = Entry(smwin, width=20)
            # entry0.grid(row=0, column=1)
            # entry1.grid(row=0, column=3)
            index = 0
            # for i in self.entries:
            #     index += 2
            #     i.grid(row=0, column=index)
            self.updateLabel = []
            self.updateEntry = []
            index = 0
            for i in self.labels:
                if index == 0:
                    self.d_id = dview.item(values)['values'][0]
                    Label(smwin, text="编号" + " " + str(self.d_id)).grid(row=0, column=0)
                    index += 2
                else:
                    entry0 = Entry(smwin, width=10)
                    entry0.grid(row=0, column=index + 1)
                    entry0.insert(0, (dview.item(values)['values'][int(index/2)]))
                    self.updateEntry.append(entry0)
                    l = Label(smwin, text=i.cget("text"))
                    l.grid(row=0, column=index)
                    self.updateLabel.append(l)
                    index += 2
            Button(smwin, text="确认修改", command=updatedata).grid(row=0, column=index+2)

    def delete(self):
        global cursor, conn
        dview = self.dview
        values = dview.selection()
        key = askokcancel('确认', '确认删除?')
        if key:
            for i in values:
                cursor.execute("delete from " + self.tableName + " where id=?", (dview.item(i)['values'][0],))
            conn.commit()
            self.updateTable()

    def inSwitch(self, tableName):
        global conn, cursor, var3
        cursor = conn.cursor()  # 创建游标对象
        try:
            cursor.execute('select * from ' + tableName)
        except:
            cursor.execute('create table user (id int(16) primary key, name varchar(20))')
            cursor.execute('insert into user(id, name) values (1,"hyh")')
            cursor.execute('insert into user(id, name) values (?,?)', (2, "hyhsw"))
            cursor.execute('insert into user(id, name) values (3,?)', ("hyhsw",))
            conn.commit()
            self.tableName = "user"

        var3 = cursor.fetchall()
        print(var3)
        self.updateViewColumn()
        self.updateTable(tableName)

    def switch(self, e):
        comboVar = self.comboVar
        global conn, cursor, var3
        conn = sqlite3.connect(comboVar.get())  # 自动在当前目录下建立库
        self.dbName = comboVar.get()
        self.comboT.config(value=self.search_tables(self.dbName))
        self.inSwitch(self.tableName)

    def switchTreeView(self, e):
        global conn, cursor, var3
        i = self.tree.selection()
        tree = self.tree
        p_i = tree.parent(i)
        text = tree.item(p_i, "text")
        text0 = tree.item(i, "text")
        if text0[-2:len(text0)] == "db":
            print(text0)
            self.dbName = text0
            conn = sqlite3.connect(text0)
        if text[-2:len(text)] == "db":
            print(text)
            self.dbName = text
            conn = sqlite3.connect(text)
            print(tree.item(i, "text"))
            self.tableName = tree.item(i, "text")
            self.inSwitch(tree.item(i, "text"))

    def newDB(self):
        global conn
        name = asksaveasfilename(initialfile='未命名.db', defaultextension='.db')
        conn = sqlite3.connect(name)
        self.choice.append(name.split("/")[-1])
        self.updateTree()

    def openDB(self):
        global conn
        name = askopenfilename(filetype=[('sqliteDB', '.db')], defaultextension='.db')
        conn = sqlite3.connect(name)
        if name.split("/")[-1] not in self.choice:
            self.choice.append(name.split("/")[-1])
            self.updateTree()

    def UI(self, win, entry0, entry1, dview, combo, comboVar, menu1):
        print(2)
        menu1_1 = Menu(menu1, tearoff=False)
        menu1_1.add_command(label="新数据库", accelerator="Ctrl+N", command=self.newDB)
        menu1_1.add_command(label="打开数据库", command=self.openDB)
        menu1_1.add_separator()
        menu1.add_cascade(label="File", menu=menu1_1)
        self.win.config(menu=menu1)
        var3 = self.var3
        # Label(win, text="编号").grid(row=0, column=0 + 1)
        # Label(win, text="名字").grid(row=0, column=2 + 1)
        # entry0.grid(row=0, column=1 + 1)
        # entry1.grid(row=0, column=3 + 1)
        self.add = Button(win, text="添加数据", command=self.adddata)
        self.add.grid(row=0, column=4 + 1)
        self.dele = Button(win, text="删除数据", command=self.delete)
        self.dele.grid(row=3, column=4 + 1)
        self.upd = Button(win, text="修改数据", command=self.update)
        self.upd.grid(row=3, column=3 + 1, sticky=E)  # 弹出用户子窗口  stiky=E

        self.updateViewColumn()
        # dview.heading('id', text='编号')  # 程序内名，用户显示名
        # dview.heading('name', text='名字')
        dview.grid(row=1, column=0 + 1, columnspan=5)
        for i in var3:
            dview.insert('', END, values=i,
                         image=PhotoImage(file="Sample.gif"))  # 多个值（元组）   (根)节点,位置,值,image图标栏图片,text=图标栏内容
        comboVar.set(self.dbName)
        combo.grid(row=3, column=0 + 1, columnspan=2, sticky=W)
        combo.bind("<<ComboboxSelected>>", self.switch)
        self.comboT.grid(row=3, column=3, sticky=W)
        self.comboT.config(value=self.search_tables(self.dbName))
        self.comboT.bind("<<ComboboxSelected>>", lambda e: self.inSwitch(self.comboTVar.get()))
        self.tree = Treeview(win, show='tree headings', height=13)
        self.updateTree()

        self.text.grid(row=0, column=0)
        self.text.bind("<Return>", self.textBox)

    def textBox(self, e):
        dbName = self.dbName
        text1 = self.text
        textBegin = int(text1.index(END).split(".")[0]) - 1
        t1 = text1.get(str(textBegin) + '.0', END)  # 或者获取当前光标位置到行末尾
        conn = sqlite3.connect(dbName)
        cursor = conn.cursor()
        try:
            cursor.execute(t1)
            a = t1[0:3]
            if a == 'sel':
                text1.insert(END, "\n" + str(cursor.fetchall()))
            elif a == "upd" or a == "del" or a == "ins":
                conn.commit()
                text1.insert(END, "\n" + str("success"))
                self.updateTable(self.tableName)
            elif a == "cre":
                text1.insert(END, "\n" + str("success"))
                self.updateTree()
            else:
                text1.insert(END, "\n" + str("不支持的操作"))
        except:
            text1.insert(END, "\n" + str(traceback.format_exc(chain=False).split("\n")[-2]))

    def updateViewColumn(self):
        dview = self.dview
        conn = sqlite3.connect(self.dbName)
        cursor = conn.cursor()
        cursor.execute("pragma table_info(" + self.tableName + ")")
        lt = cursor.fetchall()
        columnName = []
        [i for i in map(lambda i: i.destroy(), self.labels)]
        [i for i in map(lambda i: i.destroy(), self.entries)]
        self.labels = []
        self.entries = []
        self.panel1.update()
        index = 1
        for i in lt:
            columnName.append(i[1])
            l = Label(self.panel1, text=i[1])
            l.grid(row=0, column=index)
            self.labels.append(l)
            entry0 = Entry(self.panel1, width=10)
            entry0.grid(row=0, column=index + 1)
            self.entries.append(entry0)
            index += 2
        dview.config(column=columnName)
        dview.grid(columnspan=(len(columnName) * 2 + 1))
        for i in columnName:
            dview.heading(i, text=i)
        self.add.grid(column=(len(columnName) * 2 + 1))
        self.dele.grid(column=(len(columnName) * 2 + 1))
        self.upd.grid(column=(len(columnName) * 2))

    def updateTree(self):
        tree = self.tree
        for i in tree.get_children():
            tree.delete(i)
        s_f = tree.insert('', END, text="库名")
        for i in self.choice:
            s_s_f = tree.insert(s_f, END, text=i)
            for j in self.search_tables(i):
                tree.insert(s_s_f, END, text=j)
        tree.bind('<ButtonRelease-1>', self.switchTreeView)
        tree.grid(row=0, column=0, rowspan=4, sticky=N)
        self.combo.config(values=self.choice)

    def search_tables(self, tableName):
        new_conn = sqlite3.connect(tableName)
        new_cursor = new_conn.cursor()
        # Query the "sqlite_master" table to get the list of all tables
        new_cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = new_cursor.fetchall()

        # Print the list of tables
        for table in tables:
            print(table[0])

        return tables


    def data(self):
        global conn, cursor, var3
        conn = sqlite3.connect(self.dbName)  # 自动在当前目录下建立库
        cursor = conn.cursor()  # 创建游标对象
        try:
            cursor.execute('select * from user')
        except:
            cursor.execute('create table user (id int(16) primary key, name varchar(20))')
            cursor.execute('insert into user(id, name) values (1,"hyh")')
            cursor.execute('insert into user(id, name) values (?,?)', (2, "hyh"))
            cursor.execute('insert into user(id, name) values (3,?)', ("hyh",))
            conn.commit()

        var3 = cursor.fetchall()
        self.updateViewColumn()
        self.updateTable(self.tableName)

    def __add__(self, tableName):
        self.choice.append(tableName)

    def __next__(self, choice):
        if self.index == len(choice) - 1:
            raise StopIteration  # 停止迭代器异常：不再往下迭代
        self.index += 1
        return self.choice[self.index]


if __name__ == '__main__':
    win = Tk()
    # window(win)
    db(win)  # 对父类的继承会导致父类__init__的运行，不需要手动执行
    win.mainloop()
