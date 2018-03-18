#create a program that filters given input to see if its a int, string, or list then 
#return something depending on type and length

def filterNum(num):

    if isinstance(num, int):
        if(num < 100):
            print("That's a small number!")
        elif(num >= 100):
            print("That's a big number!")
    elif isinstance(num, str):
        if len(num) < 50:
            print("Short Sentence!")
        elif len(num) >= 50:
            print("Long Sentence!")
    elif isinstance(num, list):
        if len(num) < 10:
            print("Short List!")
        elif len(num) >= 50:
            print("Big List!")
filterNum(2)