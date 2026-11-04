!pip install -q scikit-fuzzy numpy matplotlib scikit-learn

import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

density = ctrl.Antecedent(np.arange(0, 51, 1), 'density')
waiting = ctrl.Antecedent(np.arange(0, 121, 1), 'waiting')
green = ctrl.Consequent(np.arange(10, 91, 1), 'green')

density['low'] = fuzz.trapmf(density.universe, [0, 0, 10, 20])
density['medium'] = fuzz.trimf(density.universe, [10, 25, 40])
density['high'] = fuzz.trapmf(density.universe, [30, 40, 50, 50])

waiting['short'] = fuzz.trapmf(waiting.universe, [0, 0, 20, 40])
waiting['moderate'] = fuzz.trimf(waiting.universe, [20, 60, 100])
waiting['long'] = fuzz.trapmf(waiting.universe, [80, 100, 120, 120])

green['short'] = fuzz.trapmf(green.universe, [10, 10, 20, 35])
green['medium'] = fuzz.trimf(green.universe, [25, 50, 75])
green['long'] = fuzz.trapmf(green.universe, [65, 75, 90, 90])

rules = [
    ctrl.Rule(density['low'] & waiting['short'], green['short']),
    ctrl.Rule(density['low'] & waiting['moderate'], green['short']),
    ctrl.Rule(density['low'] & waiting['long'], green['medium']),
    ctrl.Rule(density['medium'] & waiting['short'], green['short']),
    ctrl.Rule(density['medium'] & waiting['moderate'], green['medium']),
    ctrl.Rule(density['medium'] & waiting['long'], green['long']),
    ctrl.Rule(density['high'] & waiting['short'], green['medium']),
    ctrl.Rule(density['high'] & waiting['moderate'], green['long']),
    ctrl.Rule(density['high'] & waiting['long'], green['long'])
]

system = ctrl.ControlSystem(rules)

traffic = float(input("Enter traffic density (0-50 vehicles): "))
wait = float(input("Enter waiting time (0-120 seconds): "))

if not 0 <= traffic <= 50 or not 0 <= wait <= 120:
    raise ValueError("Input values are outside the allowed range.")

simulation = ctrl.ControlSystemSimulation(system)
simulation.input['density'] = traffic
simulation.input['waiting'] = wait
simulation.compute()

result = simulation.output['green']

print(f"Predicted Green Light Duration: {result:.2f} seconds")

density.view()
plt.title("Traffic Density Membership Functions")
plt.tight_layout()
plt.show()

waiting.view()
plt.title("Waiting Time Membership Functions")
plt.tight_layout()
plt.show()

green.view()
plt.title("Green Light Duration Membership Functions")
plt.tight_layout()
plt.show()