import os
from src.routes import app

from settings import DEBUG
from scripts.setup import setup_run

if __name__ == '__main__':
    setup_run()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', debug=DEBUG, port=port)