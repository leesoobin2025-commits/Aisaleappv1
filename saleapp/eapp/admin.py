from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms.fields.numeric import FloatField

from saleapp.eapp import app, db
from saleapp.eapp.models import Category,Product

admin=Admin(app,name="JetMind's Admin")

class ProductView(ModelView):
    column_list = ['id','name','price']
    column_searchable_list = ['name']
    can_export = True
    edit_modal = True
    column_editable_list = ['name']
    column_filters = ['id','name','price']
    form_overrides = {
        'price': FloatField
    }

admin.add_view(ModelView(Category, db.session))
admin.add_view(ModelView(Product, db.session))