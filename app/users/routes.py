from flask import render_template
from app.users import bp

# from app.extensions import db
# from app.models.post import Post

@bp.route('/')
def index():
    # posts = Post.query.all()

    users = [
        {
            'number':1,
            'first_name':"Sergio Rodrigo",
            'last_name': "Cardenas Rivera",
            'cellphone': "+59177418588",
            'register_date':''
        },
        {
            'number':2,
            'first_name':"Leonardo Daniel",
            'last_name': "Cardona Camacho",
            'cellphone': "+59171476453",
            'register_date':''
        },
        {
            'number':3,
            'first_name':"Gustavo",
            'last_name': "Garcia Coca",
            'cellphone': "+59165748223",
            'register_date':''
        },
        {
            'number':4,
            'first_name':"Juvenal Christian",
            'last_name': "Quispe Reynaga",
            'cellphone': "+59167859423",
            'register_date':''
        },
    ]
        
    
    return render_template('users/index.html', users=users)