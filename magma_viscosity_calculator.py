import math


VFT_COEFFICIENTS = {
    "Basalt": {"A": -3.0, "B": 2000.0, "C": 300.0},
    "Andesite": {"A": -2.5, "B": 4000.0, "C": 200.0},
    "Dacite": {"A": -2.0, "B": 6000.0, "C": 150.0},
    "Rhyolite": {"A": -1.5, "B": 8000.0, "C": 100.0},
}

MAGMA_TYPES = list(VFT_COEFFICIENTS.keys())

WATER_CORRECTION_PER_WT = 0.4
TEMP_MIN_C = 700.0
TEMP_MAX_C = 1400.0
WATER_MIN_WT = 0.0
WATER_MAX_WT = 8.0


def _validate_inputs(magma_type, temperature_c, water_wt):
    if magma_type not in VFT_COEFFICIENTS:
        raise ValueError(
            "Magma composition must be one of: Basalt, Andesite, Dacite, Rhyolite."
        )

    coeff = VFT_COEFFICIENTS[magma_type]

    try:
        temp = float(temperature_c)
    except (TypeError, ValueError):
        raise ValueError("Temperature must be a number.")

    try:
        water = float(water_wt)
    except (TypeError, ValueError):
        raise ValueError("Water content must be a number.")

    if not math.isfinite(temp):
        raise ValueError("Temperature must be finite.")

    if not math.isfinite(water):
        raise ValueError("Water content must be finite.")

    if temp < TEMP_MIN_C or temp > TEMP_MAX_C:
        raise ValueError(
            f"Temperature must be between {TEMP_MIN_C:.0f} and {TEMP_MAX_C:.0f} °C."
        )

    if water < WATER_MIN_WT or water > WATER_MAX_WT:
        raise ValueError(
            f"Water content must be between {WATER_MIN_WT:.1f} and {WATER_MAX_WT:.1f} wt%."
        )

    denom = temp - coeff["C"]
    if denom <= 0.0:
        raise ValueError("Temperature is too low for this magma composition.")

    return coeff, temp, water


def calculate_viscosity(magma_type, temperature_c, water_wt):
    coeff, temp, water = _validate_inputs(magma_type, temperature_c, water_wt)
    denom = temp - coeff["C"]

    log_eta = coeff["A"] + coeff["B"] / denom - WATER_CORRECTION_PER_WT * water
    eta = 10.0**log_eta

    return log_eta, eta


def calculate_log10_viscosity(magma_type, temperature_c, water_wt):
    log_eta, _ = calculate_viscosity(magma_type, temperature_c, water_wt)
    return log_eta


def compute_viscosity_curve(magma_type, temperature_c, water_wt, points=101):
    coeff, temp, water = _validate_inputs(magma_type, temperature_c, water_wt)

    low = max(TEMP_MIN_C, temp - 50.0)
    high = min(TEMP_MAX_C, temp + 50.0)

    if points < 2:
        points = 2

    temperatures = []
    log_values = []
    eta_values = []

    for i in range(points):
        t = low + (high - low) * i / (points - 1)
        denom = t - coeff["C"]

        if denom <= 0.0:
            continue

        log_eta = coeff["A"] + coeff["B"] / denom - WATER_CORRECTION_PER_WT * water
        eta = 10.0**log_eta

        temperatures.append(t)
        log_values.append(log_eta)
        eta_values.append(eta)

    return temperatures, log_values, eta_values
