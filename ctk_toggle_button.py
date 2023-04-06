from typing import Callable
import customtkinter

class ToggleButton(customtkinter.CTkFrame):
    def __init__(self,
                 *args,
                 pressed: bool = False,
                 text : str = "",
                 width: int = 100,
                 height: int = 32,
                 command: Callable = None,
                 **kwargs):
        super().__init__(*args, width=width, height=height, **kwargs)

        self.command = command
        self.pressed = pressed
        self.text = text
        self.width = width
        self.height = height

        self.configure(fg_color=("gray78", "gray28"))  # set frame color

        self.new_button = customtkinter.CTkButton(self, fg_color="#1F6AA5", text=self.text, width=self.width, height=self.height,
                                                       command=self.toggle)
        self.new_button.grid(row=0, column=0, pady=3)


    def toggle(self):
        if self.command is not None:
            self.command()
        try:
            if self.new_button._fg_color == ("#1F6AA5"):   
                self.new_button._fg_color = "#0f3552"
            else:
                self.new_button._fg_color = "#1F6AA5"
        except ValueError:
            return
    
    def set_pressed(self):
        self.new_button._fg_color = "#0f3552"
        self.new_button._draw()

    def set_unpressed(self):
        self.new_button._fg_color = "#1F6AA5"
        self.new_button._draw()

    def get(self) -> int:
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: float):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))