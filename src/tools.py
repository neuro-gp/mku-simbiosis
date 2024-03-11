from src.models import db, Brand, ImportGroup, ImportData

from slugify import slugify
from pandas import DataFrame, read_csv
from datetime import datetime

def createBrand(name, slug=None):
    # Crear una marca
    slug = slug or slugify(name)
    with db:
        try:
            brand = Brand.get(Brand.slug == slug)
            print("Brand already exists!")
        except Brand.DoesNotExist:
            brand = Brand.create(name=name, slug=slug)

    print(brand)

def listBrands():
    # Listar marcas
    with db:
        data = [brand.__data__ for brand in Brand.select()]

    print(DataFrame(data))
        
def truncateBrand():
    # Elminar todas las marcas
    with db:
        q = Brand.delete()
        q.execute()


def loadData(path, position):
    data = read_csv(path, sep=None, engine='python')
    if data.empty:
        raise Exception("No hay información para importar")

    with db:
        group = ImportGroup.create(position=position, created=datetime.now())
        for i,row in data.iterrows():
            idata = ImportData.create(
                date = row.Fecha,
                operation = row.Operación,
                item = row.Item,
                detail = row.Detalle,
                unit = row.Unidad,
                quantity = row.Cantidad,
                price = row.Precio,
                total_fob = row['Total FOB'],
                group = group
            )

        

