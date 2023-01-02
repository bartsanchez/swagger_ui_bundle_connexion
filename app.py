import connexion
from swagger_ui_bundle import swagger_ui_4_path

options = {"swagger_path": swagger_ui_4_path}
app = connexion.FlaskApp(__name__, specification_dir='openapi/', options=options)
app.add_api('my_api.yaml')
