from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.menu import MenuLink

from app import app, db
from flask import redirect, url_for
from flask_login import current_user, LoginManager
from app.models import User, Owner, Pet


class MyModelView(ModelView):
    form_excluded_columns = 'pets'


class MySecureModelView(MyModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


admin = Admin(app, index_view=MyAdminIndexView())
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)


admin.add_view(MySecureModelView(User, db.session))
admin.add_view(MyModelView(Owner, db.session))
admin.add_view(MySecureModelView(Pet, db.session))
admin.add_link(MenuLink('LogOut', '/logout'))
