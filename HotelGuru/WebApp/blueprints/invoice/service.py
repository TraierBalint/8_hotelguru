from WebApp.extensions import db
from WebApp.models.invoice import Invoice
from WebApp.blueprints.invoice.schemas import InvoiceRequestSchema, InvoiceResponseSchema
from sqlalchemy import select
from WebApp.models.reservation import Reservation
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

            # Hozzáadjuk a szobák árait
            for rr in reservation.reservation_rooms:
                total_price += rr.room.price

            # Hozzáadjuk az extra szolgáltatások árait
            for es in reservation.extraservices:
                total_price += es.price

            invoice = Invoice(
                reservation_id=reservation.id,
                total_amount=total_price,
                issued_at=datetime.now()
            )

            db.session.add(invoice)
            db.session.commit()
            return True, InvoiceResponseSchema().dump(invoice)
        
        except Exception as ex:
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
    
    @staticmethod
    def update(invoice_id, data):
        invoice = db.session.get(Invoice, invoice_id)
        if not invoice:
            return False, "Invoice not found."

        try:
            for key, value in data.items():
                if key == "issued_at" and isinstance(value, str):
                    value = datetime.fromisoformat(value).date()

                setattr(invoice, key, value)
            db.session.commit()
        except Exception as ex:
            return False, str(ex)
        return True, invoice

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
