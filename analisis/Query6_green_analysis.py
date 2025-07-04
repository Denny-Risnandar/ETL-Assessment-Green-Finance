# green_analysis.py

def compute_co2_efficiency(co2_reduction, investment_cost):
    try:
        efficiency = co2_reduction / (investment_cost * 1_000)
        return round(efficiency, 2)
    except ZeroDivisionError:
        return "Cannot compute"
