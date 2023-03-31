from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

class Fact(db.Model):
    __tablename__ =  'reptiles' 
    
    # Part of the assignment, but not working?
    # {
    # 'common_name': 'Ball python',
    # 'scientific_name': 'Python regius',
    # 'conservation_status': 'Near threatened',
    # 'native_habitat': 'Forest, savanna, shrubland, grassland',
    # 'fun_fact': 'Ball pythons received their common name from their behavior of curling up into a ball when threatened.'
    # }
    
    id = db.Column(db.Integer, primary_key = True) 
    scientific_name = db.Column(db.String(250))
    conservation_status = db.Column(db.String(250))
    native_habitat = db.Column(db.String(250))
    fun_fact = db.Column(db.Text)
    
    # submitter = db.Column(db.String(250)) 
    # fact = db.Column(db.Text) 

