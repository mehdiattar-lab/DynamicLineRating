__version__ = "1.0.0"

import cigre601
import ieee738


def thermal_rating(*args, standard="cigre", **kwargs):
    """Calculate the rating.

    ambient_temperature:   temperature of air in [°C]
    wind_speed:            in [m/s]
    angle_of_attack:       the angle between the wind and the conductor in [°]. 0° is parallel wind, 90° is perpendicular
    solar_irradiation:     in [W/m^2]
    conductor:             the conductor structure with details about the material. from pylinerating.conductor
    conductor_temperature: the target conductor temperature [°C]
    horizontal_angle:      not used
    elevation:             the see level elevation in [m]
    standard:              either `cigre` of `ieee`
    """

    if standard == "cigre":
        try:
            current=cigre601.thermal_rating(*args, **kwargs)
            print(current)
            return current
        except Exception as e:
            print("An error occurred:", e) 
    elif standard == "ieee":
        current=ieee738.thermal_rating(*args, **kwargs)
        #print(current)
        return current

    #raise ValueError("Invalid argument: standard must be cigre or ieee.")
