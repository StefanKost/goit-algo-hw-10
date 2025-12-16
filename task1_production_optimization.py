from pulp import LpMaximize, LpProblem, LpVariable, LpStatus, value, COIN_CMD, PULP_CBC_CMD
from shutil import which

# Create the optimization model
model = LpProblem(name="fresh-drinks-production", sense=LpMaximize)

# Define decision variables (non-negative integers)
lemonade = LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Objective function
model += lemonade + fruit_juice, "Total Production"

# Resource constraints
# Water: max 100 units (lemonade requires 2 units, fruit juice 1 unit)
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"

# Sugar: max 50 units (lemonade requires 1 unit)
model += 1 * lemonade <= 50, "Sugar Constraint"

# Lemon juice: max 30 units (lemonade requires 1 unit)
model += 1 * lemonade <= 30, "Lemon Juice Constraint"

# Fruit puree: max 40 units (fruit juice requires 2)
model += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Solve the problem
try:
    # Try default PuLP solver
    status = model.solve(PULP_CBC_CMD(msg=False))
except Exception as e:
    # Fallback for Apple Silicon
    cbc_path = which("cbc")
    if cbc_path:
        status = model.solve(COIN_CMD(path=cbc_path, msg=False))
    else:
        raise e

print(f"\nSolve status: {LpStatus[status]}")

print(f"Optimal Production:")
print(f" -> Lemonade:    {int(value(lemonade))} units")
print(f" -> Fruit Juice: {int(value(fruit_juice))} units")
print(f"Total Products: {int(value(model.objective))} units")
