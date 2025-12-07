cluster_summary_num = df.groupby("cluster")[num_cols].mean().round(1)
cluster_sizes = df["cluster"].value_counts()

print(cluster_sizes)
print(cluster_summary_num)

# Найчастіші платформи і емоції в кожному кластері
for c in sorted(df["cluster"].unique()):
    print(f"\nКластер {c}")
    print("Кількість:", cluster_sizes[c])
    print("Топ-платформи:")
    print(df[df["cluster"] == c]["Platform"].value_counts().head())
    print("Топ-емоції (Dominant_Emotion):")
    print(df[df["cluster"] == c]["Dominant_Emotion"].value_counts().head())
