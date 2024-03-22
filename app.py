from flask import Flask
from asgiref.wsgi import WsgiToAsgi
from src.modules.bill.bill_controller import bill_blueprint as bill_bp
from src.modules.legislator.legislator_controller import legislator_blueprint as legislator_bp
import uvicorn
import os

app = Flask(__name__)

app.register_blueprint(bill_bp, url_prefix="/bill")
app.register_blueprint(legislator_bp, url_prefix="/legislator")

asgi_app = WsgiToAsgi(app)

if __name__ == "__main__":
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = os.getenv("PORT", 8000)
    uvicorn.run(asgi_app, host=HOST, port=PORT)