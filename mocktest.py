# Import libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define earthquake parameters (modify these for different test cases)
magnitude_value = 7  # Modify this value (0-10)
depth_value = 3  # Modify this value (0-10)
population_density_value = 8  # Modify this value (0-10)
building_infrastructure_value = 5  # Modify this value (0-10)

# Define fuzzy logic system (same as your code)
magnitude = ctrl.Antecedent(np.arange(0, 11, 1), 'magnitude')
depth = ctrl.Antecedent(np.arange(0, 11, 1), 'depth')
population_density = ctrl.Antecedent(np.arange(0, 11, 1), 'population_density')
building_infrastructure = ctrl.Antecedent(np.arange(0, 11, 1), 'building_infrastructure')

rescue_efforts = ctrl.Consequent(np.arange(0, 11, 1), 'rescue_efforts')
resource_allocation = ctrl.Consequent(np.arange(0, 11, 1), 'resource_allocation')
evacuation_order = ctrl.Consequent(np.arange(0, 11, 1), 'evacuation_order')

# Define membership functions (same as your code)
# ... (all membership function definitions here)

# Create the rule base (same as your code)
# ... (all rule definitions here)

# Create control system and simulation
fis = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])
fis_simulation = ctrl.ControlSystemSimulation(fis)

# Set test case inputs
fis_simulation.input['magnitude'] = magnitude_value
fis_simulation.input['depth'] = depth_value
fis_simulation.input['population_density'] = population_density_value
fis_simulation.input['building_infrastructure'] = building_infrastructure_value

# Run the simulation and print outputs
fis_simulation.compute()

print("Test Case:")
print(f"  Magnitude: {magnitude_value}")
print(f"  Depth: {depth_value}")
print(f"  Population Density: {population_density_value}")
print(f"  Building Infrastructure: {building_infrastructure_value}")

print("\nOutputs:")
print("  Rescue Efforts:", fis_simulation.output['rescue_efforts'])
print("  Resource Allocation:", fis_simulation.output['resource_allocation'])
print("  Evacuation Order:", fis_simulation.output['evacuation_order'])

# Calculate severity with weights (same as your code)
weights = {
    'rescue_efforts': 0.4,
    'resource_allocation': 0.3,
    'evacuation_order': 0.3
}

severity = (fis_simulation.output['rescue_efforts'] * weights['rescue_efforts'] +
            fis_simulation.output['resource_allocation'] * weights['resource_allocation'] +
            fis_simulation.output['evacuation_order'] * weights['evacuation_order'])

print("\nSeverity of the disaster:", severity)
