from tkinter import* #import Tkinter
from tkinter import ttk #import Theme
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CALCULATION_DICTIONARY
global conversion_dictionary #Global conversion dictionary
conversion_dictionary = {'aa':1,'ab':0.1,'ac':0.001,'ad':0.000001,'ae':0.03937008,'af':0.00328084,'ag':0.00109361,'ah':0.00000062,
                         'ba':10,'bb':1,'bc':0.01,'bd': 0.00001,'be':0.39370079,'bf':0.0328084,'bg':0.01093613,'bh':0.00000621,
                         'ca':1000,'cb':100,'cc':1,'cd':0.001,'ce':39.37007874,'cf':3.2808399,'cg':1.09361331,'ch':0.00062137,
                         'da':1000000,'db':100000,'dc':1000,'dd':1,'de':39370.07874016,'df':3280.83989501,'dg':1093.61329834,'dh':0.62137119,
                         'ea':25.4,'eb':2.54,'ec':0.0254,'ed':0.0000254,'ee':1,'ef':0.08333333,'eg':0.02777778,'eh':0.00001578,
                         'fa':304.8,'fb':30.48,'fc':0.3048,'fd': 0.0003048,'fe':12,'ff':1,'fg':0.33333333,'fh':0.00018939,
                         'ga':914.4,'gb':91.44,'gc':0.9144,'gd':0.0009144,'ge':36,'gf':3,'gg':1,'gh':0.00056818,
                         'ha':1609344,'hb':160934.4,'hc':1609.344,'hd': 1.609344,'he':63360,'hf':5280,'hg':1760,'hh':1,
                         'ii':1,'ij':2.2046226218,'ik':35.27396195,'il':1000,'im':0.0011023113109,'in':0.00098420652761,'io':0.001, 
                         'ji':0.45359237,'jj':1,'jk':16,'jl':453.59237,'jm':0.0005,'jn':0.00044642857143,'jo':0.00045359237,   
                         'ki':0.028349523125,'kj':0.0625,'kk':1,'kl':28.349523125,'km':0.00003125,'kn':0.000027901785714,'ko':0.000028349523125, 
                         'li':0.001,'lj':0.0022046226218,'lk':0.03527396195,'ll':1,'lm':0.0000011023113109,'ln':0.00000098420652761,'lo':0.000001, 
                         'mi':907.18474,'mj':2000,'mk':32000,'ml':907184.74,'mm':1,'mn':0.89285714286,'mm':0.90718474,
                         'ni':1016.0469088,'nj':2240,'nk':35840,'nl':1016046.9088,'nm':1.12,'nn':1,'no':1.0160469088,
                         'oi':1000,'oj':2204.6226218,'ok':35273.96195,'ol':1000000,'om':1.1023113109,'on':0.98420652761,'oo':1,
                         'pp':(1,0,1,0), 'pq':(9/5,32,1,0), 'pr':(1,273.15,1,0),
                         'qp':(1,-32,5/9,0), 'qq':(1,0,1,0), 'qr':(1,-32,5/9,273.15),
                         'rp':(1,-273.15,1,0), 'rq':(1,-273,9/5,32), 'rr':(1,0,1,0)}
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< SUPPORT/CALCULATIONS_CLASS
class Calculations:
    def CalcLength(self):
        """This method gets the values of both radiobuttons, traps ValueError's, gets the user input in float form, makes sure the value is >= 0,
           combines the radiobutton values to attain the right conversion factor, calculates and then returns the result to the label in non-scientific 4dp notation."""
        x = self.v_from_l.get()
        y = self.v_to_l.get() 
        try:
            i = float(self.Entry_from_l.get())
            if (i >= 0) and (i != -0):
                v = x+y
                c = float(conversion_dictionary[v])
                r = (i*c)
                self.Label_display_l.configure(text = ("{:.4f}".format(r)))
            else:
                self.Label_display_l.configure(text = "<Enter a postive number>")
        except ValueError:
            self.Label_display_l.configure(text = "<Invalid Input>")
        self.Entry_from_l.focus()
            
    def CalcWeight(self):
        """This method gets the values of both radiobuttons, traps ValueError's, gets the user input in float form, makes sure the value is >= 0,
           combines the radiobutton values to attain the right conversion factor, calculates and then returns the result to the label in non-scientific 4dp notation."""
        x = self.v_from_w.get()
        y = self.v_to_w.get()
        try:
            i = float(self.Entry_from_w.get())
            if (i >= 0) and (i != -0): #Not accept -0 fixed!
                v = x+y
                c = float(conversion_dictionary[v])
                r = (i*c)
                self.Label_display_w.configure(text = ("{:.4f}".format(r)))
            else:
                self.Label_display_w.configure(text = "<Enter a postive number>")
        except ValueError:
            self.Label_display_w.configure(text = "<Invalid Input>")
        self.Entry_from_w.focus()
       
    def CalcTemp(self):
        """This method gets the values of both radiobuttons, traps ValueError's, gets the user input in float form, makes sure the values are not below absolute
           zero, combines the radiobutton values to attain the right conversion factor, calculates and then returns the result to the label in non-scientific 4dp notation."""
        x = self.v_from_t.get()
        y = self.v_to_t.get() 
        try:
            i = float(self.Entry_from_t.get())
            if (x == "q" and i >= -459.67 or x == "p" and i >= -273.15 or x == "r" and i >= 0):
                v = x+y 
                mul1 = float(conversion_dictionary[v][0]) 
                add1 = float(conversion_dictionary[v][1]) 
                mul2 = float(conversion_dictionary[v][2]) 
                add2 = float(conversion_dictionary[v][3]) 
                i = i*mul1
                i = i+add1
                i = i*mul2
                i = i+add2 
                self.Label_display_t.configure(text = ("{:.4f}".format(i))) #Every input is multiplied, added to, multiplied and added to depending on the conversion equation
            else:
                self.Label_display_t.configure(text = "<Below Absolute Zero>") 
        except ValueError:
            self.Label_display_t.configure(text = "<Invalid Input>")
        self.Entry_from_t.focus()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< GUI_CLASS
class CalculatorGUI(Calculations): #Sub class is used to simplify code
    def __init__(self, root): #Creates all GUI objects
        #=================================================================================================================== Create Notebook
        self.notebook = ttk.Notebook(root) #Notebook packed to root window
        self.notebook.pack()
        length_frame = ttk.Frame(self.notebook) #Frames created
        weight_frame = ttk.Frame(self.notebook)
        temperature_frame = ttk.Frame(self.notebook)
        help_frame = ttk.Frame(self.notebook)
        self.notebook.add(length_frame, text = 'LENGTH') #Frames named
        self.notebook.add(weight_frame, text = 'WEIGHT')
        self.notebook.add(temperature_frame, text = 'TEMPERATURE')
        self.notebook.add(help_frame, text = 'HELP')
        #=================================================================================================================== Length_Frame
        #---------------------------------------------------------Static GUI_Objects:
        self.Label_from_l = ttk.Label(length_frame, text = "From:", width = 10)
        self.Label_from_l.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)
        self.Label_to_l = ttk.Label(length_frame, text = "To:", width = 10)
        self.Label_to_l.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = E)
        self.Label_exit_l = ttk.Label(length_frame, text = "<Esc/exit>")
        self.Label_exit_l.grid(row = 11, column = 0, columnspan = 1, padx = 5, pady = 5)
        self.Label_help_l = ttk.Label(length_frame, text = "<Ctr-h/Help>")
        self.Label_help_l.grid(row = 11, column = 2, columnspan = 1, padx = 5, pady = 5)
        #---------------------------------------------------------RadioButton GUI_Objects:
        self.v_from_l = StringVar()
        self.v_from_l.set("a") #Initially activated to eliminate error
        self.v_to_l = StringVar()
        self.v_to_l.set("a")
        
        self.values_l = ["a","b","c","d","e","f","g","h"]
        texts = ["mm","cm","m","Km","Inches","Feet","Yards","Miles"]
        i=0
        for i in range (0,8,1):
            self.rb_from_l = ttk.Radiobutton(length_frame, variable = self.v_from_l, value = self.values_l[i], text = texts[i])
            self.rb_from_l.grid(row = int(i+1), column = 0, sticky = W) 
            i+=1
        i=0
        for i in range (0,8,1):
            self.rb_to_l = ttk.Radiobutton(length_frame, variable = self.v_to_l, value = self.values_l[i], text = texts[i])
            self.rb_to_l.grid(row = int(i+1), column = 2, sticky = W)
            i+=1
        #---------------------------------------------------------Dynamic GUI_Objects:
        self.Label_entry_l = ttk.Label(length_frame, text = "Enter a value:")
        self.Label_entry_l.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = W)
        self.Entry_from_l = ttk.Entry(length_frame, width = 10)
        self.Entry_from_l.grid(row = 9, column = 1, padx = 5, pady = 5, sticky = E+W)
        self.Entry_from_l.focus()
        self.Button_l = ttk.Button(length_frame, text = "Calculate", command = self.CalcLength)
        self.Button_l.grid(row = 9, column = 2, padx = 5, pady = 5)
        self.Button_clear_l = ttk.Button(length_frame, text = "Clear", command = self.clear_function)
        self.Button_clear_l.grid(row = 10, column = 2, padx = 2, pady = 5)
        self.Label_display_l = ttk.Label(length_frame,text = "")
        self.Label_display_l.grid(row = 10, column = 0, columnspan = 2, padx = 5, pady = 5)
        #=================================================================================================================== Weight_Frame
        #---------------------------------------------------------Static GUI_Objects:
        Label_from_w = ttk.Label(weight_frame, text = "From:", width = 10)
        Label_from_w.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)
        Label_to_w = ttk.Label(weight_frame, text = "To:", width = 10)
        Label_to_w.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = E)
        self.Label_exit_w = ttk.Label(weight_frame, text = "<Esc/exit>")
        self.Label_exit_w.grid(row = 11, column = 0, columnspan = 1, padx = 5, pady = 5)
        self.Label_help_w = ttk.Label(weight_frame, text = "<Ctr-h/Help>")
        self.Label_help_w.grid(row = 11, column = 2, columnspan = 1, padx = 5, pady = 5)
        #---------------------------------------------------------RadioButton GUI_Objects:
        self.v_from_w = StringVar()
        self.v_from_w.set("i") #Initially activated to eliminate error
        self.v_to_w = StringVar()
        self.v_to_w.set("i")
        
        self.values_w = ["i","j","k","l","m","n","o"]
        texts = ["Kg","Pounds","Oz","Grams","Short_ton","Long_ton","Metric_ton"]
        i=0
        for i in range (0,7,1):
            self.rb_from_w = ttk.Radiobutton(weight_frame, variable = self.v_from_w, value = self.values_w[i], text = texts[i])
            self.rb_from_w.grid(row = int(i+1), column = 0, sticky = W) 
            i+=1
        i=0
        for i in range (0,7,1):
            self.rb_to_w = ttk.Radiobutton(weight_frame, variable = self.v_to_w, value = self.values_w[i], text = texts[i])
            self.rb_to_w.grid(row = int(i+1), column = 2, sticky = W)
            i+=1
        #---------------------------------------------------------Dynamic GUI_Objects:
        self.Label_entry_w = ttk.Label(weight_frame, text = "Enter a value:")
        self.Label_entry_w.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = W)
        self.Entry_from_w = ttk.Entry(weight_frame, width = 10)
        self.Entry_from_w.grid(row = 9, column = 1, padx = 5, pady = 5, sticky = E+W)
        self.Button_w = ttk.Button(weight_frame, text = "Calculate", command = self.CalcWeight)
        self.Button_w.grid(row = 9, column = 2, padx = 5, pady = 5)
        self.Button_clear_w = ttk.Button(weight_frame, text = "Clear", command = self.clear_function)
        self.Button_clear_w.grid(row = 10, column = 2, padx = 2, pady = 5)
        self.Label_display_w = ttk.Label(weight_frame,text = "")
        self.Label_display_w.grid(row = 10, column = 0, columnspan = 2, padx = 5, pady = 5)
        #=================================================================================================================== Temperature_Frame
        #---------------------------------------------------------Static GUI_Objects:
        Label_from_t = ttk.Label(temperature_frame, text = "From:", width = 10)
        Label_from_t.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = E)
        Label_to_t = ttk.Label(temperature_frame, text = "To:", width = 10)
        Label_to_t.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = E)
        self.Label_exit_t = ttk.Label(temperature_frame, text = "<Esc/exit>")
        self.Label_exit_t.grid(row = 11, column = 0, columnspan = 1, padx = 5, pady = 5)
        self.Label_help_t = ttk.Label(temperature_frame, text = "<Ctr-h/Help>")
        self.Label_help_t.grid(row = 11, column = 2, columnspan = 1, padx = 5, pady = 5)
        #---------------------------------------------------------RadioButton GUI_Objects:
        self.v_from_t = StringVar()
        self.v_from_t.set("p") #Initially activated to eliminate error
        self.v_to_t = StringVar()
        self.v_to_t.set("p")
        
        self.values_t = ["p","q","r"]
        texts = ["Celcius","Fahrenheit","Kelvin"]
        i=0
        for i in range (0,3,1):
            self.rb_from_t = ttk.Radiobutton(temperature_frame, variable = self.v_from_t, value = self.values_t[i], text = texts[i])
            self.rb_from_t.grid(row = int(i+1), column = 0, sticky = W) 
            i+=1
        i=0
        for i in range (0,3,1):
            self.rb_to_t = ttk.Radiobutton(temperature_frame, variable = self.v_to_t, value = self.values_t[i], text = texts[i])
            self.rb_to_t.grid(row = int(i+1), column = 2, sticky = W)
            i+=1
        #---------------------------------------------------------Dynamic GUI_Objects:
        self.Label_entry_t = ttk.Label(temperature_frame, text = "Enter a value:")
        self.Label_entry_t.grid(row = 9, column = 0, padx = 5, pady = 5, sticky = W)
        self.Entry_from_t = ttk.Entry(temperature_frame, width = 10)
        self.Entry_from_t.grid(row = 9, column = 1, padx = 5, pady = 5, sticky = E+W)
        self.Button_t = ttk.Button(temperature_frame, text = "Calculate", command = self.CalcTemp)
        self.Button_t.grid(row = 9, column = 2, padx = 5, pady = 5)
        self.Button_clear_t = ttk.Button(temperature_frame, text = "Clear", command = self.clear_function)
        self.Button_clear_t.grid(row = 10, column = 2, padx = 2, pady = 5)
        self.Label_display_t = ttk.Label(temperature_frame,text = "")
        self.Label_display_t.grid(row = 10, column = 0, columnspan = 2, padx = 5, pady = 5)
        #=================================================================================================================== Help_Frame
        self.help_text = ttk.Label(help_frame, text = """

        <Enter> = Calculate
        <Del> = Clear

        <Ctrl-Left> = Change Tab (Left)
        <Ctrl-Right> = Change Tab (Right)

        Radiobuttons(Rb)
        <Shift-Down> = Left  Rb Scroll Down
        <Shift-Up> = Left  Rb Scroll Up
        <Shift-Right> = Right Rb Scroll Down
        <Shift-Left> = Right Rb Scroll Up
        
        <Esc> = Exit Calculator
        <Ctrl-h> = Return to Help Tab""") #Help text
        self.help_text.grid()
        #=================================================================================================================== Key Binding
        root.bind("<Return>", self.calculate_callback) #Enter key to calculate button
        root.bind("<Delete>", self.clear_callback) #Delete key to clear button
        root.bind("<Control-Left>", self.Left_Change) #Control and left arrow key to scroll left one tab
        root.bind("<Control-Right>", self.Right_Change) #Control and right arrow key to scroll right one tab
        root.bind("<Escape>", self.close_app) #Escape key to exit application
        root.bind("<Control-h>", self.help_frame) #Control and h key to scroll to help tab
        root.bind("<Control-H>", self.help_frame) #Incase keyboard has Caps Lock on this binding will still work
        root.bind("<Shift-Up>", self.up_pick) #Shift and up key to scroll up on left radiobuttons
        root.bind("<Shift-Down>", self.down_pick) #Shift and down key to scroll down on left radiobuttons
        root.bind("<Shift-Left>", self.left_pick) #Shift and left key to scroll down on left radiobuttons
        root.bind("<Shift-Right>", self.right_pick) #Shift and right key to scroll up on left radiobuttons
        #===================================================================================================================  Callback & Clear Methods
    def clear_function(self): #This method checks which tab the notebook is on and according to this clears entry and display widgets, and focuses entry box for next input
        tab_index = self.notebook.index(self.notebook.select())
        if  tab_index == 0:
            self.Entry_from_l.delete(0, END)
            self.Label_display_l.configure(text = "")
            self.Entry_from_l.focus()
        if tab_index == 1:
            self.Entry_from_w.delete(0, END)
            self.Label_display_w.configure(text = "")
            self.Entry_from_w.focus()
        if tab_index == 2:
            self.Entry_from_t.delete(0, END)
            self.Label_display_t.configure(text = "")
            self.Entry_from_t.focus()
    def calculate_callback(self, event): #This method, depending on the tab calls the calculate method
        tab_index = self.notebook.index(self.notebook.select())
        if tab_index == 0:
            self.CalcLength()
        if tab_index == 1:
            self.CalcWeight()
        if tab_index == 2:
            self.CalcTemp()
    def clear_callback(self, event): #This method calls the 'clear_function' method
        self.clear_function()
    def Left_Change(self, event): #This method gets the notebook tab index and depending whether it is possible will move the user one tab to the left
        tab_index = self.notebook.index(self.notebook.select())
        if tab_index != 0:
          self.notebook.select(tab_index-1)
          self.Entry_from_l.focus()
          self.Entry_from_w.focus()
    def Right_Change(self, event): #This method gets the notebook tab index and depending whether it is possible will move the user one tab to the right
        tab_index = self.notebook.index(self.notebook.select())
        if tab_index != 3:
          self.notebook.select(tab_index+1)
          self.Entry_from_w.focus()
          self.Entry_from_t.focus()
    def close_app(self, event): #This method will close the root window/exit application
        root.destroy()
    def help_frame(self, event): #This method will move the user to the 'HELP' frame
        self.notebook.select(3)
    def up_pick(self, event): #This method will scroll up the available left hand radiobuttons
        tab_index = self.notebook.index(self.notebook.select())
        if (tab_index == 0) and (self.v_from_l.get() != "a"): #Checks which tab, and that radiobutton selection is not already at the top
            self.v_from_l.set(self.values_l[(self.values_l.index(self.v_from_l.get()))-1]) #gets index of current radiobutton value, takes away 1, gets new value and sets this
        if (tab_index == 1) and (self.v_from_w.get() != "i"):
            self.v_from_w.set(self.values_w[(self.values_w.index(self.v_from_w.get()))-1])
        if (tab_index == 2) and (self.v_from_t.get() != "p"):
            self.v_from_t.set(self.values_t[(self.values_t.index(self.v_from_t.get()))-1])
    def down_pick(self, event): #This method will scroll down the available left hand radiobuttons
        tab_index = self.notebook.index(self.notebook.select())
        if (tab_index == 0) and (self.v_from_l.get() != "h"):
            self.v_from_l.set(self.values_l[(self.values_l.index(self.v_from_l.get()))+1])
        if (tab_index == 1) and (self.v_from_w.get() != "o"):
            self.v_from_w.set(self.values_w[(self.values_w.index(self.v_from_w.get()))+1])
        if (tab_index == 2) and (self.v_from_t.get() != "r"):
            self.v_from_t.set(self.values_t[(self.values_t.index(self.v_from_t.get()))+1])
    def left_pick(self, event): #This method will scroll up the available right hand radiobuttons
        tab_index = self.notebook.index(self.notebook.select())
        if (tab_index == 0) and (self.v_to_l.get() != "a"):
            self.v_to_l.set(self.values_l[(self.values_l.index(self.v_to_l.get()))-1])
        if (tab_index == 1) and (self.v_to_w.get() != "i"):
            self.v_to_w.set(self.values_w[(self.values_w.index(self.v_to_w.get()))-1])
        if (tab_index == 2) and (self.v_to_t.get() != "p"):
            self.v_to_t.set(self.values_t[(self.values_t.index(self.v_to_t.get()))-1])
    def right_pick(self, event): #This method will scroll down the available right hand radiobuttons
        tab_index = self.notebook.index(self.notebook.select())
        if (tab_index == 0) and (self.v_to_l.get() != "h"):
            self.v_to_l.set(self.values_l[(self.values_l.index(self.v_to_l.get()))+1])
        if (tab_index == 1) and (self.v_from_w.get() != "o"):
            self.v_to_w.set(self.values_w[(self.values_w.index(self.v_to_w.get()))+1])
        if (tab_index == 2) and (self.v_to_t.get() != "r"):
            self.v_to_t.set(self.values_t[(self.values_t.index(self.v_to_t.get()))+1])
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MAIN_ROUTINE
#Main Routine:
if __name__ == "__main__":
    root = Tk() #Create root window
    app = CalculatorGUI(root) #Define GUI
    root.title("C.C v4.5")
    root.resizable(False,False)
    root.mainloop() #Start Application
