import mysql.connector

RecipeDB = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    passwd = "passwd",
    port = "3306"
)

mycursor = RecipeDB.cursor()

def userCheck():
    userReturn = int(input("New or Returning User?\n 1: NEW \n 0: RETURNING \n"))
    if (userReturn == 1): # user is new
        mycursor.execute("CREATE DATABASE Recipe_book")
        mycursor.execute("USE Recipe_book")
        defaultRecipeIngredTable()
        defaultIngredData()
        chickenParmRecipe()
        friedChickenRecipe()
        friedRiceRecipe()
    else: # user is returning
        mycursor.execute("USE Recipe_book")

####################vvvvvvvvvvv DEFAULT TABLES AND RECIPES vvvvvvvvvvvvvv########################

def defaultRecipeIngredTable():
    #mycursor.execute("CREATE TABLE recipes (rec_name VARCHAR(255))")
    mycursor.execute("CREATE TABLE ingredients (ingred_name VARCHAR(255), quantity INT, unit VARCHAR(255))")
    mycursor.execute("CREATE TABLE chicken_parm (ingred_name VARCHAR(255), quantity INT, unit VARCHAR(255))")
    mycursor.execute("CREATE TABLE fried_chicken (ingred_name VARCHAR(255), quantity INT, unit VARCHAR(255))")
    mycursor.execute("CREATE TABLE fried_rice (ingred_name VARCHAR(255), quantity INT, unit VARCHAR(255))")
    mycursor.execute("CREATE TABLE lasagna (ingred_name VARCHAR(255), quantity INT, unit VARCHAR(255))")
    mycursor.execute("CREATE TABLE burger (ingred_name VARCHAR(255), quantity INT, unit VARCHAR(255))")

def defaultIngredData():
    sql = "INSERT INTO ingredients (ingred_name, quantity, unit) VALUES (%s, %s, %s)"
    data = [
        ('chicken breast','10','halves'),
        ('flour','10','cups'),
        ('eggs','24','count'),
        ('panko','50','cups'),
        ('bread crumbs','50','cups'),
        ('parsley','50','tablespoons'),
        ('oil','100','tablespoons'),
        ('marinara sauce','24','oz'),
        ('mozzerella','10','cups'),
        ('basil','50','cups'),
        ('salt','50','tablespoons'),
        ('paprika','100','tablespoons'),
        ('pepper','100','tablespoons'),
        ('water','100000','cups'),
        ('chicken legs','10','lbs'),
        ('rice','100','cups'),
        ('onion minced','10','cups'),
        ('garlic minced','10','tablespoons'),
        ('carrots diced','10','cups'),
        ('peas','10','cups'),
        ('soy sauce','10','tablespoons'),
        ('green onions', '10', 'tablespoons'),
        ('ground beed','10','lbs'),
        ('speghetti sauce','32','oz'),
        ('cottage cheese','32','oz'),
        ('lasagana noodles','25','count')
    ]
    mycursor.executemany(sql,data)
    RecipeDB.commit()


def chickenParmRecipe():
    sql = "INSERT INTO chicken_parm (ingred_name, quantity, unit) VALUES (%s, %s, %s)"
    data = [
        ('chicken breast','4','halves'),
        ('flour','.5','cups'),
        ('eggs','2','count'),
        ('panko','.66','cups'),
        ('bread crumbs','.66','cups'),
        ('parsley','2','tablespoons'),
        ('oil','4','tablespoons'),
        ('marinara sauce','24','oz'),
        ('mozzerella','1','cups'),
        ('basil','.25','cups'),
    ]
    mycursor.executemany(sql,data)
    RecipeDB.commit()


def friedChickenRecipe():
    sql = "INSERT INTO fried_chicken (ingred_name, quantity, unit) VALUES (%s, %s, %s)"
    data = [
        ('flour','4','cups'),
        ('salt','2','tablespoons'),
        ('paprika','1','tablespoons'),
        ('pepper','3','tablespoons'),
        ('egg','2','count'),
        ('water','1','cup'),
        ('chicken leggs','5','lbs'),
        ('oil','3','cups'),
    ]
    mycursor.executemany(sql,data)
    RecipeDB.commit()

def friedRiceRecipe():
    sql = "INSERT INTO fried_rice (ingred_name, quantity, unit) VALUES (%s, %s, %s)"
    data = [
        ('rice','1','cups'),
        ('water','2','cups'),
        ('oil','1','cup'),
        ('onion minced','.25','cup'),
        ('garlic minced','1','tablespoons'),
        ('carrots diced','.5','cups'),
        ('eggs','2','count'),
        ('salt','3','tablespoons'),
        ('peas','.5','cups'),
        ('soy sauce','1','tablespoons')
    ]
    mycursor.executemany(sql,data)
    RecipeDB.commit()

##################^^^^^^^^^^^^^ DEFAULTS TABLES AND RECIPES ^^^^^^^^^^^^^^^##########################

#################vvvvvvvvvvvvvv PRINT FUNCTIONS FOR TABLES vvvvvvvvvvvvvvvv##########################

def printIngredTable():
    mycursor.execute("SELECT * FROM ingredients")
    results = mycursor.fetchall()
    for x in results:
        print(x)
    print("\n")

def printChickenParm():
    mycursor.execute("SELECT * FROM chicken_parm")
    results = mycursor.fetchall()
    for x in results:
        print(x)
    print("\n")

def printFriedChicken():
    mycursor.execute("SELECT * FROM fried_chicken")
    results = mycursor.fetchall()
    for x in results:
        print(x)
    print("\n")


def printFriedRice():
    mycursor.execute("SELECT * FROM fried_rice")
    results = mycursor.fetchall()
    for x in results:
        print(x)
    print("\n")

#################^^^^^^^^^^^^^ PRINT FUNCTIONS FOR TABLES ^^^^^^^^^^^^################

#################vvvvvvvvvvvvv TABLE UPDATING vvvvvvvvvvvvvvvv################

def recipeStockUpdate():
    ingredient = input("Choose an ingredient to update: \n")
    numChange = input("Choose the quantity to change: \n")
    sql = "UPDATE ingredients SET quantity = '%s' WHERE ingred_name = '%s'" % (numChange, ingredient)
    mycursor.execute(sql) 
    RecipeDB.commit()

    
