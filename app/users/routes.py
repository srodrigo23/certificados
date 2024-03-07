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
            'cell_phone': "+59177418588",
            'register_date':''
        },
        {
            'number':2,
            'first_name':"Leonardo Daniel",
            'last_name': "Cardona Camacho",
            'cell_phone': "+59171476453",
            'register_date':''
        },
        {
            'number':3,
            'first_name':"Gustavo",
            'last_name': "Garcia Coca",
            'cell_phone': "+59165748223",
            'register_date':''
        },
        {
            'number':4,
            'first_name':"Juvenal Christian",
            'last_name': "Quispe Reynaga",
            'cell_phone': "+59167859423",
            'register_date':''
        },
    ]

    from app.controllers.users_controller import get_all_users
    from app.controllers.users_controller import add_new_user
    
    for user in users:
        add_new_user(
            first_name=user['first_name'], 
            last_name=user['last_name'],
            cell_phone=user['cell_phone']
        )
    users_with_number = get_all_users()
    cont=0
    for u in users_with_number:
        cont+=1
        u.number=cont
    return render_template('users/index.html', users=users_with_number, title="Usuarios")