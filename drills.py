import pandas as pd

data = pd.read_csv("50_states.csv")

if "Ohio" in data.state.values:
    row = data[data["state"] == "Ohio"]
    x = int(row.x.item())
    y = int(row.y.item())
    print(f"Ohio is located at: {x}, {y}")