
from thermostat_control import target_temperature, hvac_action, energy_alert


# TARGET TEMPERATURE TESTS

def test_away_mode():
    assert target_temperature("away", True, 12) == 16

def test_sleep_mode_night():
    assert target_temperature("sleep", True, 23) == 18

def test_sleep_mode_day():
    assert target_temperature("sleep", True, 12) == 20

def test_unoccupied():
    assert target_temperature("home", False, 12) == 18

def test_morning_temperature():
    assert target_temperature("home", True, 7) == 22

def test_evening_temperature():
    assert target_temperature("home", True, 18) == 21

def test_normal_temperature():
    assert target_temperature("home", True, 12) == 20


# HVAC ACTION TESTS

def test_hvac_idle():
    assert hvac_action(20, 20.5, 10) == "idle"

def test_heat_boost():
    assert hvac_action(15, 22, 2) == "heat_boost"

def test_heat():
    assert hvac_action(15, 22, 10) == "heat"

def test_cool_boost():
    assert hvac_action(25, 20, 35) == "cool_boost"

def test_cool():
    assert hvac_action(25, 20, 25) == "cool"


# ENERGY ALERT TESTS

def test_energy_ok():
    assert energy_alert([5, 7, 8], 10) == "ok"

def test_energy_warning():
    assert energy_alert([15, 5, 8], 10) == "warning"

def test_energy_critical():
    assert energy_alert([15, 16, 17], 10) == "critical"
