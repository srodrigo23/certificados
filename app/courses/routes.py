
from flask import render_template
from app.courses import bp

# from app.extensions import db
# from app.models.post import Post

@bp.route('/')
def index():
    # posts = Post.query.all()
    return render_template('courses/index.html')#, posts=posts)