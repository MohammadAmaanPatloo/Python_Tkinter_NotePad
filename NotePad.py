from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
# The below Functions handle various actions triggered by the user, such as creating a new file, opening a file, saving a file, quitting the application, and performing cut, copy, and paste operations.
def newFile(): # Function to create a new file
    global file # A global variable file is initialized to keep track of the current file being edited.
    root.title("Python(tkinter) - Notepad by MAP")
    file = None
    TextArea.delete(1.0, END)


def openFile():  # Function to open an existing file
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile(): # Function to save the current file
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp(): # Function to quit the application
    root.destroy()

def cut():  # Function to perform cut operation
    TextArea.event_generate(("<<Cut>>"))

def copy():  # Function to perform copy operation
    TextArea.event_generate(("<<Copy>>"))

def paste():  # Function to perform paste operation
    TextArea.event_generate(("<<Paste>>"))

def about(): # Function to show about information
    showinfo("Notepad", "Notepad by MAP")

if __name__ == '__main__':
    #Basic tkinter setup
    root = Tk()
    root.title("Python(tkinter) - Notepad by MAP")
    root.geometry("644x788")

    #Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Creating a menu bar
    MenuBar = Menu(root)

    # File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    #  Adding menu items
    # To open new file
    FileMenu.add_command(label="New", command=newFile) # add_command() method specifies the label and the function to be executed when the menu item is clicked.
    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file
    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    #To give a feature of cut, copy and paste
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu = EditMenu)
    # Edit Menu Ends

    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    # Help Menu Ends
    
    root.config(menu=MenuBar)

    #Adding Scrollbar 
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview) # config() method is used to specify the command to be executed when the scrollbar is scrolled, and the yscrollcommand attribute of the text area is set to the scrollbar's set() method.
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()