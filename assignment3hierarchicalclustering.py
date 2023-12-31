# -*- coding: utf-8 -*-
"""Assignment3HierarchicalClustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XKTmO8P6tX2ZDDmEdaDZYmW1yunWwyPM
"""

from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split

data = fetch_olivetti_faces()
X, y = data.data, data.target

"""Step 2"""

X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, stratify=y_temp, random_state=42)

"""Step 3"""

from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
import numpy as np

svc = SVC(gamma='auto')
cross_val_scores = cross_val_score(svc, X_train, y_train, cv=5)

print(f"Average 5-Fold CV Score: {np.mean(cross_val_scores)}")

"""Step 4a"""

from sklearn.cluster import AgglomerativeClustering

euclidean_clustering = AgglomerativeClustering(distance_threshold=0, n_clusters=None, metric='euclidean', linkage='ward')
euclidean_clusters = euclidean_clustering.fit(X)

"""4b"""

minkowski_clustering = AgglomerativeClustering(distance_threshold=0, n_clusters=None, metric='manhattan', linkage='average')
minkowski_clusters = minkowski_clustering.fit(X)

"""4c"""

cosine_clustering = AgglomerativeClustering(distance_threshold=0, n_clusters=None, metric='cosine', linkage='average')
cosine_clusters = cosine_clustering.fit(X)

"""Step 5"""

from sklearn.metrics import silhouette_score

def silhouette_scores(X, metric, linkage):
    for n_clusters in range_n_clusters:
        clusterer = AgglomerativeClustering(n_clusters=n_clusters, metric=metric, linkage=linkage)
        preds = clusterer.fit_predict(X)
        score = silhouette_score(X, preds)
        print("For n_clusters =", n_clusters, "with metric", metric, "The average silhouette_score is :", score)

silhouette_scores(X, 'euclidean', 'ward')
silhouette_scores(X, 'manhattan', 'average')
silhouette_scores(X, 'cosine', 'average')

"""Step 6"""

from sklearn.cluster import AgglomerativeClustering
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, KFold
import numpy as np

configs = {
    'euclidean': {'metric': 'euclidean', 'linkage': 'ward'},
    'manhattan': {'metric': 'manhattan', 'linkage': 'average'},
    'cosine': {'metric': 'cosine', 'linkage': 'average'},
}

avg_cv_scores = {}

for config_name, params in configs.items():
    clusterer = AgglomerativeClustering(n_clusters=n_clusters, **params)
    X_transformed = clusterer.fit_predict(X)
    X_transformed = X_transformed.reshape(-1, 1)

    classifier = RandomForestClassifier(random_state=42)
    cv = KFold(n_splits=5, shuffle=True, random_state=42)
    cv_scores = cross_val_score(classifier, X_transformed, y, cv=cv)

    avg_cv_scores[config_name] = np.mean(cv_scores)

avg_cv_scores