from tkinter import *

class StudyClock:
    def __init__(self):
        self.root = Tk()
        self.root.title("StudyClock")
        self.root.geometry("400x200")
        self.root.configure(bg="#ffc4eb")

        self.container = Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nswe")
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.container.rowconfigure(0, weight=1)
        self.container.columnconfigure(0, weight=1)

        self.frames = {}

        
        # Define available functions
        self.options = ["study_clock", "clock", "light_mode", "task_manager"]
        self.current_option = 0

        # Initialize function frames
        for option in self.options:
            self.frames[option] = self.create_frame(option)

        # Initialize main menu
        self.frames["main"] = self.main()
        self.frames["Clock"] =self.create_to_clockframe()
        self.frames["study_clock"]= self.create_to_studyframe()
        self.frames["light_mode"]=self.create_to_lightframe()
        self.frames["task manager"]=self.create_to_taskmanagerframe()
        self.show_frame("main")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def main(self):
        frame = Frame(self.container, bg="#ffc4eb")
        frame.grid(row=0, column=0, sticky="nswe")

        for i in range(3):
            frame.grid_columnconfigure(i, weight=1)

        self.mainlabel = Label(
            frame, font="Arial 16", text="📚Study Helper!📚",
            bg="#ffc4eb", fg="#39232E"
        )
        self.mainlabel.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="we")

        self.option_label = Label(frame, text="Current: Study Clock", font="Arial 12", bg="#ffc4eb", fg="#39232E")
        self.option_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        self.cycle = Button(frame, text="Cycle Options", bg="#dda6aa", font="Arial 12", command=self.cycle_options)
        self.cycle.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.confirm = Button(frame, text="Confirm", bg="#dda6aa", font="Arial 12", command=self.confirm_selection)
        self.confirm.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.back = Button(frame, text="Go Back", bg="#dda6aa", font="Arial 12", command=lambda: self.show_frame("main"))
        self.back.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        return frame

    def cycle_options(self):
        self.current_option = (self.current_option + 1) % len(self.options)
        new_text = f"Current: {self.options[self.current_option].replace('_', ' ').title()}"
        self.option_label.config(text=new_text)

    def confirm_selection(self):
        selected_frame = self.options[self.current_option]
        if selected_frame=="clock":
            self.create_to_clockframe
        elif selected_frame=="study_clock":
            self.create_to_studyframe()
        elif selected_frame == "light_mode":
            self.create_to_lightframe()
        elif selected_frame == "task_manager":
            self.create_to_taskmanagerframe()

        self.show_frame(selected_frame)

    def create_frame(self, mode_name):
        frame = Frame(self.container, bg=self.get_color(mode_name))
        Label(frame, text=f"{mode_name.replace('_', ' ').title()} Mode", font="Arial 16", bg=self.get_color(mode_name)).pack(pady=20)
        Button(frame, text="Back", command=lambda: self.show_frame("main")).pack()
        return frame

    def get_color(self, mode_name):
        colors = {
            "study_clock": "#dda6aa",
            "clock": "#c4ebff",
            "light_mode": "#e6f7c1",
            "task_manager": "#ffe9c4"
        }
        return colors.get(mode_name, "#ffffff")
    



    def create_to_clockframe(self):
        frame=Frame(self.container)
        frame.grid(row=0,column=0,sticky="nswe")
        Label(frame,text="clock").grid(row=0,column=1)
        return frame

    def create_to_studyframe(self):
        frame=Frame(self.container)
        frame.grid(row=0,column=0,sticky="nswe")
        Label(frame,text="study").grid(row=0,column=1)
        return frame

    def create_to_lightframe(self):
        frame=Frame(self.container)
        frame.grid(row=0,column=0,sticky="nswe")
        Label(frame,text="light").grid(row=0,column=1)
        return frame

    def create_to_taskmanagerframe(self):
        frame=Frame(self.container)
        frame.grid(row=0,column=0,sticky="nswe")
        Label(frame,text="task").grid(row=0,column=1)
        return frame

    def run(self):
        self.root.mainloop()

StudyClock().run()