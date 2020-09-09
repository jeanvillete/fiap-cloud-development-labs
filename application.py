from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>olá Jean FIAP!</h1>\nVersao deployada via BeanStalk! o/"

if __name__ == '__main__':
    application.run()
