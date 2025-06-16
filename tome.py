from tkinter import *
import time 
class StudyClock(Tk):
    def __init__(self):
        super().__init__()
        self.title("StudyClock")
        self.geometry("400x200")
        self.configure(bg="#ffc4eb")

        self.container = Frame(self)
        self.container.grid(row=0, column=0, sticky="nswe")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.frames = {}
        self.options = ["Clock", "StudyClock", "LightMode", "TaskManager"]
        self.current_option = 0
    
        # Initialize frames
        self.frames["Main"] = MainMenu(self)
        self.frames["Clock"] = ClockMode(self)
        self.frames["StudyClock"] = StudyClockMode(self)
        self.frames["LightMode"] = LightMode(self)
        self.frames["TaskManager"] = TaskManagerMode(self)

        self.show_frame("Main")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def cycle_options(self):
        self.current_option = (self.current_option + 1) % len(self.options)
        new_text = f"Current: {self.options[self.current_option]}"
        self.frames["Main"].option_label.config(text=new_text)

    def confirm_selection(self):
        selected_frame = self.options[self.current_option]
        self.show_frame(selected_frame)

class MainMenu(Frame):
    def __init__(self, parent):
        super().__init__(parent.container, bg="#ffc4eb")
        self.grid(row=0, column=0, sticky="nswe")
        self.mainlabel = Label(self, font="Arial 16", text="📚Study Helper!📚",bg="#ffc4eb", fg="#39232E").grid(row=1,column=0,columnspan=3,padx=10,pady=10)

        self.option_label = Label(self, text="Current: StudyClock", font="Arial 12", bg="#ffc4eb", fg="#39232E")
        self.option_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        Button(self, text="Cycle Options", bg="#dda6aa", font="Arial 12", command=parent.cycle_options).grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        Button(self, text="Confirm", bg="#dda6aa", font="Arial 12", command=parent.confirm_selection).grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        Button(self, text="Go Back", bg="#dda6aa", font="Arial 12", command=lambda: parent.show_frame("Main")).grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

class ClockMode(Frame):
    def __init__(self, parent):
        super().__init__(parent.container, bg="#c4ebff")
        self.grid(row=0, column=0, sticky="nswe")
        Label(self, text="Clock Mode", font="Arial 16", bg="#c4ebff").pack(pady=20)
        Button(self, text="Back", command=lambda: parent.show_frame("Main")).pack()
  
        Label(self, text=time.strftime("%H:%M:%S"), font="Arial 16", bg="#dda6aa").pack(pady=20)


class StudyClockMode(Frame):
    def __init__(self, parent):
        super().__init__(parent.container, bg="#dda6aa")
        self.grid(row=0, column=0, sticky="nswe")
        Label(self, text="Study Clock Mode", font="Arial 16", bg="#dda6aa").pack(pady=20)
        Button(self, text="Back", command=lambda: parent.show_frame("Main")).pack()
        

class LightMode(Frame):
    def __init__(self, parent):
        super().__init__(parent.container, bg="#e6f7c1")
        self.grid(row=0, column=0, sticky="nswe")
        Label(self, text="Light Mode", font="Arial 16", bg="#e6f7c1").pack(pady=20)
        Button(self, text="Back", command=lambda: parent.show_frame("Main")).pack()

class TaskManagerMode(Frame):
    def __init__(self, parent):
        super().__init__(parent.container, bg="#ffe9c4")
        self.grid(row=0, column=0, sticky="nswe")
        Label(self, text="Task Manager Mode", font="Arial 16", bg="#ffe9c4").pack(pady=20)
        Button(self, text="Back", command=lambda: parent.show_frame("Main")).pack()

if __name__ == "__main__":
    app = StudyClock()
    app.mainloop()