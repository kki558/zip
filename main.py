import zipfile
from tkinter import *
from tkinter.ttk import *
from typing import Dict
import threading
import os
from base64 import b64decode
from PIL import ImageTk


class WinGUI(Tk):

    widget_dic: Dict[str, Widget] = {}

    def __init__(self):
        super().__init__()
        self.__win()
        self.widget_dic["tk_input_lke01dom"] = self.__tk_input_lke01dom(self)
        self.widget_dic["tk_button_lke02cnq"] = self.__tk_button_lke02cnq(self)
        self.widget_dic["tk_button_lke02oqt"] = self.__tk_button_lke02oqt(self)
        self.widget_dic["tk_input_lke037ny"] = self.__tk_input_lke037ny(self)
        self.widget_dic["tk_label_lke03z9i"] = self.__tk_label_lke03z9i(self)
        self.widget_dic["tk_text_lknwfu7d"] = self.__tk_text_lknwfu7d(self)

    def __win(self):
        icon_img = b'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'
        icon_img = b64decode(icon_img)
        icon_img = ImageTk.PhotoImage(data=icon_img)
        # print(icon_img)
        self.title("zip爆破")
        # 设置窗口大小、居中
        width = 599
        height = 472
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height,
                                    (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)
        self.iconphoto(True, icon_img)
        # 自动隐藏滚动条

    def scrollbar_autohide(self, bar, widget):
        self.__scrollbar_hide(bar, widget)
        widget.bind("<Enter>", lambda e: self.__scrollbar_show(bar, widget))
        bar.bind("<Enter>", lambda e: self.__scrollbar_show(bar, widget))
        widget.bind("<Leave>", lambda e: self.__scrollbar_hide(bar, widget))
        bar.bind("<Leave>", lambda e: self.__scrollbar_hide(bar, widget))

    def __scrollbar_show(self, bar, widget):
        bar.lift(widget)

    def __scrollbar_hide(self, bar, widget):
        bar.lower(widget)

    def vbar(self, ele, x, y, w, h, parent):
        sw = 15  # Scrollbar 宽度
        x = x + w - sw
        vbar = Scrollbar(parent)
        ele.configure(yscrollcommand=vbar.set)
        vbar.config(command=ele.yview)
        vbar.place(x=x, y=y, width=sw, height=h)
        self.scrollbar_autohide(vbar, ele)

    def __tk_input_lke01dom(self, parent):
        global ipt
        ipt = Entry(parent, )
        ipt.place(x=100, y=80, width=400, height=30)
        return ipt

    def __tk_button_lke02cnq(self, parent):
        btn = Button(parent, text="开始爆破", takefocus=False,)
        btn.place(x=100, y=170, width=123, height=30)
        return btn

    def __tk_button_lke02oqt(self, parent):
        btn = Button(parent, text="退出程序", takefocus=False,)
        btn.place(x=370, y=170, width=131, height=30)
        return btn

    def __tk_input_lke037ny(self, parent):
        global ipt1
        ipt1 = Entry(parent, )
        ipt1.place(x=100, y=120, width=399, height=30)
        return ipt1

    def __tk_label_lke03z9i(self, parent):
        label = Label(parent, text="Copyright kki558.", anchor="center", )
        label.place(x=0, y=440, width=130, height=30)
        return label

    def __tk_text_lknwfu7d(self, parent):
        global text
        text = Text(parent)
        text.place(x=100, y=240, width=401, height=156)
        self.vbar(text, 100, 240, 401, 156, parent)
        return text


class Win(WinGUI):

    def __init__(self):
        super().__init__()
        self.__event_bind()
        text.tag_config("error", foreground="red")
        text.tag_config("success", foreground="green")
        text.tag_config("wor", foreground="orange")
        ipt.insert(0, "请输入压缩包路径")
        ipt1.insert(0, "请输入密码词典路径")
        ipt.configure(foreground="gray")
        ipt1.configure(foreground="gray")
        text.config(state="normal")

    def start_zip(self, evt):
        # inputa = ipt.get()
        inputa = ipt.get()
        # print(inputa)

        passwords = ipt1.get()
        # print(inputa, "\n", passwords)
        text.insert("end", "[Info] Start cracking the package.\n")
        if inputa == "" or inputa == "请输入压缩包路径":
            text.insert("end", "[Error] The package path cannot be empty.\n", "error")
        elif not os.path.exists(inputa):
            text.insert("end", "[Error] Package path is invalid.\n", "error")
        
        if passwords == "" or passwords == "请输入密码词典路径":
            text.insert("end", "[Error] The password dictionary path cannot be empty\n", "error")
        elif not os.path.exists(passwords):
            text.insert("end", "[Error] Password dict path is invalid.\n", "error")

        if inputa != "" and inputa!= "请输入压缩包路径" and passwords != "" and passwords != "请输入密码词典路径" and os.path.exists(inputa) and os.path.exists(passwords):
            t = threading.Thread(target=self.crack_zip, args=(inputa, passwords))
            t.daemon = True
            t.start()
        text.see(END)

    def crack_zip(self, inputa, passwords):
        zip_file = zipfile.ZipFile(inputa)
        with open(passwords, "r", encoding="utf-8") as f:
            abcd = f.read()
            pwds = abcd.splitlines()
            # print(pwds)
        for pwd in pwds:

            try:
                zip_file.extractall(pwd=bytes(pwd, "utf-8"))
                text.insert(
                    "end", f"[Info] Success with passdord: {pwd}\n", "success")
                # print(f"[Info] Success with passdord: {pwd}")
                break
            except:
                text.insert(
                    "end", f"[Info] Failed with password: {pwd}\n", "wor")
                # print(f"[Info] Failed with password: {pwd}", "error")
            text.see(END)
        text.insert("end", "All passwords are invalid.", "wor")
        print("All passwords are invalid.")

    def exit(self, evt):
        win.destroy()

    def on_entry_click(*args):
        if ipt.get() == "请输入压缩包路径":
            ipt.delete(0, END)
            ipt.configure(foreground="black")

    def on_entry1_click(*args):
        if ipt1.get() == "请输入密码词典路径":
            ipt1.delete(0, END)
            ipt1.configure(foreground="black")

    def on_entry_leave(*args):
        if ipt.get() == "":
            ipt.insert(0, "请输入压缩包路径")
            ipt.configure(foreground="gray")

    def on_entry1_leave(*args):
        if ipt1.get() == "":
            ipt1.insert(0, "请输入密码词典路径")
            ipt1.configure(foreground="gray")

    def disable_editing(*args):
        return "break"

    def __event_bind(self):
        self.widget_dic["tk_button_lke02cnq"].bind(
            '<Button-1>', self.start_zip)
        self.widget_dic["tk_button_lke02oqt"].bind('<Button-1>', self.exit)
        self.widget_dic["tk_input_lke01dom"].bind(
            '<FocusIn>', self.on_entry_click)
        self.widget_dic["tk_input_lke01dom"].bind(
            '<FocusOut>', self.on_entry_leave)
        self.widget_dic["tk_input_lke037ny"].bind(
            '<FocusIn>', self.on_entry1_click)
        self.widget_dic["tk_input_lke037ny"].bind(
            '<FocusOut>', self.on_entry1_leave)
        self.widget_dic["tk_text_lknwfu7d"].bind(
            '<KeyPress>', self.disable_editing)
        pass


if __name__ == "__main__":
    win = Win()
    win.mainloop()


# print(ret)
