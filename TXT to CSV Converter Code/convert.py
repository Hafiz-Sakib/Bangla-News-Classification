import os
import pandas as pd

# Root folder containing all category folders
root_dir = "./"


data = []

# Loop through each category folder
for category in os.listdir(root_dir):
    category_path = os.path.join(root_dir, category)
    
    if os.path.isdir(category_path):
        for file in os.listdir(category_path):
            if file.endswith(".txt"):
                file_path = os.path.join(category_path, file)
                with open(file_path, "r", encoding="utf-8-sig") as f:
                    text = f.read().strip()
                    data.append([text, category.lower()])  # Label = folder name

# Create DataFrame
df = pd.DataFrame(data, columns=["text", "label"])

# Shuffle and save to CSV
df = df.sample(frac=1, random_state=42).reset_index(drop=True)
df.to_csv("news_dataset.csv", index=False, encoding='utf-8-sig')



print("✅ Dataset created successfully! Shape:", df.shape)
df.head()
