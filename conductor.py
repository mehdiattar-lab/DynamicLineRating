from collections import namedtuple
import nusselt

ConductorConstants = namedtuple(
    "ConductorConstants",
    [
        "stranded",
        "high_rs",
        "diameter",
        "cross_section",
        "absortivity",
        "emmisivity",
        "materials_heat",
        "resistance",
    ],
)

HeatMaterial = namedtuple(
    "HeatMaterial", ["name", "mass_per_unit_length", "specific_heat_20deg", "beta"]
)


def drake_resistance(conductor_temperature): # this assumes that the resistance increase is linear to the chanegs of conductor temperature
    # at_25 = 7.283e-5
    # at_75 = 8.688e-5

    at_20 = 9.42e-5
    at_75 = 11.22e-5

    per_1 = (at_75 - at_20) / (75 - 20)

    resistance = at_20 + (conductor_temperature - 20) * per_1
    return resistance


# From CIGRE601 examples
drake_constants = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=28.1e-3,
    cross_section=None,
    absortivity=0.8,
    emmisivity=0.8,
    materials_heat=[
        HeatMaterial("steel", 0.5119, 481, 1.00e-4),
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
    ],
    resistance=drake_resistance,
)

drake_constants_ieee738 = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=24.2e-3,
    cross_section=None,
    absortivity=0.8,
    emmisivity=0.8,
    materials_heat=[
        HeatMaterial("steel", 0.310, 481, 1.00e-4),
        HeatMaterial("aluminum", 0.849, 897, 3.80e-4),
    ],
    resistance=drake_resistance,
)

drake_constants_example_b = ConductorConstants(
    stranded=True,
    high_rs=True,
    diameter=28.1e-3,
    cross_section=None,
    absortivity=0.9,
    emmisivity=0.9,
    materials_heat=[
        HeatMaterial("steel", 0.5119, 481, 1.00e-4),
        HeatMaterial("aluminum", 1.116, 897, 3.80e-4),
    ],
    resistance=drake_resistance,
)
