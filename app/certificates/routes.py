from flask import render_template
from app.certificates import bp

# from app.extensions import db
# from app.models.post import Post

@bp.route('/')
def index():
    # posts = Post.query.all()
    return render_template('certificates/index.html')#, posts=posts)

# @bp.route('/categories/')
# def categories():
#     return render_template('posts/categories.html')