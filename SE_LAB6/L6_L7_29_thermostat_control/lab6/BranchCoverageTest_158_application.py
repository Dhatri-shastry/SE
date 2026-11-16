
from thermostat_control import target_temperature, hvac_action, energy_alert


# TARGET TEMPERATURE - BRANCH TESTS


def test_away_branch():
    assert target_temperature("away", True, 12) == 16

def test_sleep_before_6():
    assert target_temperature("sleep", True, 5) == 18

def test_sleep_after_22():
    assert target_temperature("sleep", True, 23) == 18

def test_sleep_during_day():
    assert target_temperature("sleep", True, 12) == 20

def test_unoccupied_branch():
    assert target_temperature("home", False, 12) == 18

def test_morning_branch():
    assert target_temperature("home", True, 7) == 22

def test_not_morning_branch():
    assert target_temperature("home", True, 12) == 20

def test_evening_branch():
    assert target_temperature("home", True, 18) == 21

def test_not_evening_branch():
    assert target_temperature("home", True, 12) == 20


# HVAC ACTION - BRANCH TESTS

def test_idle_branch():
    assert hvac_action(20, 20.5, 10) == "idle"

def test_heat_boost_branch():
    assert hvac_action(15, 22, 2) == "heat_boost"

def test_heat_normal_branch():
    assert hvac_action(15, 22, 5) == "heat"

def test_cool_boost_branch():
    assert hvac_action(25, 20, 35) == "cool_boost"

def test_cool_normal_branch():
    assert hvac_action(25, 20, 30) == "cool"


# ENERGY ALERT - BRANCH TESTS

def test_empty_readings():
    assert energy_alert([], 10) == "ok"

def test_no_readings_over_limit():
    assert energy_alert([5, 8, 10], 10) == "ok"

def test_warning_branch():
    assert energy_alert([11, 10, 9], 10) == "warning"

def test_critical_branch():
    assert energy_alert([11, 12, 10], 10) == "critical"
