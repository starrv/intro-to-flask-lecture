#!/usr/bin/env python3
# 📚 Review With Students:
    # Seeding 
# 5. ✅ Imports
    # app from app
from app import app
    # db and Production from models
from models import db, Production
# 6. ✅ Initialize the SQLAlchemy instance with `db.init_app(app)`


# 7. ✅ Create application context `with app.app_context():`
with app.app_context():
    Production.query.delete()
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/

# 8.✅ Create a query to delete all existing records from Production    
   
# 9.✅ Create some seeds for production and commit them to the database. 
    production_1=Production("Grant Money","Hip Hop",30000000.00,"https://assets.dnainfo.com/generated/photo/2014/10/free-money-1414002257.jpg/larger.jpg","Future","Fire",True)
    production_2=Production("Soul Mate","Hip Hop",10000000.00,"https://lonerwolf.com/wp-content/uploads/2014/10/soul-mate-relationship-connections-min.jpg","Mac Miller","Fire",True)
    production_3=Production("Under My Umbrella","R&B",100000000,"https://upload.wikimedia.org/wikipedia/en/0/01/Rihanna_-_Umbrella.png","RiRi","its on fire!!",True)
    production_4=Production("Jimmy Hendrix","Rock",50000.00,"https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Denis_Bourez_-_Madame_Tussauds%2C_London_%288747018021%29.jpg/1200px-Denis_Bourez_-_Madame_Tussauds%2C_London_%288747018021%29.jpg","Jimmy Hendrix","its on fire!!",True)
    production_5=Production("Poker Face","Pop",100000000,"https://goat.com.au/wp-content/uploads/2019/11/Lady-Gaga-Poker-Face-HERO.png","Lady Gaga","its on fire!!",True)

    db.session.add_all([production_1,production_2,production_3,production_4,production_5])
    db.session.commit()
    db.session.close()
    
# 10.✅ Run in terminal:
    # `python seed.py`
# 11.✅ run `flask shell` in the terminal 
    # from app import app
    # from models import Production
    # Check the seeds by querying Production
# 12.✅ Navigate back to app.py  
    