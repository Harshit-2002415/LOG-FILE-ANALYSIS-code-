import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load log file
log_file = "system.log"   # replace with your log filename
data = []

with open(log_file, "r") as f:
    for line in f:
        parts = line.strip().split(" ", 3)
        if len(parts) == 4:
            timestamp = parts[0] + " " + parts[1]   # date + time
            level = parts[2]                        # INFO, ERROR, etc.
            message = parts[3]                      # actual message
            data.append([timestamp, level, message])

# Step 2: Convert into DataFrame
df = pd.DataFrame(data, columns=["Timestamp", "Level", "Message"])
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Step 3: Count log levels
level_counts = df["Level"].value_counts()
print(level_counts)

# Step 4: Plot errors over time
error_logs = df[df["Level"] == "ERROR"]
error_logs.set_index("Timestamp").resample("1H").count()["Message"].plot(kind="line")
plt.title("Errors per Hour")
plt.xlabel("Time")
plt.ylabel("Error Count")
plt.show()
