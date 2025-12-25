import pandas as pd
import numpy as np

# Load data asli
df = pd.read_csv("data/housing.csv")

augmented = []

for _ in range(4):  # 1x asli + 4x augment = ~5x
    temp = df.copy()
    temp["area"] = temp["area"] + np.random.normal(0, 5, size=len(df))
    temp["kamar"] = temp["kamar"] + np.random.choice([-1, 0, 1], size=len(df))
    temp["kamar"] = temp["kamar"].clip(1, 10)
    augmented.append(temp)

df_aug = pd.concat([df] + augmented, ignore_index=True)

print("Jumlah data:", len(df_aug))

df_aug.to_csv("data/housing_5000.csv", index=False)
