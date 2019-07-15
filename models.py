from datetime import datetime
from config import db, ma


class Person(db.Model):
    __tablename__ = "person"
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class PersonSchema(ma.ModelSchema):
    class Meta:
        model = Person
        sqla_session = db.session

class CareerProjection(db.Model):
    __tablename__ = "careerProjection"
    occupation_title = db.Column(db.String(64))
    soc_code = db.Column(db.String(32), primary_key=True)
    employment_2016_thousands = db.Column(db.Float)
    employment_2026_thousands =  db.Column(db.Float)
    employment_change_thousands_2026 = db.Column(db.Float)
    employment_change_percent_2026 = db.Column(db.Float)
    openings = db.Column(db.Float)
    median_wage = db.Column(db.Integer)
    entry_level_education = db.Column(db.String(64))
    work_experience_related = db.Column(db.String(64))
    on_the_job_training = db.Column(db.String(64))

class CarreerProjectionSchema(ma.ModelSchema):
    class Meta:
        model = CareerProjection
        sqla_session = db.session
