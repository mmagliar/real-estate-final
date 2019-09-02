# Evaluating Real Estate
By: David Kling, Michael Magliaro, and Benjamin Eck

Trying to predict real estate prices is a difficult task. There are potentially thousands of variables that one could look at to determine what they should list their house for. Several real estate listing websites now offer free estimates for what your house is worth using machine learning models. Each of these sites use a proprietary blend of models and variables to determine what they think your house is worth. For example, at the time that this is being written one of the collaborators' properties is valued at the following prices by 4 major listing sites:

- Zillow: $244,961
- Realtor: $213,300
- Redfin: $238,000 - $263,000
- Trulia: $243,255


### Our Original Idea: Are population fluxuations correlated to real estate prices? If so, can we use this data in conjunction with basic property metrics to estimate sale prices for active listings?
After creating several models to predict real estate prices the best model we could create had a score of 0.4722. We decided to dive deeper into the data and see what else we could predict using it.

### Our Refined Idea: Can we use machine learning to classify properties into county and/or cities/towns based on several property attributes?
We decided to take some data from Garden State MLS and try our hands at predicting listing prices. The results of our efforts were four machine learning models using Random Forest Classifiers.

- The first predicts whether a given set of property attributes would be in Sussex or Union county. This model has a score of 0.9608 indicating that it can predict the county with strong confidence.
- The second uses all of the data we collected to predict what city or town the property would reside in. With a score of 0.6157, we cannot trust the results of this model nearly as much.
- The third model uses only the data from Sussex County to determine the city or town. While limiting the possible cities or towns that the model has to choose between we hypothesized that this model would be inherently more accurate, but that was not the case. With a score of 0.6028 this model had the lowest confidence of these four models.
- The last model uses only the data from Union County to determine the city or town. After seeing the results of the third model we thought that this model would have a slightly higher score than the second model because this model would average with the third to roughly equal the second. We were surprised again when this model returned a score of 0.7255. This potentially indicates that there property attributes are more strongly correlated in Union County than Sussex County.

#### Our Data Characteristics:
- Number of attributes: 21 features total. The county prediction model takes in all 16 attributes provided by the user. The other three utilize all but the 'exterior features' attribute.
- Number of records: 2,145

#### Usage:
- Clone the repository
- Use 'pip install -r requirements.txt' on a new virtual environment to install necessary dependencies.
- In the command line use 'python app.py' to spin up the flask app.
- In your browser type '127.0.0.1:8000' to go to the home page.