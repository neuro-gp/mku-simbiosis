from src.models import db, ImportGroup, ImportData

from pandas import read_csv
from datetime import datetime

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