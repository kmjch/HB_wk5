"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

from sqlalchemy import or_

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.filter(Brand.id == 8).all()

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued is None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
Brand.query.filter(or_(Brand.discontinued is not None, Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)


def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    print db.session.query(Model.name, Model.brand_name, Brand.headquarters).filter(Model.year == year).all()


# def get_brands_summary():
    # '''Prints out each brand name, and each model name for that brand
    #  using only ONE database query.'''

    # query_for_brands = db.session.query(Model.brand_name).all()
    # for brand in query_for_brands:
        # print brand.name
        # find a list of the model names for each brand
        # for model in brand_model_list:
            # print model.name
    # query_for_brands returns an error


# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# A BaseQuery object on which you can call .all(), .one(), .first(), etc.
# It's kind of like you didn't put a ; at the end of your sql call. It's waiting
# for you to say something else too in order to signal you're done with your query
# and for how much output to show.

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

# A diagram that shows the relationship between data in different tables in a
# database. The types of relationships that are shown are one-to-one, one-to-many,
# and many-to-many.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    """ Design a function in python that takes in any string as parameter, and
    returns a list of objects that are brands whose name contains or is equal to
    the input string. """

    # if mystr is a string that doesn't spell out a brand name, add %'s to the
    # string so that it can look for brand names that contain mystr
    if Brand.query.filter(Brand.name.like(mystr)).all() == []:
        mystr = '%' + mystr + '%'
    return Brand.query.filter(Brand.name.like(mystr)).all()


def get_models_between(start_year, end_year):
    """ Design a function that takes in a start year and end year (two integers),
    and returns a list of objects that are models with years that fall between
    the start year (inclusive) and end year (exclusive). """

    return Model.query.filter(Model.year > (start_year - 1), Model.year < (end_year)).all()
