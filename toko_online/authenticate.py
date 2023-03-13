from flask import Flask, jsonify, request, make_response
from functools import wraps
import jwt
import datetime
from . import secret

app = Flask(__name__)
app.config['SECRET_KEY'] = f'{secret}'


def token_required(f):
    @wraps()
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'pesan': 'Token hilang/tidak ada'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'pesan': 'token tidak sah'}), 403

        return f(*args, **kwargs)
    return decorated
