from app import app
from peewee import *
from flask_security import Security, PeeweeUserDatastore, \
    UserMixin, RoleMixin, login_required
import peewee


DATABASE = peewee.PostgresqlDatabase('leavemanagement', user="postgres")

class Role(Model, RoleMixin):
	name = CharField(unique=True)
	description = TextField(null=True)

	class Meta:
		database = DATABASE

class User(Model, UserMixin):
	email = TextField()
	password = TextField()
	active = BooleanField(default=True)
	confirmed_at = DateTimeField(null=True)

	class Meta:
		database = DATABASE

class UserRoles(Model):
    # Because peewee does not come with built-in many-to-many
    # relationships, we need this intermediary class to link
    # user to roles.
	user = ForeignKeyField(User, related_name='roles')
	role = ForeignKeyField(Role, related_name='users')
	name = property(lambda self: self.role.name)
	description = property(lambda self: self.role.description)

	class Meta:
		database = DATABASE

# Setup Flask-Security
#user_datastore = PeeweeUserDatastore(User, Role, UserRoles)
#security = Security(app, user_datastore)

# Create a user to test with
@app.before_first_request
#def create_user():
#    for Model in (Role, User, UserRoles):
#        Model.drop_table(fail_silently=True)
#        Model.create_table(fail_silently=True)
#    user_datastore.create_user(email='yvonnendutaw@gmail.com', password='password')

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe = True)
    DATABASE.close()
