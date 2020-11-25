#This is a file full of functions that are used in the AptTools.py
#application. 
import pickle

def writeMoneyData(values):
    fileChecker('bin/money.dat')
    moneyFile = open('bin/money.dat', 'wb')
    pickle.dump(values, moneyFile)
    moneyFile.close()

def readMoneyData():
    fileChecker('bin/money.dat')
    moneyFile = open('bin/money.dat', 'rb')
    readValues = pickle.load(moneyFile)
    moneyFile.close()
    return readValues

def fileChecker(path):
    #Opens file at the specified path, creating the file
    #if it does not exist and then returns
    file = open(path, 'ab')
    file.close()
    return