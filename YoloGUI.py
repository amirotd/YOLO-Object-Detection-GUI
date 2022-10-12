import tkinter as tk
from tkinter import filedialog


class YoloGui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Yolo object detection")
        self.geometry('512x256+200+100')
        self['padx'] = 5
        self['pady'] = 5

        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=5)

        self.grid_rowconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=5)

        self.image_var = tk.StringVar(self)
        self.image_var.set('')
        self.confidence_var = tk.StringVar(self)
        self.confidence_var.set('0.5')
        self.threshold_var = tk.StringVar(self)
        self.threshold_var.set('0.3')

        self.upload_box = tk.Entry(self, textvariable=self.image_var)
        self.upload_box.grid(column=0, row=0)

        self.upload_button = tk.Button(self, text='Browse', command=self.upload_file)
        self.upload_button.grid(column=1, row=0)

        self.confidence_box = tk.Spinbox(self, textvariable=self.confidence_var, increment=0.1, from_=0, to=100)
        self.confidence_box.grid(column=0, row=1)

        self.threshold_box = tk.Spinbox(self, textvariable=self.threshold_var, increment=0.1, from_=0, to=100)
        self.threshold_box.grid(column=1, row=1)

        self.start_button = tk.Button(self, text='Start', command=self.start)
        self.start_button.grid(column=0, row=2)

        self.quit_button = tk.Button(self, text='Quit', command=self.destroy)
        self.quit_button.grid(column=1, row=2)

    def upload_file(self):
        filename = filedialog.askopenfilename()
        self.image_var = filename
        self.upload_box.delete(0, tk.END)
        self.upload_box.insert(0, self.image_var)

    def start(self):
        pass


if __name__ == '__main__':
    app = YoloGui()
    app.mainloop()
