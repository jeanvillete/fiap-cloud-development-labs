from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1>ola Jean FIAP!</h1><p>Versao deployada via BeanStalk! o/</p> <p>mostrando que nao se pode utilizar caracteres especiais</p>"

if __name__ == '__main__':
    application.run()
