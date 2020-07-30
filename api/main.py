from src.routes import app

from settings import DEBUG
from scripts.setup import setup_run

if __name__ == '__main__':
    setup_run()
    app.run(debug=DEBUG)