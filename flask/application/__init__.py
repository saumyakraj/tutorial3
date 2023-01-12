from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://saumyak:password@localhost/flask_db'



from application.views import views