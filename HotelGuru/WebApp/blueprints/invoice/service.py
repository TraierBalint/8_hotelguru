from WebApp.extensions import db
from WebApp.models.invoice import Invoice
from WebApp.blueprints.invoice.schemas import InvoiceRequestSchema, InvoiceResponseSchema
from sqlalchemy import select
from WebApp.models.reservation import Reservation
from WebApp.models.invoceItem  import InvoiceItem
from WebApp.models.reservation_rooms import ReservationRoom
from WebApp.models.extraservice import ExtraService
from datetime import datetime
class InvoiceService:

    @staticmethod
    def create(data):
        reservation = db.session.get(Reservation, data["reservation_id"])
        if not reservation:
            return False, "Reservation not found."

        try:
            total_price = 0
            invoice_items = []
            item_map = {}

            # Szobák hozzáadása
            for rr in reservation.reservation_rooms:
                room = rr.room
                total_price += room.price

                key = ("room", room.name)
                if key in item_map:
                    #Mikor dict frissül akkor a list is frissül, mert a memóriába mindkettő ugyanoda mutat
                    item_map[key].quantity += 1
                else:
                    item = InvoiceItem(
                        item_type="room",
                        item_id=room.id,
                        name=room.name,
                        price=room.price,
                        quantity=1
                    )
                    item_map[key] = item
                    invoice_items.append(item)

            # Extra szolgáltatások hozzáadása
            for es in reservation.extraservices:
                total_price += es.price

                key = ("extra_service", es.name)
                if key in item_map:
                    item_map[key].quantity += 1
                else:
                    item = InvoiceItem(
                        item_type="extra_service",
                        item_id=es.id,
                        name=es.name,
                        price=es.price,
                        quantity=1
                    )
                    item_map[key] = item
                    invoice_items.append(item)

            # Számla létrehozása
            invoice = Invoice(
            reservation_id=reservation.id,
            total_amount=total_price,
            issued_at=datetime.now(),
            items=invoice_items
        )

            db.session.add(invoice)
            db.session.commit()
            return True, InvoiceResponseSchema().dump(invoice)
        
        except Exception as ex:
            db.session.rollback()
            return False, str(ex)
        
    @staticmethod
    def get_by_id(invoice_id):
        invoice = db.session.get(Invoice, invoice_id)
        if not invoice:
            return False, "Invoice not found."
        return True, InvoiceResponseSchema().dump(invoice)    
    
    @staticmethod
    def list_all():
        invoices = db.session.execute(select(Invoice)).scalars().all()
        return True, InvoiceResponseSchema(many=True).dump(invoices)
    
    
    #1. módosítani lehet a kiállítási dátumot manuálisan
    #2. lesz majd egy lista az itemekről ott még fel tudunk venni újat illetve a mennyiségét tudjuk módosítani és akár eltávolítani a számlából
    #3. a végösszeg újra számolódik 
    @staticmethod
    def update(invoice_id, data):
        invoice = db.session.get(Invoice, invoice_id)
        if not invoice:
            return False, "Invoice not found."

        try:
            # Dátum frissítése, ha jön
            if "issued_at" in data and isinstance(data["issued_at"], str):
                invoice.issued_at = datetime.fromisoformat(data["issued_at"])

            # Tételek frissítése
            if "items" in data:
                invoice.items.clear()
                total_price = 0

                for item_data in data["items"]:
                    item = InvoiceItem(
                        item_type=item_data["item_type"],
                        item_id=item_data["item_id"],
                        name=item_data["name"],
                        price=item_data["price"],
                        quantity=item_data["quantity"]
                    )
                    total_price += item.price * item.quantity
                    invoice.items.append(item)

                invoice.total_amount = total_price

            db.session.commit()
            return True, InvoiceResponseSchema().dump(invoice)

        except Exception as ex:
            db.session.rollback()
            return False, str(ex)


    @staticmethod
    def delete(invoice_id):
        invoice = db.session.get(Invoice, invoice_id)
        if not invoice:
            return False, "Invoice not found."

        try:
            db.session.delete(invoice)
            db.session.commit()
        except Exception as ex:
            return False, str(ex)

        return True, "Invoice deleted successfully."
