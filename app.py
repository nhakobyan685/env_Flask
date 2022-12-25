from flask import Flask
import os


app = Flask(__name__)

if os.environ.get('FLASK_ENV') == 'dev':
    app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Development')

elif os.environ.get('FLASK_ENV') == 'testing':
    app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Testing')

else:
    app.logger.info(os.environ.get('FLASK_ENV'))
    app.config.from_object('config.Production')


@app.route('/')
def hello():

    env = app.config.get('ENV_VALUE')

    if env == "Development":
        return f"Hi folks your in {env} environment and volume is mounted."
    elif env == "Testing":
        return f"Hi folks your in {env} environment."
    else:
        return f"Hi folks your in {env} environment."

if __name__ == '__main__':
    app.run(host='0.0.0.0')

