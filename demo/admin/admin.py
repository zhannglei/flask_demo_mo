from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose

from demo import admin, db
from demo.model.user import User


class AnalyticsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('analytics_index.html')


admin.add_view(AnalyticsView(name='Analytics', endpoint='analytics'))

admin.add_view(ModelView(User, db.session))