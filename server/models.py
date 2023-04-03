# 📚 Review With Students:
    # Review models
    # Review MVC
#SQLAlchemy import
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

# 📚 Review With Students:
    # What SQLAlchemy() is replacing from SQLAlchemy in phase 3
     
db = SQLAlchemy()
# 1. ✅ Create a Production Model
class Production(db.Model):

    def __init__(self,title,genre,budget,image,director,description,ongoing):
        self.id=None
        self.title=title
        self.genre=genre
        self.budget=budget
        self.image=image
        self.director=director
        self.description=description
        self.ongoing=ongoing
        self.created_at=None
        self.updated_at=None

	# tablename = 'Productions'
    __tablename__="productions"
	# Columns:
        # title: string, genre: string, budget:float, image:string,director: string, description:string, ongoing:boolean, created_at:date time, updated_at: date time 
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String,nullable=False)
    genre=db.Column(db.String,nullable=False)
    budget=db.Column(db.Float,nullable=False)
    image=db.Column(db.String,nullable=False)
    director=db.Column(db.String,nullable=False)
    description=db.Column(db.String,nullable=False)
    ongoing=db.Column(db.Boolean,nullable=False,default=True)
    created_at=db.Column(db.DateTime(timezone=True),nullable=False,server_default=func.now())
    updated_at=db.Column(db.DateTime(timezone=True),server_onupdate=func.now())

    def __repr__(self):
        return f"<Production {self.id} {self.title} {self.genre} {self.budget} {self.image} {self.director} {self.description} {self.ongoing} {self.created_at} {self.updated_at}>"


# 2. ✅ navigate to app.py