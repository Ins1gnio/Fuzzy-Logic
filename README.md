# Fuzzy Logic and Clustering
This repo. consist of fuzzy logic, and clustering (HCM and Fuzzy Clustering).

## Fuzzy Logic
Fuzzy Logic fully created in python (without Scikit Lib.), created for "Fundamental of Intelligent System" Class, BME. This code consist of 2 Input Membership Function (IMF) and 1 Output Membership Function (OMF), which together with the linguistic term is plotted using matplotlib. The rule-base is printed by grid. Fuzzy Inference System (FIS) is implemented using Mamdani max - min method. Defuzzification procedure done using centroid method (CoG of the shape). Code is based on an example to find body condition, with 2 inputs (height and weight).

## HCM Clustering
Its better to write a code about Hard-c means (HCM) before doing fuzzy clustering, since it is the basic of the algorithm which mainly dealing with crisp value. So, in this repo. I upload the code about HCM, which I think it is not as complex fuzzy clustering. Code is based on book reference by Timothy J. Ross (Fuzzy Logic with Engineering Application, pp. 371).

## FCM Clustering
Algorithm for Fuzzy-c means (FCM) made by doing some modification related to the equation used to find the center cluster and updating the u matrix value. New parameter can be seen, which includes fuzzy weight (m') and error tolerance. Code is based on book reference by Timothy J. Ross (Fuzzy Logic with Engineering Application, pp. 379).
