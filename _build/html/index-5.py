from numpy import array 
from scipy.cluster.hierarchy import dendrogram, linkage
import scipy.cluster.hierarchy 
import halla

x = array([[0.1,0.2,0.3,0.4],[1,1,1,0],[0.01,0.04,0.09,0.16],[0,0,0,1]])

lxspearman = halla.hierarchy.hclust( x, pdist_metric = lambda u,v: halla.distance.cord(u,v,method="spearman") )

dendrogram(lxspearman)