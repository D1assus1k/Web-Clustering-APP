import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

def clusterization_process(input_csv, output_csv='test.csv'):
    global largest_cluster_name, largest_cluster_size, optimal_silhouette_score
    print('____________________________Функция кластеризации начала свою работу____________________________')
    df = pd.read_csv(input_csv)
    X = StandardScaler().fit_transform(df[['x', 'y']])
    cluster_range = range(2, min(15, len(df) - 1))
    silhouette_scores = [silhouette_score(X, KMeans(n_clusters=n, random_state=0, n_init="auto").fit_predict(X)) for n
                         in cluster_range]
    optimal_clusters = cluster_range[np.argmax(silhouette_scores)]
    optimal_silhouette_score = silhouette_scores[np.argmax(silhouette_scores)]
    print('____________________________Колчество центроидов:', optimal_clusters, '____________________________')
    print('____________________________Коэффициент силуэта:', optimal_silhouette_score, '____________________________')
    kmeans = KMeans(n_clusters=optimal_clusters, random_state=0, n_init="auto").fit(X)
    df['cluster'] = kmeans.labels_
    df['number'] = np.nan
    colors = ['Первое облако', 'Второе облако', 'Третье облако', 'Четвертое облако', 'Пятое облако',
              'Шестое облако', 'Седмое облако', 'Восьмое облако', 'Девятое облако', 'Десятое облако',
              'Одиннадцатое облако', 'Двенадцатое облако', 'Тринадцатое облако', 'Четырнадцатое облако', 'Пятнадцатое облако']
    df['color'] = [colors[c % len(colors)] for c in df['cluster']]
    cluster_sizes = df['cluster'].value_counts()
    largest_cluster_id = cluster_sizes.idxmax()
    largest_cluster_size = cluster_sizes.max()
    largest_cluster_name = colors[largest_cluster_id % len(colors)]
    print(f"Самый большой кластер: {largest_cluster_name} с {largest_cluster_size} точек")
    df[['cluster', 'x', 'y', 'number', 'color']].to_csv(output_csv, index=False)
    print('____________________________Кластеризация произведена____________________________')
    return optimal_clusters, largest_cluster_name, largest_cluster_size, optimal_silhouette_score




