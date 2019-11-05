# This is to prevent reuse of code "DRY" and avoid repetition

'''
SIMPLE FUNCTIONS -  basic print within other functions
'''

def hsu(p, q): # is the formal parameter, # q = number
    print(p * q)  # known as the string or value

def main(): 
    # primary function and values of varaibles travels with them, ex. Rally
    pizza = "Papa Murphy" 
    # this is local variable and not anywhere else, gobally found; scope is limited to the main function, only defined in main function
    hsu(pizza,42)
     #calls the value of pizza, also called an argument

main()