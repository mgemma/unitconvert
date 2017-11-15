"""
A python module to convert between temperature scales
"""

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius

    PARAMETERS
    ----------
    fahrenheit: float
        A temperature value in units of Fahrenheit

    RETURNS
    -------
    celsius: float
        A temperature value in units of Celsius
    """
    #convert temperature:
    return (fahrenheit-32)*(5/9)

def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit

    PARAMETERS
    ----------
    celsius: float
        A temperature value in units of Celsius

    RETURNS
    -------
    fahrenheit: float
        A temperature value in units of Fahrenheit
    """
    #convert temperature:
    return celsius*(9/5)+32
