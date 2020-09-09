from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>ola Jean FIAP!</h1>\nVersao deployada via BeanStalk! o/ \n mostrando que nao se pode utilizar caracteres especiais"

if __name__ == '__main__':
    application.run()
