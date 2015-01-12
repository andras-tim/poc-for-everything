from flask.ext.wtf import Form
from wtforms_alchemy import model_form_factory
from .server import db
from .models import User, Task
 
BaseModelForm = model_form_factory(Form)


class ModelForm(BaseModelForm):
    @classmethod
    def get_session(cls):
        return db.session


class UserCreateForm(ModelForm):
    class Meta:
        model = User


class TaskCreateForm(ModelForm):
    class Meta:
        model = Task