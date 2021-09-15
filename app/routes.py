#app routes
from run import app
from flask import render_template, redirect, request, url_for



@app.route('/')
def app_index():
    return render_template("index.html")

@app.route('/about')
def app_about():
    from models import Box
    from models import Skill
    from models import Experience
    from models import Education
    boxes=Box.query.all()
    skills=Skill.query.all()
    experiences=Experience.query.all()
    educations=Education.query.all()
    return render_template("about.html",boxes=boxes,skills=skills,experiences=experiences,educations=educations)

@app.route('/works')
def app_works():
    from models import Work
    works=Work.query.all()
    return render_template("works.html",works=works)

@app.route('/contact')
def app_contact():
    return render_template("contact.html")        

@app.route('/blog')
def app_blog():
    from models import Blog
    blogs=Blog.query.all()
    return render_template("blog.html",blogs=blogs)    