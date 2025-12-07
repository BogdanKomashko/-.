import pandas as pd
import numpy as np

# 1. Завантаження основного датасету
df = pd.read_csv("social_media_emotions.csv")

# Якщо раптом в CSV є дивні текстові рядки (типу "Tabii, ..."),
# можна викинути рядки, де Age не можна привести до числа:
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df = df.dropna(subset=["Age"])

# Приведемо інші числові колонки
num_cols = [
    "Age",
    "Daily_Usage_Time (minutes)",
    "Posts_Per_Day",
    "Likes_Received_Per_Day",
    "Comments_Received_Per_Day",
    "Messages_Sent_Per_Day",
]

for col in num_cols[1:]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=num_cols)  # викинути рядки з NaN у числових

# Категоріальні змінні
cat_cols = ["Gender", "Platform"]

# Optionally: обрізаємо пробіли
for c in cat_cols + ["Dominant_Emotion"]:
    df[c] = df[c].astype(str).str.strip()

print(df.head())
print(df.dtypes)
print(df["Dominant_Emotion"].value_counts())
