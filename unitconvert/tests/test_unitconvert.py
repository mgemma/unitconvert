import pytest
import unitconvert.distance as dist
import unitconvert.temperature as temp

def test_miles_to_kilometers():
    #known result, one mile equals 1.60934 kilometers
    assert dist.miles_to_kilometers(1) == 1.60934

    # check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        dist.miles_to_kilometers(1, 2)


def test_kilometers_to_miles():
    #known result, one km equals 0.621371 miles
    assert dist.kilometers_to_miles(1) == 0.621371

    # check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        dist.kilometers_to_miles(1, 2)


def test_fahrenheit_to_celsius():
    #known result, 32 deg Fahrenheit equals 0 deg Celsius
    assert temp.fahrenheit_to_celsius(32) == 0

    # check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        temp.fahrenheit_to_celsius(1, 2)


def test_celsius_to_fahrenheit():
    #known result, 0 Celsius equals 32 deg Fahrenheit
    assert temp.celsius_to_fahrenheit(0) == 32

    # check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        temp.celsius_to_fahrenheit(1, 2)
