from blanco.database import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Float
from sqlalchemy import Integer


class PickingItem(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    picking_id = Column(Integer, ForeignKey("picking.id"))
    product_id = Column(Integer, ForeignKey("product.id"))
    sku_id = Column(Integer, ForeignKey("sku.id"))
    location_id = Column(Integer, ForeignKey("Location.id"))
    inventory_id = Column(Integer, ForeignKey("Inventory.id"))
    stock = Column(Float)
    unit_id = Column(Integer, ForeignKey("unit.id"))
    create_at = Column(DateTime)
    update_at = Column(DateTime)

    def __init__(self, picking_id, product_id, sku_id, location_id, inventory_id, stock, unit_id, create_at, update_at):
        self.picking_id = picking_id
        self.product_id = product_id
        self.sku_id = sku_id
        self.location_id = location_id
        self.inventory_id = inventory_id
        self.stock = stock
        self.unit_id = unit_id
        self.create_at = create_at
        self.update_at = update_at

    def __repr__(self):
        return "<picking item {}>".format(self.id)

