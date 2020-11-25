import sys
import time
import pickle
import PySimpleGUI as gui

from aptToolsFunctions import *

class FinanceTrackerEntryWindow:

    def start(self):
        #Configure the gui variables
        textBoxColor = 'LightGray'
        largeTextFont = ['Ariel', 20]
        smallTextFont = ['Ariel', 12]
    
        #And initialize a dictionary to store data in
        moneyData = {}
        #First, load saved data into memory, pass if there is no saved data
        try:
            moneyData = readMoneyData()
        except:
            print("No saved data! New money.dat file to be created.")
            pass
        
        gui.ChangeLookAndFeel('Dark')
        gui.SetOptions(element_padding=(0, 0))
        
        #Define the layout for the application
        layout = [
            [gui.T("Finance Tracker", font=largeTextFont)],

            [
            gui.T("Store Name:", font=smallTextFont),
            gui.I(key='-Store-', do_not_clear=False, background_color=textBoxColor, text_color='black')
            ],

            [
            gui.T("Ammount:", font=smallTextFont),
            gui.I(key='-Amount-', do_not_clear=False, background_color=textBoxColor,
                  text_color='black', pad=((11,0), (0,0)))
            ],

            [
            gui.B("Enter", pad=(8,0)),
            gui.B('Done')
            ]
        ]

        #This is where the application window is created
        app = None
        if sys.platform != 'darwin':
            app = gui.Window("Apt Tools", layout, grab_anywhere=True, no_titlebar=True)
        else:
            app = gui.Window("Apt Tools", layout, grab_anywhere=True)

        #Event Loop
        while True:
        
            event, values = app.read()

            if event in [gui.WIN_CLOSED, 'Done']:
                break

            #Check if enter button has been pressed
            if event == 'Enter':
                #Try to take the user input and add it to it's respective
                #spot in the dictionary, if it has no spot, create one
                try:
                    if values.get('-Store-') in moneyData.keys:
                        moneyData[values.get('-Store-')
                                ].append((int(values.get('-Amount-')), time.time()))
                    else:
                        moneyData[values.get('-Store-')
                                ] = [(int(values.get('-Amount-')), time.time())]
                except:
                    print("Invalid Input!")
                    continue

            #Save our data to file
            writeMoneyData(moneyData)

        #Clean up
        app.close()

    def __init__(self):
        self.start()

class FinanceTrackerGraphWindow:

    def start(self):
        moneyData = {}
        try:
            moneyData = readMoneyData()
        except:
            print("No Data Found!")
            pass

        layout=[
            gui.Graph(size=(600,600), graph_bottom_left=(0,0), graph_top_right=(600,600), key='graph', background_color=['light']gray)
        ]

        app = None
        if sys.platform != 'darwin':
            app = gui.Window("Apt Tools", layout, grab_anywhere=True, no_titlebar=True)
        else:
            app = gui.Window("Apt Tools", layout, grab_anywhere=True)

        app.close()

    def __init__(self):
        self.start()

if __name__ == '__main__':
    window = FinanceTrackerGraphWindow()