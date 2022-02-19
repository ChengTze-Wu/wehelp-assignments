from flask import Flask
from view import auth, api
import config

app = Flask(__name__)
app.config.from_object(config.Development)
app.register_blueprint(auth.auth)
app.register_blueprint(api.api, url_prefix="/api/")

if __name__ == '__main__':
    app.run(port=3000)