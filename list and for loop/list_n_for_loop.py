
# task 1
readings = [12.5, "Error", 18.2, 15.0, "Error", 22.1, 10.8]

for i in range(len(readings)):
    if readings[i] == "Error":
        readings[i] = 0.0
print(f"Cleaned Readings: {readings}")

# task 2
for i in range(len(readings)):
    readings[i] = round(readings[i] * 1.10, 1)
print(f"Calibrated Readings: {readings}")

# task 3
low_quality_log = []
for i in range(len(readings)):
    if readings[i] < 15.0:
        low_quality_log.append(readings[i])
print(f"Low Quality Log: {low_quality_log}")

# Extra Challenge          
readings = [item for item in readings if item >= 15.0]
print("Updated Readings:", readings)
