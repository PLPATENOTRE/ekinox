# ekinox


GOAL : Determine if it is relevant to use Machine Learning techniques to identify the key factors that make the success of a student to his exam

### To know before reading code and notebooks :

* I only focused on the _student_por_ dataset : It is more consistend. The analysis can also be run on _student_mat_ to confirm observations and conclusions
* I made the choice to infer target : it seemed to me more relevant to make a classification. That way, I choosed to transform the G3 target: 
    * Passed the exam **(1)** : G3 >=10
    * Failed the exam **(0)** : G3 < 10
--> it is the target we'll use.
* I used information from the _student_mat_ in the modelization to enrich the training set.

**NB:** I prefered notebooks to take this technical test. I hope it's a good choice for reading and interpretation



### There are 2 notebooks :

* **_Ekinox_EDA_** :
    * Statistical descriptions of the dataset
    * Visualization
    
**NB:** I did not conclude anything from this part. It just to plot a few variables and know if we can have an intuition.

* **_Ekinox_Test_**  : 
    * _Pre-processing_
        * NAs management
        * Duplicates management
        * Dummification 
        * Scaling
        
    * _Machine Learning_
        * Test a few models
        * Display and compare results
        
        

**_MODELS_** 

We try **4 modelisations**: random, linear, tree-based, SVM

* **Random**:
    * We can obtain a first baseline model
* **Logistic Regression**
    * We don't optimize paramters.
* **Random Forest**
    * We checked overfitting limits
    * We gridsearch the n_estimators, max_depth and add a cross validation
    * We retain the best estimator
    * We observe the metrics and best features
* **SVM**    
    * We ran a linear SVC 
    * We don't optimize parameters
            

**_METRICS_** 


* Accuracy
* Recall
* LogLoss

**_CONCLUSIONS_**

The takeaways and answer to questions asked        
        

    