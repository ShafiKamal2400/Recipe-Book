import SQL_Funcs
import mysql.connector


SQL_Funcs.userCheck()

userInput = int(input("enter a recipe to print or print ingredient list: \n |1: Chicken Parm| |2:Fried Chicken| |3:Fried Rice| |4: Ingredient Stock| |0: exit| \n"))

while userInput != 0:
    if userInput == 1:
        SQL_Funcs.printChickenParm()
    elif userInput == 2:
        SQL_Funcs.printFriedChicken()
    elif userInput == 3:
        SQL_Funcs.printFriedRice()
    elif userInput == 4:
        SQL_Funcs.printIngredTable()
    userInput = int(input("enter another option\n"))

SQL_Funcs.recipeStockUpdate()
SQL_Funcs.printIngredTable()
input()
