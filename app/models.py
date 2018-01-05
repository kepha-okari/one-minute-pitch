from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
#from sqlalchemy.sql import func

@login_manager.user_loader
def load_user(user_id):
    '''
    @login_manager.user_loader Passes in a user_id to this function
    Function queries the database and gets a user's id as a response
    '''
    return User.query.get(int(user_id))

#comments model
class Comment(db.Model):
    """class models comments from users in pitches"""
    __tablename__ = 'comments'

    # add columns
    id = db.Column(db. Integer,primary_key = True)
    comment_section_id = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    #pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))


    def save_comment(self):
        """ Save the comments per pitch """
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self,id):
        comment = Comments.query.order_by(Comments.date_posted.desc()).filter_by(pitches_id=id).all()
        return comment


class User(UserMixin,db.Model):
    """ class modelling the users """

    __tablename__='users'

    #create the columns
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    pitches = db.relationship("Pitch", backref="user", lazy = "dynamic")
    #comment = db.relationship("Comments", backref="user", lazy = "dynamic")

    # securing passwords
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'


#pitches class
class Pitch(db.Model):
    """ List of pitches in each category """

    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String)
    cagory_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


    def save_pitch(self):
        ''' Save the pitches '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()

    # display pitches
    @classmethod
    def get_pitches(cls):
        pitches = Pitch.query.all()
        return pitches

# categories model
class Category(db.Model):
    ''' Category class define category per pitch '''

    __tablename__ = 'categories'

    # add columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    # save
    def save_category(self):
        ''' Function that saves a category '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        ''' gets pitches by category '''
        categories = Category.query.all()
        return categories
