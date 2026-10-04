import pandas as pd 
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score

def eps_min_sam_opt(x):
  DB = np.zeros(shape=(5,5))
  EPS = list(np.linspace(0.05, 0.2,5))
  for min_sam in range(5,10): 
    for eps in EPS:
        try:
          dbscan_cluster = DBSCAN(eps=eps, min_samples=min_sam+1)
          dbscan_cluster.fit(x)
          Pred = dbscan_cluster.labels_
          db = silhouette_score(x[Pred != -1],Pred[Pred !=-1] )
          DB[EPS.index(eps)][min_sam-5] = round(db, 2) 
        except:
          DB[EPS.index(eps)][min_sam-5] = 0 

  DB = pd.DataFrame(DB)
  for j in range(5) :
    for i in range(5):
      if DB[j][i] == max(DB.max()):
        print('EPS:',EPS[i],'min_samples :',j+5)