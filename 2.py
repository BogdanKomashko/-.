from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans

features = num_cols + cat_cols  # все, крім Dominant_Emotion

X = df[features]

preprocess = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_cols),
    ]
)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

cluster_pipeline = Pipeline(steps=[
    ("preprocess", preprocess),
    ("kmeans", kmeans),
])

cluster_pipeline.fit(X)

df["cluster"] = cluster_pipeline["kmeans"].labels_
