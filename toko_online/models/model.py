from .. import db

# User as Pelanggan


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(64), unique=True)
    alamat = db.Column(db.String(124), unique=False, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)

    desc_order_id = db.Column(
        db.Integer, db.ForeignKey('description_order.id'))

    def __init__(self, username, alamat, email, password):
        self.username = username
        self.alamat = alamat
        self.email = email
        self.password = password

# Description_Order as Detail_Pesanan


class Description_Order(db.Model):
    __tablename__ = 'description_order'
    id = db.Column(db.Integer, primary_key=True)
    quantity_of_goods = db.Column(db.Integer, unique=False, nullable=True)

    user = db.relationship('User', backref='description_order')
    order = db.relationship('Order', backref='description_order')

    def __init__(self, quantity_of_goods):
        self.quantity_of_goods = quantity_of_goods

# Order as Pesanan


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(64), unique=True, nullable=False)
    date_order = db.Column(db.Integer, unique=False, nullable=False)

    desc_order_id = db.Column(
        db.Integer, db.ForeignKey('description_order.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    sales_result_id = db.Column(db.Integer, db.ForeignKey('sales_result.id'))

    def __init__(self, date_order):
        self.date_order = date_order

# Sales_Result as Hasil Penjualan


class Sales_Result(db.Model):
    __tablename__ = 'sales_result'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(64), unique=True, nullable=False)
    sales_date = db.Column(db.String(50), unique=False, nullable=False)

    order = db.relationship('Order', backref='sales_result')
    sales_record = db.relationship('Sales_Record', backref='sales_result')

    def __init__(self, sales_date):
        self.sales_date = sales_date

# Sales_Record as Data Penjualan


class Sales_Record(db.Model):
    __tablename__ = 'sales_record'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(64), unique=True, nullable=False)
    income = db.Column(db.Integer, unique=False, nullable=False)
    output = db.Column(db.Integer, unique=False, nullable=False)
    profit = db.Column(db.Integer, unique=False, nullable=False)

    sales_result_id = db.Column(db.Integer, db.ForeignKey('sales_result.id'))
    owner = db.relationship('Owner', backref='sales_record', uselist=False)

    def __init__(self, income, output, profit):
        self.income = income
        self.output = output
        self.profit = profit

# Owner


class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(64), unique=True, nullable=False)
    username = db.Column(db.String(50), unique=False, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)

    sales_record_id = db.Column(db.Integer, db.ForeignKey('sales_result.id'))

    def __init__(self, username, password):
        self.username = username
        self.password = password

# Product as Produk


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(64), unique=True, nullable=False)
    nama = db.Column(db.String(50), unique=True, nullable=False)
    jenis = db.Column(db.String(50), unique=False, nullable=False)
    exp_date = db.Column(db.String(50), unique=False, nullable=False)

    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    order = db.relationship('Order', backref='product')
    karyawan = db.relationship('Employment', backref='product')

    def __init__(self, nama, jenis, exp_date):
        self.nama = nama
        self.jenis = jenis
        self.exp_date = exp_date

# Employment as Karyawan


class Employment(db.Model):
    __tablename__ = 'employment'
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(64), unique=True, nullable=False)
    first_name = db.Column(db.String(50), unique=False, nullable=False)
    middle_name = db.Column(db.String(50), unique=False, nullable=False)
    last_name = db.Column(db.String(50), unique=False, nullable=False)
    date_of_birth = db.Column(db.String(50), unique=False, nullable=False)
    age = db.Column(db.Integer, unique=False, nullable=True)
    street = db.Column(db.String(50), unique=False, nullable=False)
    rt = db.Column(db.Integer, unique=False, nullable=False)
    rw = db.Column(db.Integer, unique=False, nullable=False)
    kelurahan = db.Column(db.String(50), unique=False, nullable=False)
    kecamatan = db.Column(db.String(50), unique=False, nullable=False)
    category = db.Column(db.String(50), unique=False, nullable=False)
    date_of_entry = db.Column(db.String(50), unique=False, nullable=False)

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, first_name, middle_name, last_name, date_of_birth, age, street, rt, rw, kelurahan, kecamatan, category, date_of_entry):
        self.first_name = first_name
        self.middle_name = middle_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.street = street
        self.rt = rt
        self.rw = rw
        self.kelurahan = kelurahan
        self.kecamatan = kecamatan
        self.category = category
        self.date_of_entry = date_of_entry
