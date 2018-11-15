# Fraud Detection Case Study

<img src='images/crisp_dm.png'/>

## Business Understanding:
We are a vendor for event tickets and many events posted to our site are fraudulant. We suspect that there is a way to predict whether or not an event is fraudulent based on the metadata we collect about the event and the organizers. If we can automatically flag likely fraudulant events and cascade these events to a human

## Data Understanding
The nature of fraud is that the ratio between fraudulant events and non-fraudulent events is imbalanced. Reviewing our training data in `data/data.zip`, the ratio is 1:9. This does not cause issues if this is kept in mind while evaluating the model, but condsideration needs to be made for how to `train/test split` our data to ensure that the ratio of successes to failures is maintained in the training set and the testing set. To solve this problem, we used the scikit learn class: `sklearn.model_selection.StratifiedShuffleSplit`.

## Data Preparation
While text data is present in the data provided, we chose to avoid natural language processing. We extracted `continuous and categorical variables, and feature engineered features` from the avaialable data.

## Modelling

```python
def fraud_pipeline():
    """instantiate a pipeline object"""
    pipeline = Pipeline([
        ('featurizer', Featurizer()),
        ('imputer', Imputer()),
        ('dummifier', Dummifier()),
        ('standardizer', Standardizer()),
        ('model', RandomForestClassifier(n_estimators=5000, 
                                         max_depth=25))
        ])
    return pipeline
```

#### TRAIN AND PICKLE A MODEL:

Use the following code snippet to create a pickled pipeline.
```python
from src import model, stream
"""get training data (may require 
unzipping data.zip file)"""

X, y = model.load('../data/data.json')
pipe = model.fraud_pipeline()
pipe.fit(X, y)

"""get streaming data to predict on"""
streamed_data = stream.get_stream_df(100)
pipe.predict_proba(streamed_data)

"""pickle the pipeline"""
model.pickle_pipeline(pipe, 'pickled_pipeline.pkl')
```


## Evaluation
During training, we evaluated our model using log-loss. With a `log-loss score of 0.0614`, we are confident that we can flag likely fraud effectively.

#### Feature Importance:

- 'country_US',
- 'payout_type_CHECK',
'has_payee_name_0',
'has_logo_0',
'has_twitter_0',
'channels_0',
'user_type_3',
'delivery_method_1.0',
'delivery_method_0.0',
'has_facebook_0',
'event_duration',
'user_type_1',
'max_cost',
'name_length',
'body_length',
'has_payout_type_0',
'payout_type_',
'user_age',
'sale_duration',
'has_previous_payouts_0']
Because we are deploying our model on a dashboard, evaluating an optimal threshold at which to flag an event as likely fraudulent became important. A threshold that is too low is likely to overwhelm a human analyst and be resource intensive. A threshold too high and it is likely that fraudelent events will go unnoticed. 

Using a cost-benefit a matrix, we found the following results:
<img src='images/cost_benefit2.png'/>


## Deployment
<img src='images/web_app.png'/>

#### Deliverables

We will want two deliverables from you for this project:

* A dashboard for investigators to use which helps them identify new events that are worthy of investigation for fraud.  This will pull in new data regularly, and update a useful display for the investigation team.  How you wish to lay this out is up to you.
* A ten-minute presentation on your process and results. 





