from time import time, sleep
import tkinter
import tkinter.messagebox
from threading import Thread


def main():
    class Download(Thread):
        def run(self):
            sleep(10)
            button_download.config(state=tkinter.NORMAL)
            tkinter.messagebox.showinfo("进度", "下载完成")

    def download():
        button_download.config(state=tkinter.DISABLED)
        Download(daemon=True).start()
        pass

    def display():
        tkinter.messagebox.showinfo("关于", "this is a test")

    top = tkinter.Tk()
    top.geometry('200x150')
    panel = tkinter.Frame(top)
    button_download = tkinter.Button(panel, text="下载", command=download)
    button_show = tkinter.Button(panel, text="展示", command=display)
    button_download.pack(side='left')
    button_show.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()
    pass