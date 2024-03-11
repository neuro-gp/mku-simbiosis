from src import app

import peewee

db = peewee.SqliteDatabase(app.DBNAME)

class Brand(peewee.Model):
    name = peewee.CharField()
    slug = peewee.CharField()

    class Meta:
        database = db
        table_name = 'brands'

    def __str__(self):
        return f'[{self.id}] {self.name} ({self.slug})'

class Type(peewee.Model):
    name = peewee.CharField()
    slug = peewee.CharField()

    class Meta:
        database = db
        table_name = 'types'

class Product(peewee.Model):
    name = peewee.CharField()
    slug = peewee.CharField()
    brand = peewee.ForeignKeyField(Brand, backref='products')
    type = peewee.ForeignKeyField(Type, backref='products')

    class Meta:
        database = db
        table_name = 'products'

class RgexCode(peewee.Model):
    re = peewee.CharField()
    product = peewee.ForeignKeyField(Product, backref='regex_codes')

    class Meta:
        database = db
        table_name = 'regex_code'

class ImportGroup(peewee.Model):
    position = peewee.CharField()
    created = peewee.DateTimeField()

    class Meta:
        database = db
        table_name = 'import_group'

class ImportData(peewee.Model):
    date = peewee.DateField()
    operation = peewee.CharField()
    item = peewee.CharField()
    detail = peewee.CharField()
    unit = peewee.CharField()
    quantity = peewee.IntegerField()
    price = peewee.FloatField()
    total_fob = peewee.FloatField()
    group = peewee.ForeignKeyField(ImportGroup, backref='imports')

    class Meta:
        database = db
        table_name = 'import_data'

class ImportProduct(peewee.Model):
    import_data = peewee.ForeignKeyField(ImportData)
    product = peewee.ForeignKeyField(Product)
    trust = peewee.FloatField()

    class Meta:
        database = db
        table_name = 'import_product'


# -- Migration function ---

def migrate():
    with db:
        db.create_tables([
            Brand,
            Type,
            Product,
            RgexCode,
            ImportGroup,
            ImportData,
            ImportProduct
        ])