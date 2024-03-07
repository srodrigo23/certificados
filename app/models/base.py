from app.extensions import db

# Define a base model for other database tables to inherit

class Base(db.Model):

    __abstract__ = True

    date_created = db.Column(
        db.DateTime(),
        default=db.func.current_timestamp()
    )
    date_modified = db.Column(
        db.DateTime(),
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp()
    )

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, data):
        db.session.update(data)
        db.session.commit()
    
    def expunge(self):
        db.session.expunge(self)