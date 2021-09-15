# admin routes
from run import app,db
from flask import render_template, redirect, request, url_for
import os

@app.route('/admin')
def admin_base():
    return render_template("admin/base.html")


@app.route('/admin/aboutboxes',methods=['GET','POST'])
def admin_boxes():
    from models import Box
    boxes=Box.query.all()
    if request.method=='POST':
        box=Box(
           number_of_works=request.form['number_of_works'],
            works_name=request.form['works_name']
        )
        db.session.add(box)
        db.session.commit()
        return redirect("/admin/aboutboxes")
    return render_template("admin/aboutboxes.html",boxes=boxes)

@app.route('/delete/<int:id>')
def delete(id):
    from models import Box
    box=Box.query.get(id)
    db.session.delete(box)
    db.session.commit()
    return redirect('/admin/aboutboxes')

@app.route('/update/<int:id>',methods=['GET','POST'])
def update(id):
    from models import Box
    box=Box.query.get(id)
    if request.method=='POST':
        box=Box.query.get(id)
        number_of_works=request.form['number_of_works'],
        works_name=request.form['works_name']
        db.session.commit()
        return redirect('/admin/aboutboxes')
    return render_template('admin/boxesupdate.html',box=box)


@app.route('/admin/skills',methods=['GET','POST'])
def admin_skills():
    from models import Skill
    skills=Skill.query.all()
    if request.method=='POST':
        file=request.files['program_picture']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        skill=Skill(
           program_picture=filename,
            program_nam=request.form['program_nam']
        )
        db.session.add(skill)
        db.session.commit()
        return redirect("/admin/skills")
    return render_template("admin/skills.html",skills=skills)

@app.route('/deletee/<int:id>')
def deletee(id):
    from models import Skill
    skill=Skill.query.get(id)
    db.session.delete(skill)
    db.session.commit()
    return redirect('/admin/skills')  

@app.route('/admin/experience',methods=['GET','POST'])
def admin_experience():
    from models import Experience
    experiences=Experience.query.all()
    if request.method=='POST':
        experience=Experience(
            work_date=request.form['work_date'],
            work_location=request.form['work_location'],
            work_about=request.form['work_about']
        )
        db.session.add(experience)
        db.session.commit()
        return redirect("/admin/experience")
    return render_template("admin/experience.html",experiences=experiences)

@app.route('/Delete/<int:id>')
def Delete(id):
    from models import Experience
    experience=Experience.query.get(id)
    db.session.delete(experience)
    db.session.commit()
    return redirect('/admin/experience')  

@app.route('/admin/education',methods=['GET','POST'])
def admin_education():
    from models import Education
    educations=Education.query.all()
    if request.method=='POST':
        education=Education(
            learn_date=request.form['learn_date'],
            learn_location=request.form['learn_location'],
            learn_about=request.form['learn_about']
        )
        db.session.add(education)
        db.session.commit()
        return redirect("/admin/education")
    return render_template("admin/education.html",educations=educations)

@app.route('/Deletee/<int:id>')
def Deletee(id):
    from models import Education
    education=Education.query.get(id)
    db.session.delete(education)
    db.session.commit()
    return redirect('/admin/education')  

@app.route('/admin/works',methods=['GET','POST'])
def admin_works():
    from models import Work
    works=Work.query.all()
    if request.method=='POST':
        file=request.files['work_picture']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        work=Work(
           work_picture=filename,
           page_link=request.form['page_link']
        )
        db.session.add(work)
        db.session.commit()
        return redirect("/admin/works")
    return render_template("admin/works.html",works=works)

@app.route('/Delet/<int:id>')
def Delet(id):
    from models import Work
    work=Work.query.get(id)
    db.session.delete(work)
    db.session.commit()
    return redirect('/admin/works')  

@app.route('/admin/contact')
def admin_contact():
    return render_template("admin/contact.html")


@app.route('/admin/blogs',methods=['GET','POST'])
def admin_blogs():
    from models import Blog
    blogs=Blog.query.all()
    if request.method=='POST':
        file=request.files['blog_picture']
        filename=file.filename
        file.save(os.path.join('static/uploads/',filename))
        blog=Blog(
           blog_picture=filename,
           blog_title=request.form['blog_title'],
           blog_about=request.form['blog_about'],
           blog_date=request.form['blog_date'],
           blog_link=request.form['blog_link']
        )
        db.session.add(blog)
        db.session.commit()
        return redirect("/admin/blogs")

    return render_template("admin/blogs.html",blogs=blogs)

@app.route('/Delett/<int:id>')
def Delett(id):
    from models import Blog
    blog=Blog.query.get(id)
    db.session.delete(blog)
    db.session.commit()
    return redirect('/admin/blogs')      
