from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_STREAMS'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

@app.route("/")
def home():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        new_post = Post(title=post_title, content=post_content)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('create_post.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Create the DB tables
    app.run(debug=True)
