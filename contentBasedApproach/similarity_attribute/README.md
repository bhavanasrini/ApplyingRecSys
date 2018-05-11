Distance is computed for all features

Ordinal Attribute :  Grade
Compute ranking of an attribute; rank = {1,…,M}, M is higher rank. 
Distance between two user = (rank1 – rank2)/( MaxRank – 1)

Binary Attribute(symmetric Attribute):  Gender
  d(i,j) = (r+s)/(q+r+s+t)
We are computing distance by comparing, if the values are equal or not

Numerical Attribute: Age,Price
Normalize age and price attribute using z-score method  and apply cosine similarity between the two vectors 

Zip code feature : Convert zipcode to latitude and longitude and find distance between locations in miles/kilometers.If distance is greater than a threshold, return  distance as 1 otherwise  return 0.

Categorical Attribute :
Category: Applying cosine similarity to category set.
Ethnicity,Organiser Id : Comparing respective values of two user .If they are equal, return 0 otherwise return 1

Interval Attribute: Age group
    Finding distance between Age groups  by calculating different between age range for each program
d(A,B) = (MaxAge(A) – MinAge(B))/(MaxAge(A)—MinAge(A))+(MaxAge(B)—MinAge(B))


