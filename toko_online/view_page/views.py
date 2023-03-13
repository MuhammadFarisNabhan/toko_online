from flask import Blueprint, render_template, request
from ..authenticate import token_required
import jwt
import datetime

view = Blueprint("view", __name__)


@view.route('/')
def home():
    return render_template("beranda.html")


@view.route('/daftar')
def signUp():
    return render_template("mendaftar.html")


@view.route('/masuk')
def login():
    # auth = request.authorization
    # if auth and auth.password == 'password':
    #     token = jwt.encode({'user':auth.username, 'exp':datetime.datetime.utcnow()+ datetime.timedelta(minutes=60)}, app)

    return render_template("masuk.html")


@view.route('/keranjang')
def cart():
    return render_template("keranjang.html")


@view.route('/pembayaran')
def payment():
    return render_template("pembayaran.html")


@view.route('/data_penjualan')
def data():
    return render_template("data_penjualan.html")


@view.route('/karyawan')
def employment():
    return render_template("detail_karyawan.html")
