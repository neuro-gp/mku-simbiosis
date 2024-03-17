from src.models import db, Brand

from slugify import slugify
from pandas import DataFrame

# -- Brands CRUD --

def createBrand(name, slug=None):
    # Crear una marca
    slug = slug or slugify(name, to_lower=True)
    with db:
        try:
            brand = Brand.get(Brand.slug == slug)
            print("Brand's slug already exists!")
        except Brand.DoesNotExist:
            brand = Brand.create(name=name, slug=slug)

    print(brand)

def listBrands():
    # Listar marcas
    with db:
        data = [brand.__data__ for brand in Brand.select()]

    print(DataFrame(data))

def searchBrands(term):
    # Listar marcas
    with db:
        data = [brand.__data__ for brand in Brand.select().where(Brand.name.contains(term))]

    print(DataFrame(data))

def updateBrand(id, name=None, slug=None):
    # Actualiza una marca
    with db:
        try:
            brand = Brand.get(Brand.id == id)
            brand.name = name or brand.name
            brand.slug = slug or brand.slug
            brand.save()
            print(brand)
        except Brand.DoesNotExist:
            print(f"Brand with id {id} not found")

def deleteBrand(id):
    # Elminar una marca
    with db:
        Brand.delete_by_id(id)

def truncateBrand():
    # Elminar todas las marcas
    with db:
        q = Brand.delete()
        q.execute()




        

