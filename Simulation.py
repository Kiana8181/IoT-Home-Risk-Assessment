import random

def generate_weather():
    weather_prob = random.uniform(0, 1)
    if weather_prob < 0.3:
        return 'Rainy', weather_prob
    else:
        return 'Sunny', weather_prob

def generate_window_open(weather):
    window_open_prob = random.uniform(0, 1)
    if (weather == 'Rainy' and window_open_prob < 0.1) or (weather == 'Sunny' and window_open_prob < 0.8):
        return True, window_open_prob
    else:
        return False, window_open_prob

def generate_door_locked():
    door_locked_prob = random.uniform(0, 1)
    return True if door_locked_prob < 0.9 else False, door_locked_prob

def generate_security_system():
    security_system_prob = random.uniform(0, 1)
    return 'On' if security_system_prob < 0.8 else 'Off', security_system_prob

def generate_burglar_alarm(security_system):
    burglar_alarm_prob = random.uniform(0, 1)
    if (security_system == 'On' and burglar_alarm_prob < 0.95) or (security_system == 'Off' and burglar_alarm_prob < 0.1):
        return 'On', burglar_alarm_prob
    else:
        return 'Off', burglar_alarm_prob

def generate_fire_alarm(fire):
    fire_alarm_prob = random.uniform(0, 1)
    if (fire and fire_alarm_prob < 0.9) or (not fire and fire_alarm_prob < 0.05):
        return 'On', fire_alarm_prob
    else:
        return 'Off', fire_alarm_prob

def generate_burglary(burglar_alarm, door_locked):
    burglary_prob = random.uniform(0, 1)
    if burglar_alarm == 'On' and door_locked:
        return True if burglary_prob < 0.01 else False, burglary_prob
    elif burglar_alarm == 'On' and not door_locked:
        return True if burglary_prob < 0.1 else False, burglary_prob
    elif burglar_alarm == 'Off' and door_locked:
        return True if burglary_prob < 0.3 else False, burglary_prob
    else:
        return True if burglary_prob < 0.8 else False, burglary_prob

def generate_fire(window_open):
    fire_prob = random.uniform(0, 1)
    if (window_open and fire_prob < 0.05) or (not window_open and fire_prob < 0.01):
        return True, fire_prob
    else:
        return False, fire_prob

def simulate_smart_home():
    weather, weather_prob = generate_weather()
    window_open, window_open_prob = generate_window_open(weather)
    door_locked, door_locked_prob = generate_door_locked()
    security_system, security_system_prob = generate_security_system()
    fire, fire_prob = generate_fire(window_open)
    fire_alarm, fire_alarm_prob = generate_fire_alarm(fire)
    burglar_alarm, burglar_alarm_prob = generate_burglar_alarm(security_system)
    burglary, burglary_prob = generate_burglary(burglar_alarm, door_locked)

    return {
        'Weather': (weather, weather_prob),
        'Window Open': (window_open, window_open_prob),
        'Door Locked': (door_locked, door_locked_prob),
        'Security System': (security_system, security_system_prob),
        'Fire': (fire, fire_prob),
        'Fire Alarm': (fire_alarm, fire_alarm_prob),
        'Burglar Alarm': (burglar_alarm, burglar_alarm_prob),
        'Burglary': (burglary, burglary_prob)
    }

def analyze_risks(simulations):
    burglary_count = sum(1 for sim in simulations if sim['Burglary'][0])
    fire_count = sum(1 for sim in simulations if sim['Fire'][0])

    burglary_risk = burglary_count / len(simulations)
    fire_risk = fire_count / len(simulations)

    return {
        'Burglary Risk': burglary_risk,
        'Fire Risk': fire_risk
    }

def print_simulation(simulation):
    print("Generated data and probabilities:")
    for key, value in simulation.items():
        print(f"{key}: {value[0]}, Probability: {value[1]:.2f}")

def main():
    num_simulations = 10000
    simulations = [simulate_smart_home() for _ in range(num_simulations)]

    for i, simulation in enumerate(simulations):
        print(f"Simulation {i + 1}:")
        print_simulation(simulation)
        print("------------------------------")

    risks = analyze_risks(simulations)

    print(f"Simulated {num_simulations} smart homes")
    print(f"Burglary Risk: {risks['Burglary Risk']:.2%}")
    print(f"Fire Risk: {risks['Fire Risk']:.2%}")

if __name__ == "__main__":
    main()