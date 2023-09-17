
from collections import Counter
from time import sleep
from random import random

listGreeting=['**************************************'
,'**    Welcome to the Snakes Cafe!   **'
,'**    Please see our menu below.    **'
,'**'
,'** To quit at any time, type "quit" **'
,'**************************************']

listAppetizers=[
    'Appetizers',
    '----------',
    'Wings',
    'Cookies',
    'Spring Rolls']

listEntrees=[
    'Entrees',
    '_______',
    'Salmon',
    'Steak',
    'Meat Tornado',
    'A Literal Garden'
]

listDesserts=[
    'Desserts',
    '________',
    'Ice Cream',
    'Cake',
    'Pie'
]

listDrinks=[
    'Drinks',
    '______',
    'Coffee',
    'Tea',
    'Unicorn Tears'
]

listMenu=[*listAppetizers,*listEntrees,*listDesserts,*listDrinks]

listOrderPrompt=[
    '***********************************',
    '** What would you like to order? **',
    '***********************************'
]

listWarning=[
    "**      I'm sorry I didn't get that.    **"
    '** Please enter any item from the menu. **'
]



dictResponses={'greeting':listGreeting,'appetizers':listAppetizers,'entrees':listEntrees,'desserts':listDesserts,'drinks':listDrinks,'menu':listMenu,'orderPrompt':listOrderPrompt,'warning':listWarning}

dictMenuOptions=Counter([*listAppetizers[2:],*listEntrees[2:],*listDesserts[2:],*listDrinks[2:]])

dictCustOrder={}
listCustOrder=[]

def printMessage(message:str):
    #TODO: remove leading space
    print("\n","\n".join(message),"\n")

def formateOrder(key:str,value:int)->str:
    strS, strAdj = ["s","have"] if value>1 else ["","has"]
    print(strS,strAdj)
    return f'** {value} order{strS} of {key} {strAdj} been added to your meal **'

#TODO: add parameter types
def whileOrdering(dictMenuOpt,dictRes,dictCustOrd,listCustOrd)->list:
    for i in ['greeting','menu','orderPrompt']:
        printMessage(dictRes[i])

    strInput = ''

    while True:
        strInput = input("> ")
        sleep(random()*2)

        if strInput == 'quit' or strInput =='q':
            printMessage(['**********  Exiting...   **********'])
            sleep(4.5)
            break
        elif strInput in dictMenuOpt:
            if strInput in dictCustOrd:
                dictCustOrd[strInput]+=1
            else:
                dictCustOrd[strInput]=1

            strCurrOrder = formateOrder(strInput,dictCustOrd[strInput])

            listCustOrd= listCustOrd.append(strCurrOrder)

            printMessage([strCurrOrder])

        else:
            printMessage(dictRes['warning'])







if __name__=='__main__':
    custOrder=whileOrdering(dictMenuOptions,dictResponses,dictCustOrder,listCustOrder)