# Adam Beigel
# 8 December 2023

with open('api_key_bus.txt') as f:
    bus_key = f.read().strip()

with open('api_key_train.txt') as f:
    train_key = f.read().strip()

print(f"bus key: {bus_key}")
print(f"train key: {train_key}")
