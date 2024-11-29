import mysql.connector


# Creates database connection and returns connection object
def create_mysql_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        port = 3306,
        user="root",
        password="root",
        database="celiac_disease"
    )
    return mydb

# Gets all the data from the gene_info table and returns json object
def get_gene_info_data():
    mydb = create_mysql_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT DISTINCT gene_info.gene_name, gene_info.gene_symbol, gene_info.gene_role, gene_info.gene_references, gene_additional_info.gene_information FROM gene_info INNER JOIN gene_additional_info ON gene_info.gene_symbol = gene_additional_info.gene_symbol")
    result = mycursor.fetchall()

    # Fetch column names
    columns = ['gene_name', 'gene_symbol', 'gene_role', 'gene_references', 'gene_information']

    # Convert result to a list of dictionaries
    data = []
    for row in result:
        row_dict = {}
        for col_index, col_name in enumerate(columns):
            row_dict[col_name] = row[col_index]
        data.append(row_dict)

    mycursor.close()
    mydb.close()
    return data


def get_diagnosis_data():
    mydb =create_mysql_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT dig_name from diagnosis")
    result = mycursor.fetchall()
    data = []
    for row in result:
        data.append(row[0])
    mycursor.close()
    mydb.close()
    return data

def get_signs_and_symptoms_data():
    mydb =create_mysql_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT type_of_finding, sign_name from signs_and_symptoms")
    result = mycursor.fetchall()
    columns = ['type_of_finding','sign_name']
    data = []
    for row in result:
        row_dict = {}
        for col_index, col_name in enumerate(columns):
            row_dict[col_name] = row[col_index]
        data.append(row_dict)
    mycursor.close()
    mydb.close()
    return data

def get_eat_food_data():
    mydb =create_mysql_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT food_type, food_name from eat_food")
    result = mycursor.fetchall()
    columns = ['food_type','food_name']
    data = []
    for row in result:
        row_dict = {}
        for col_index, col_name in enumerate(columns):
            row_dict[col_name] = row[col_index]
        data.append(row_dict)
    mycursor.close()
    mydb.close()
    return data

def get_not_eat_food_data():
    mydb =create_mysql_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT food_name from not_eat_food")
    result = mycursor.fetchall()
    data = []
    for row in result:
        data.append(row[0])
    mycursor.close()
    mydb.close()
    return data
    

def get_references_data():
    mydb =create_mysql_connection()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * from ref")
    result = mycursor.fetchall()
    data = []
    for row in result:
        data.append(row[0])
    mycursor.close()
    mydb.close()
    return data



