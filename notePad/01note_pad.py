import tkinter as tk
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os
def pr():
    print("xxxxxxx")

# 方法写在窗体外面，否则会不断循环
filename = ''
def openfile():
    global filename
    filename = askopenfilename(defaultextension='.txt', filetype=[('文本文件','.txt')]) # 没有name获取路径，而不是文件名
    if filename == '':
        pass
    else:
        win.title("FilePath: " + os.path.basename(filename) + " | Path: " + filename)
        text1.delete(1.0, tk.END)
        f = open(filename, 'r', encoding='utf-8')
        text1.insert(1.0, f.read())
        f.close()
def save():
    global filename
    try:
        f = open(filename, 'w')
        info = text1.get(1.0, tk.END)
        f.write(info)
        f.close()
    except:
        saveas()
def saveas():
    global filename
    filename = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    f = open(filename, 'w')
    info = text1.get(1.0, tk.END)
    f.write(info)
    f.close()
    win.title("FilePath: " + os.path.basename(filename) + " | Path: " + filename)
def new(e):
    global filename
    win.title("未命名文件")
    filename = None
    text1.delete(1.0, tk.END)
def cut():
    text1.event_generate('<<Cut>>')
def copy():
    text1.event_generate('<<Copy>>')
def paste():
    text1.event_generate('<<Paste>>')
def redo():
    try:
        # text1.edit_redo()
        text1.event_generate('<<Redo>>')
    except:
        pass
def undo():
    text1.edit_undo()
def selectAll():
    text1.tag_add('sel','1.0','end')
def setFont():
    def saveClose():
        text1.config(font=(var1.get(), var2.get()))
        fontWin.destroy()
    def close():
        fontWin.destroy()
    fontWin = Toplevel(win)
    fontWin.resizable(False, False)
    fontWin.geometry("280x60")
    fontWin.title("字体设置")
    list1 = ["黑体", "隶书", "宋体", "微软雅黑"]
    Label(fontWin, text="字体：").grid(row=0, column=0, pady=3, padx=3)
    var1 = StringVar()
    Combobox(fontWin, values=list1, textvariable=var1, width=8).grid(row=0, column=1, pady=3, padx=3)
    # list2 = [10, 11, 12, 13, 14, 15, 16, 17]
    list2 = [i for i in range(10, 18)]
    Label(fontWin, text="大小：").grid(row=0, column=2, pady=3, padx=3)
    var2 = IntVar()
    Combobox(fontWin, values=list2, textvariable=var2, width=8).grid(row=0, column=3, pady=3, padx=3)
    Button(fontWin, text="确认", command=saveClose).grid(row=1, column=0, columnspan=2)
    Button(fontWin, text="取消", command=close).grid(row=1, column=3, columnspan=2)

w1 = "0.1"
def find():
    def findall():
        global w1
        con = context.get()
        while True:
            w1 = text1.search(con, w1, "end")
            text1.tag_add("all", w1, w1 + "+" + str(len(con)) + "c")
            text1.tag_config("all", background="red")
            w1 = text1.search(con, w1 + "+" + str(len(con)) + "c", "end")
            if w1 == "":
                w1 = "0.1"
                break
    def findNext():
        global w1
        var1 = context.get()
        if w1 != "": w1 = text1.search(var1, w1, "end")
        if w1 == "":
            showinfo("提示", "没有找到文本")
        else:
            text1.tag_remove("all", "0.1", "end")
            text1.tag_add("all", w1, w1 + "+" + str(len(var1)) + "c")
            text1.tag_config("all", background="red")
            w1 = text1.search(var1, w1 + "+" + str(len(var1)) + "c", "end")
    fontWin = Toplevel(win)
    fontWin.resizable(False, False)
    fontWin.geometry("280x60")
    fontWin.title("查找")
    Label(fontWin, text="查找内容").grid(row=0, column=0, pady=3, padx=3)
    context = tk.Entry(fontWin, width=16)
    context.grid(row=0, column=1, pady=3, padx=3)
    Button(fontWin, text="查找全部", command=findall).grid(row=1, column=0, columnspan=2)
    Button(fontWin, text="查找下一个", command=findNext).grid(row=1, column=3, columnspan=2)

def replace():
    def replaceall():
        global w1
        var1=context.get()
        var2=context0.get()
        w1=text1.search(var1, w1, 'end')
        if w1 == '':
            showinfo("提示","没有找到文本")
        else:
            while True:
                text1.delete(w1, w1 + "+" + str(len(var1)) + "c")
                text1.insert(w1, var2)
                w1 = text1.search(var1, w1 + "+" + str(len(var1)) + "c", "end")
                if w1 == "":
                    w1 = "0.1"
                    break
    def findnext():
        global w1
        var1 = context.get()
        w1=text1.search(var1, w1, "end")
        if w1 == "":
            showinfo("提示", "没有找到文本")
        else:
            text1.tag_add("all", w1, w1 + "+" + str(len(var1)) + "c")
            text1.tag_config("all", background="red")
            w1 = w1 + "+" + str(len(var1)) + "c"
    def replacenext():
        var1 = context.get()
        var2 = context0.get()
        global w1
        if w1 == "":
            pass
        else:
            w1 = w1 + "-" + str(len(var1)) + "c"
            text1.delete(w1, w1 + "+" + str(len(var1)) + "c")
            text1.insert(w1, var2)
    def closerep():
        text1.tag_remove("all", '1.0', 'end')
        fontWin.destroy()
    fontWin = Toplevel(win)
    fontWin.resizable(False, False)
    fontWin.geometry("280x120")
    fontWin.title("查找")
    Label(fontWin, text="查找内容").grid(row=0, column=0, pady=3, padx=3)
    context = tk.Entry(fontWin, width=16)
    context.grid(row=0, column=1, pady=3, padx=3)
    Label(fontWin, text="替换内容").grid(row=1, column=0, pady=3, padx=3)
    context0 = tk.Entry(fontWin, width=16)
    context0.grid(row=1, column=1, pady=3, padx=3)
    Button(fontWin, text="替换全部", command=replaceall).grid(row=0, column=3, sticky='e', padx=40)
    Button(fontWin, text="查找下一个", command=findnext).grid(row=1, column=3, sticky='e', padx=40)
    Button(fontWin, text="查找下一个", command=replacenext).grid(row=2, column=3, sticky='e', padx=40)
    Button(fontWin, text="取消", command=closerep).grid(row=3, column=3, sticky='e', padx=40)

win = tk.Tk()
win.geometry('600x600')
menu1 = tk.Menu(win)  # 创建
menu1_1_2 = tk.Menu(menu1, tearoff=False)  # 第一个文件的二级菜单
menu1_1_3 = tk.Menu(menu1, tearoff=False)
menu1_1_4 = tk.Menu(menu1, tearoff=False)
menu1.add_cascade(label="文件(F)", menu=menu1_1_2)  # 添加  cascade菜单语句
menu1.add_cascade(label="编辑(E)", menu=menu1_1_3)
menu1.add_cascade(label="格式(O)", menu=menu1_1_4)

list1 = ["新窗口", "打开", "保存", "另存为", "退出"]
list2 = ["Ctrl+N", "Ctrl+O", "Ctrl+S", "Ctrl+W", "Ctrl+P"]
for i in range(len(list1)):
    if list1[i] == "打开":
        menu1_1_2.add_command(label=list1[i], accelerator=list2[i], command=openfile)
    elif list1[i] == "保存":
        menu1_1_2.add_command(label=list1[i], accelerator=list2[i], command=save)
    elif list1[i] == "另存为":
        menu1_1_2.add_command(label=list1[i], accelerator=list2[i], command=saveas)
    elif list1[i] == "新建":
        menu1_1_2.add_command(label=list1[i], accelerator=list2[i], command=lambda:new(1))
    else:
        menu1_1_2.add_command(label=list1[i], accelerator=list2[i])

list1 = ["复制", "粘贴", "剪切", "重做", "撤回", "查找", '全选', '字体', '替换']
list2 = ["Ctrl+Z", "Ctrl+X", "Ctrl+C", "", "", "Ctrl+F", '', '', '']
for i in range(len(list1)):
    if list1[i] == "复制":
        menu1_1_3.add_command(label=list1[i], accelerator=list2[i], command=copy)
    elif list1[i] == "粘贴":
        menu1_1_3.add_command(label=list1[i], accelerator=list2[i], command=paste)
    elif list1[i] == "剪切":
        menu1_1_3.add_command(label=list1[i], accelerator=list2[i], command=cut)
    elif list1[i] == "重做":
        menu1_1_3.add_command(label=list1[i], accelerator=list2[i], command=redo)
    elif list1[i] == "撤回":
        menu1_1_3.add_command(label=list1[i], accelerator=list2[i], command=undo)
    elif list1[i] == "查找":
        menu1_1_3.add_command(label=list1[i], accelerator=list2[i], command=find)
    elif list1[i] == "替换":
        menu1_1_3.add_command(label=list1[i], accelerator=list2[i], command=replace)
    elif list1[i] == "全选":
        menu1_1_3.add_command(label=list1[i], accelerator=list2[i], command=selectAll)
        menu1_1_3.add_separator()
    elif list1[i] == "字体":
        menu1_1_3.add_command(label=list1[i], accelerator=list2[i], command=setFont)
    # if list1[i] == "复制":
    #     menu1_1_3.add_command(label=list1[i], accelerator=list2[i], command=copy)
    else: menu1_1_3.add_command(label=list1[i], accelerator=list2[i])

list1 = ["放大", "状态", "换行"]
for i in range(len(list1)):
    menu1_1_4.add_command(label=list1[i])

text1 = tk.Text(win, undo=True)
text1.pack(fill=tk.BOTH, expand=tk.YES, side='left')
scroll = tk.Scrollbar(win) # 这个要展开才有，它有最小宽度
scroll.pack(fill=tk.Y, side='left')
scroll.configure(command=text1.yview)
text1.configure(yscrollcommand=scroll.set)

win.bind('<Control-n>', new)
# win.bind('<Control-o>', openfile)

win.configure(menu=menu1)  # 显示
win.mainloop()

