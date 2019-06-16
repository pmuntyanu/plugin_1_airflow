from airflow.models import BaseOperator
from airflow.plugins_manager import AirflowPlugin


class Plugin1AirflowOperator(BaseOperator):
    def execute(self, context):
        pass


class Plugin1Airflow(AirflowPlugin):
    # The name of your plugin (str)
    name = 'plugin_1_airflow'
    # A list of class(es) derived from BaseOperator
    operators = [Plugin1AirflowOperator]
    # A list of class(es) derived from BaseSensorOperator
    sensors = []
    # A list of class(es) derived from BaseHook
    hooks = []
    # A list of class(es) derived from BaseExecutor
    executors = []
    # A list of references to inject into the macros namespace
    macros = []
    # A list of objects created from a class derived
    # from flask_admin.BaseView
    admin_views = []
    # A list of Blueprint object created from flask.Blueprint. For use with the flask_admin based GUI
    flask_blueprints = []
    # A list of menu links (flask_admin.base.MenuLink). For use with the flask_admin based GUI
    menu_links = []
    # A list of dictionaries containing FlaskAppBuilder BaseView object and some metadata. See example below
    appbuilder_views = []
    # A list of dictionaries containing FlaskAppBuilder BaseView object and some metadata. See example below
    appbuilder_menu_items = []
