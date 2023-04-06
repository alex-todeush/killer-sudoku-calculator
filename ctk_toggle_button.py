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

    def set_command(self, command):
        self.command = command

    def toggle(self):
        if self.command is not None:
            self.command()
        if self.pressed == False:   
            self.set_pressed()
        else:
            self.set_unpressed()
    
    def set_pressed(self):
        self.new_button._fg_color = "#0f3552"
        self.pressed = True
        self.new_button._draw()

    def set_unpressed(self):
        self.new_button._fg_color = "#1F6AA5"
        self.pressed = False
        self.new_button._draw()