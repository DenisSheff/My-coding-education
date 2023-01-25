import data_provider as pd
import logger as log


def temperature_value_view(sensor):
    data = pd.get_temperature(sensor)
    log.temperature_logger(data)
    return data


def pressure_value_view(sensor):
    data = pd.get_pressure(sensor)
    log.pressure_logger(data)
    return data


def wind_value_view(sensor):
    data = pd.get_wind_speed(sensor)
    log.wind_logger(data)
    return data
