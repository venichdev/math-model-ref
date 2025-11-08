"""
EV Calculator - Electric Vehicle Energy & Battery Calculator
===========================================================

A comprehensive, thesis-quality implementation of EV performance calculations
based on validated mathematical models from academic literature.

Modules:
    ev_calculator: Main calculator with all classes and functions

Usage:
    from src.ev_calculator import VehicleParameters, BatteryParameters, EnergyCalculator

    vehicle = VehicleParameters()
    battery = BatteryParameters()
    calc = EnergyCalculator(vehicle, battery, ...)
"""

__version__ = "1.0.0"
__author__ = "Based on math-model-ref repository"
__license__ = "MIT"

# Import main classes for easy access
from .ev_calculator import (
    VehicleParameters,
    BatteryParameters,
    PowertrainParameters,
    AuxiliaryLoads,
    VehicleDynamics,
    BatteryModel,
    EnergyCalculator,
    DriveCycle,
    ModelValidator,
    EVVisualizer
)

__all__ = [
    'VehicleParameters',
    'BatteryParameters',
    'PowertrainParameters',
    'AuxiliaryLoads',
    'VehicleDynamics',
    'BatteryModel',
    'EnergyCalculator',
    'DriveCycle',
    'ModelValidator',
    'EVVisualizer'
]
