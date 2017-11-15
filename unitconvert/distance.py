"""
A python module for converting units of distance
"""
def miles_to_kilometers(miles):
    """
    Convert from units of miles to kilometers

    PARAMETERS
    ----------
    miles: float
        A distance value in units of miles

    RETURNS
    -------
    kilometers: float
        A distance value in units of kilometers
    """
    #convert miles to km:
    return miles*1.60934

def kilometers_to_miles(km):
    """
    Convert from units of kilometers to miles

    PARAMETERS
    ----------
    km: float
        A distance value in units of kilometers

    RETURNS
    -------
    miles: float
        A distance value in units of miles
    """
    #convert km to miles:
    return km*0.621371
