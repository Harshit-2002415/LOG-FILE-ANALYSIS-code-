import pandas as pd
import matplotlib.pyplot as plt

log_file = "system.log" 
data = []

with open(log_file, "r") as f:
    for line in f:
        parts = line.strip().split(" ", 3)
        if len(parts) == 4:
            timestamp = parts[0] + " " + parts[1]  
            level = parts[2]                      
            message = parts[3]                     
            data.append([timestamp, level, message])

df = pd.DataFrame(data, columns=["Timestamp", "Level", "Message"])
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

level_counts = df["Level"].value_counts()
print(level_counts)

error_logs = df[df["Level"] == "ERROR"]
error_logs.set_index("Timestamp").resample("1H").count()["Message"].plot(kind="line")
plt.title("Errors per Hour")
plt.xlabel("Time")
plt.ylabel("Error Count")
plt.show()

