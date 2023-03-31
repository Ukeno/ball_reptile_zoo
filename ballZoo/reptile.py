from flask import ( Blueprint, render_template ) 
# from . import models
import json 

reptiles = json.load(open('reptiles.json'))

bp = Blueprint('reptile', __name__, url_prefix="/reptiles")

@bp.route('/')
def index(): 
    return render_template('reptiles/index.html', reptiles=reptiles)

## Part of the assignment, but can't get it to work>
# @bp.route('/<int:id>')
# def show(id): 
#     user = models.User.query.filter_by(id=id).first()
#     user_dict = {
#         'username': user.username
#     }

#     return user_dict

@bp.route('/<int:id>')
def show(id): 
    reptile = reptiles[id - 1]
    return render_template('reptiles/show.html', reptile=reptile)