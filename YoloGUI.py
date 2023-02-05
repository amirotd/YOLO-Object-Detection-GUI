import tkinter as tk
from tkinter import filedialog
from Yolo import Yolo


class YoloGui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Yolo object detection")
        self.geometry('512x256+200+100')
        self.configure(bg='LightSteelBlue2')
        self['padx'] = 5
        self['pady'] = 5

        self.grid_columnconfigure(0, weight=5)
        self.grid_columnconfigure(1, weight=5)

        self.grid_rowconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=5)
        self.grid_rowconfigure(3, weight=5)

        self.image_var = tk.StringVar(self)
        self.image_var.set('')
        self.yolo_var = tk.StringVar(self)
        self.yolo_var.set('')
        self.confidence_var = tk.StringVar(self)
        self.confidence_var.set('0.5')
        self.threshold_var = tk.StringVar(self)
        self.threshold_var.set('0.3')

        self.upload_frame = tk.LabelFrame(self, text='Add File', bg='LightSteelBlue2')
        self.upload_frame.grid(column=0, row=0)

        self.upload_box = tk.Entry(self.upload_frame, textvariable=self.image_var, width=60)
        self.upload_box.grid(column=0, row=0)

        self.upload_button = tk.Button(self.upload_frame, text='Browse', command=self.upload_file, bg='SteelBlue3', fg='white', activebackground='SteelBlue2')
        self.upload_button.grid(column=1, row=0)

        self.yolo_path_frame = tk.LabelFrame(self, text='Yolo Path', bg='LightSteelBlue2')
        self.yolo_path_frame.grid(column=0, row=1)

        self.yolo_path_box = tk.Entry(self.yolo_path_frame, textvariable=self.yolo_var, width=60)
        self.yolo_path_box.grid(column=0, row=0)

        self.yolo_button = tk.Button(self.yolo_path_frame, text='Browse', command=self.set_path, bg='SteelBlue3', fg='white', activebackground='SteelBlue2')
        self.yolo_button.grid(column=1, row=0)

        self.settings_frame = tk.LabelFrame(self, text='Settings', bg='LightSteelBlue2')
        self.settings_frame.grid(column=0, row=2)

        self.confidence_label = tk.Label(self.settings_frame, text='Confidence')
        self.confidence_label.grid(column=0, row=0)

        self.confidence_box = tk.Spinbox(self.settings_frame, textvariable=self.confidence_var, increment=0.1, from_=0, to=100, width=10)
        self.confidence_box.grid(column=1, row=0)

        self.threshold_label = tk.Label(self.settings_frame, text='Threshold')
        self.threshold_label.grid(column=0, row=1)

        self.threshold_box = tk.Spinbox(self.settings_frame, textvariable=self.threshold_var, increment=0.1, from_=0, to=100, width=10)
        self.threshold_box.grid(column=1, row=1)

        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.grid(column=0, row=3)

        self.start_button = tk.Button(self.buttons_frame, text='Start', command=self.start, bg='SteelBlue3', fg='white', activebackground='SteelBlue2')
        self.start_button.grid(column=0, row=0)

        self.quit_button = tk.Button(self.buttons_frame, text='Quit', command=self.destroy, bg='SteelBlue3', fg='white', activebackground='SteelBlue2')
        self.quit_button.grid(column=1, row=0)

    def upload_file(self):
        filename = filedialog.askopenfilename()
        self.image_var = filename
        self.upload_box.delete(0, tk.END)
        self.upload_box.insert(0, self.image_var)
        self.upload_box.xview_moveto(1)

    def set_path(self):
        path = filedialog.askdirectory()
        self.yolo_var = path
        self.yolo_path_box.delete(0, tk.END)
        self.yolo_path_box.insert(0, self.yolo_var)

    def start(self):
        y = Yolo(self.image_var, self.yolo_var, float(self.confidence_var.get()), float(self.threshold_var.get()))
        y.start_process()


if __name__ == '__main__':
    app = YoloGui()
    app.mainloop()
