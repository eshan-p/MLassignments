# Tweet Clustering using K-Means

- file(s): tweetClustering.py

- built & ran using Google Colab

- libraries/imports used:
    - re (regex for preprocessing tweets)
    - requests (loading text file from GitHub repo)
    - random (initial logic for k-means function)

- 'cnnhealth.txt' file used from UCI dataset provided in assignment
    - program may take up to ~3 minutes to build & run due to size of text file

- 'Table of results' printed in console output
    - example provided below:

    - Value of K: 20
      SSE: 3201.132343684662
      Cluster sizes:
        Cluster 1: 371 tweets
        Cluster 2: 310 tweets
        Cluster 3: 37 tweets
        Cluster 4: 326 tweets
        Cluster 5: 174 tweets
        Cluster 6: 88 tweets
        Cluster 7: 37 tweets
        Cluster 8: 266 tweets
        Cluster 9: 269 tweets
        Cluster 10: 43 tweets
        Cluster 11: 499 tweets
        Cluster 12: 97 tweets
        Cluster 13: 244 tweets
        Cluster 14: 136 tweets
        Cluster 15: 174 tweets
        Cluster 16: 319 tweets
        Cluster 17: 64 tweets
        Cluster 18: 377 tweets
        Cluster 19: 139 tweets
        Cluster 20: 91 tweets
      
      Value of K: 10
      SSE: 3316.638963273725
      Cluster sizes:
        Cluster 1: 832 tweets
        Cluster 2: 349 tweets
        Cluster 3: 433 tweets
        Cluster 4: 215 tweets
        Cluster 5: 920 tweets
        Cluster 6: 247 tweets
        Cluster 7: 446 tweets
        Cluster 8: 147 tweets
        Cluster 9: 308 tweets
        Cluster 10: 164 tweets
      
      Value of K: 5
      SSE: 3444.025327154853
      Cluster sizes:
        Cluster 1: 1520 tweets
        Cluster 2: 1020 tweets
        Cluster 3: 941 tweets
        Cluster 4: 441 tweets
        Cluster 5: 139 tweets
      
      Value of K: 3
      SSE: 3517.690233226645
      Cluster sizes:
        Cluster 1: 1588 tweets
        Cluster 2: 739 tweets
        Cluster 3: 1734 tweets

      Value of K: 1
      SSE: 3651.683146575215
      Cluster sizes:
        Cluster 1: 4061 tweets
