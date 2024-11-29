from flask import Flask, render_template

from db_connection import get_diagnosis_data, get_eat_food_data, get_gene_info_data, get_not_eat_food_data, get_references_data, get_signs_and_symptoms_data


app=Flask(__name__,static_folder="static")
@app.route('/')
def index():
    diagnosis_data = get_diagnosis_data()
    signs_and_symptoms = get_signs_and_symptoms_data()
    return render_template("index.html",diagnosis = diagnosis_data, signs=signs_and_symptoms)
    
@app.route('/database')
def database():
    gene_info_db_data=get_gene_info_data()
    return render_template("database.html",data=gene_info_db_data)

@app.route('/food')
def food():
    eat_food_db_data=get_eat_food_data()
    not_eat_food_db_data=get_not_eat_food_data()
    print(not_eat_food_db_data)
    return render_template("food.html",eat_food=eat_food_db_data,not_eat_food=not_eat_food_db_data)
    
@app.route('/references')
def references():
    references_db_data=get_references_data()
    return render_template("references.html",references=references_db_data)




if __name__=="__main__":
    app.run(debug=True)
