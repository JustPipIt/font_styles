import tkinter as tk


# create the list for row range, and column range
rows = [2, 3, 4]
columns = [0, 1, 2, 3, 4]
 

# create the function for changing the label text to nothing
def remove_text():
    for row in rows:
                for column in columns:
                                try:
                                                test_label["text"] = ""
                                except:
                                                pass

 # create a function to populate the labels with
# user text and fonts
def display_fonts():
                # populate the fonts list
                fonts = create_fonts_list()
                user_text = text_entry.get()
                for row in rows:
                                for column in columns:
                                                test_label = tk.Label(text=f"{user_text}")
                                                test_label.grid(row=row, column=column)
                                                ###############################################

                                                # I got crazy here, but this is the best work

                                                # around I can come up to spread a different

                                                # font per label

                                                ###############################################
                                                for font in fonts:
                                                                old_font = font
                                                                old_font_index = fonts.index(old_font)
                                                                font_to_pop = fonts.index(font)
                                                ################################################################

                                                # compare the 2 indexes defined above shorten the list of fonts

                                                # The font applied to the label will be the last font in the list

                                                # The text fonts will appear in reverse order of the list

                                                ##################################################################
                                                if old_font_index == font_to_pop:
                                                                fonts.pop(font_to_pop)
                                                                test_label.configure(font=old_font)

                               
# a function called by display_fonts to repopulate the depleted fonts list
def create_fonts_list():
                fonts = ["Helvetica", "Sylfaen", "Leelawadee", "Jokerman", "Magneto", "Mistral", "Modern", "Verdana", "Fixedsys", "Terminal", "Broadway", "Candara", "Arial", "Tahoma", "Georgia"]
                return fonts

 


############################

# The following is the code

# that creates the app itself

###############################
 

# create the window

window = tk.Tk()

window.geometry("1000x800")

 

# format the window for a 5X5 grid

window.rowconfigure([0, 1, 2, 3, 4], minsize=100, weight=1)

window.columnconfigure([0, 1, 2, 3, 4],  minsize=100, weight=1)

 

# create a label that will display the directions

directions = tk.Label(text="Enter some text to see it in different fonts")

directions.grid(row=0, column=2)

directions.configure(font="Didot")

 

# create the area to enter your text

text_entry = tk.Entry(width=50)

text_entry.grid(row=1, column=2)

 

# create the button that will generate the different font styles of the text

show_fonts = tk.Button(relief=tk.RIDGE, borderwidth=5, text="Show Fonts", command=lambda: [remove_text(), display_fonts()])

show_fonts.configure(font="Didot")

show_fonts.grid(row=1, column=3, sticky="ew")

 

# keep the app going

window.mainloop()