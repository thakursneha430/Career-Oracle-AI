from flask import Flask
from api.routes import main
from config.settings import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])