import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# https://www.linkedin.com/pulse/k-means-clustering-its-real-world-use-case-pratik-kohad-1c/

# the elbow method may not be the most efficient method of finding the K
# thats where the Silhouette score method comes in
# https://towardsdatascience.com/elbow-method-is-not-sufficient-to-find-best-k-in-k-means-clustering-fc820da0631d

x = [4, 5, 10, 4, 3, 11, 14, 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

# plt.scatter(x, y)
# plt.show()

data = list(zip(x, y))


def elbow(theData):
    inertias = []

    for i in range(1, 11):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(theData)
        inertias.append(kmeans.inertia_)

    plt.plot(range(1, 11), inertias, marker='o')
    plt.title('Elbow method')
    plt.xlabel('Number of clusters')
    plt.ylabel('Inertia')
    plt.show()


# after looking at the visuals, the elbow point might look like 2
# so fit the data

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()

# just like that, things got clustered
