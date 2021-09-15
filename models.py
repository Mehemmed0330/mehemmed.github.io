from run import db


class Box(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     number_of_works= db.Column(db.String(80))
     works_name= db.Column(db.String(80))

class Skill(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     program_picture= db.Column(db.String(80))
     program_nam= db.Column(db.String(80))

class Experience(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     work_date= db.Column(db.String(80))
     work_location= db.Column(db.String(80)) 
     work_about= db.Column(db.String(80))    

class Education(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     learn_date= db.Column(db.String(80))
     learn_location= db.Column(db.String(80)) 
     learn_about= db.Column(db.String(80))         

class Work(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     work_picture= db.Column(db.String(80))
     page_link= db.Column(db.String(80))     


class Blog(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     blog_picture= db.Column(db.String(80))
     blog_title= db.Column(db.String(80))     
     blog_about= db.Column(db.String(80))   
     blog_date=db.Column(db.String(80))
     blog_link=db.Column(db.String(80))

class work(db.Model):
     id = db.Column(db.Integer, primary_key=True)
