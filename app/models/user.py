from app.extensions import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
   __tablename__ = 'users'
   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(64), unique=True, index=True)
   username = db.Column(db.String(64), unique=True, index=True)
   password_hash = db.Column(db.String(128), nullable=False)
   messages = db.relationship('Message',backref='user')

   def __repr__(self):
        return f'<Users {self.email}>'
  

   @property
   def password(self):
      raise AttributeError('password is not a readable attribute')

   @password.setter
   def password(self, password):
      self.password_hash = generate_password_hash(password)

   def verify_password(self, password):
      return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
   return User.query.get(int(id))