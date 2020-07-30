from src.routes import app

from settings import DEBUG

if __name__ == '__main__':
    app.run(debug=DEBUG)