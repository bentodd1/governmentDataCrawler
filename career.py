from flask import make_response, abort
from config import db
from models import CarreerProjectionSchema,CareerProjection


def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        json string of list of people
    """
    # Create the list of people from our data
    careerProjection = CareerProjection.query.all()

    # Serialize the data for the response
    career_schema = CarreerProjectionSchema(many=True)
    data = career_schema.dump(careerProjection).data
    return data