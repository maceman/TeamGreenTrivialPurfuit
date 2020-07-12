import os
import sys
import tkinter as tk

LARGE_FONT= ("Verdana", 12)

x_padding = 25
y_padding = 25

class TitleScreenFrame(tk.Frame):

    def __init__(self, master):
        """
        """
        tk.Frame.__init__(self, master=master, bg="#264653")
        ## create first frame with team green icon
        path_to_logo="resources" + os.path.sep + "team-green-icon.png"
        team_green_logo_image = tk.PhotoImage(file=path_to_logo)
        lbl_team_green_logo = tk.Label(master=self, image=team_green_logo_image)
        lbl_team_green_logo.img = team_green_logo_image

        ## create second frame with buttons
        btn_new_game = tk.Button(master=self, text="New Game", command=self.new_game_btn_command, bg="#2a9d8f")
        btn_database_tool = tk.Button(master=self, text="Database Tool", command=self.database_tool_btn_command, bg="#2a9d8f")
        btn_quit_game = tk.Button(master=self, text="Quit Game", command=self.quit_game_btn_command, bg="#2a9d8f")

        ## create third title frame
        lbl_game_title = tk.Label(master=self, font=("Verdana", 44), bg="#2a9d8f", text="Welcome to Trivial Purfuit")

        # layout properly
        lbl_game_title.grid(row=0, column=0, columnspan=2, padx=x_padding, pady=y_padding)
        lbl_team_green_logo.grid(row=1, column=0, rowspan=3, padx=x_padding, pady=y_padding)
        btn_new_game.grid(row=1, column=1, padx=x_padding, pady=y_padding)
        btn_database_tool.grid(row=2, column=1, padx=x_padding, pady=y_padding)
        btn_quit_game.grid(row=3, column=1, padx=x_padding, pady=y_padding)

    def database_tool_btn_command(self):
        """
        """
        print("Database Tool")

    def new_game_btn_command(self):
        """
        """
        print("New Game")

    def quit_game_btn_command(self):
        """
        """
        print("Quit Game")
        sys.exit(1)
