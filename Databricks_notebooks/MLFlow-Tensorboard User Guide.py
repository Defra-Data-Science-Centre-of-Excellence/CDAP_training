# Databricks notebook source
# MAGIC %md
# MAGIC # How to Use MLflow, TensorBoard and Hyperopt for distributing hyperparameter tuning
# MAGIC 
# MAGIC This notebook assumes the user has some knowledge of Machine Learning, but you don't have to be an expert!
# MAGIC 
# MAGIC We will use the orchards dataset located in the landing zone to show how to use TensorBoard, MLFlow & Hyperopt.
# MAGIC 
# MAGIC Tensorboard is a visualisation tool for machine learning experiments which allows you to track different metrics such as loss & accuracy. For more details on Tensoboard capabilities go to https://www.tensorflow.org/tensorboard/get_started
# MAGIC 
# MAGIC MLflow is a tool that will help us track our machine learning models, and register them for use at a later date.
# MAGIC 
# MAGIC Hyperopt is a bayesian hyperparameter tuning package.
# MAGIC 
# MAGIC 
# MAGIC It will include the following steps:
# MAGIC 1. Load, explore & preprocess the data
# MAGIC 2. Create a neural network model with Keras
# MAGIC 3. View the training with TensorBoard
# MAGIC 4. Use Hyperopt & MLflow to perform automated hyperparameter tuning
# MAGIC 5. Use Hyperopt & MLflow on a SVC (Support Vectors Classifier) to show distributed hyperparameter tuning
# MAGIC 6. Register the model in MLflow and use the model to make predictions

# COMMAND ----------

# MAGIC %pip install geopandas

# COMMAND ----------

# MAGIC %md
# MAGIC ## Clean and save data into your directory
# MAGIC This step can be skipped, you can load the cleaned data straight from the lab zone

# COMMAND ----------

import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# COMMAND ----------

#Read in traditional orchards dataset
orchards_gdf = gpd.read_file('/dbfs/mnt/landingr/General Access/traditional_orchards/JSON/Traditional_Orchards_HAP_England.json')

# COMMAND ----------

#Drop irrelevant columns
orchards_gdf.drop(columns = ['objectid', 'incid', 'prihabtxt', 'habdefver', 's1captdate', 's1habid', 's1status', 's1planting', 's2captdate', 's2habid', 's2status', 's2planting', 'api_date', 's3boundary', 's3metadata', 'top_data', 's4date', 's4status', 's4planting', 's4metadata', 'mastermap', 's5captdate', 'stewardshi', 'iacs', 'created_on', 'last_edit', 'nontocode', 'notes', 'trees', 'interest', 'easting', 'northing', 'geometry'], inplace = True)

# COMMAND ----------

#Replaces blank values with a zero, perform necerssary data cleaning

orchards_gdf = orchards_gdf.replace(r'^\s*$','0', regex=True)

orchards_gdf = orchards_gdf.replace(['Y','y', 'S', 's', '6', '2', 'O', 'F', 'R', 'A', 'D', 'Y', 'C'], '1')
orchards_gdf = orchards_gdf.replace(['?', 'N'], '0')

orchards_gdf['pridet'] = orchards_gdf['pridet'].replace(['Definately is TO priority habitat', 'Definitely is Traditional Orchard priority habitat'], 'TO priority habitat')
orchards_gdf['pridet'] = orchards_gdf['pridet'].replace(['Traditional orchard habitat may be present', 'Probably Traditional Orchard priority habitat but some uncertainty due to age of data source', 'Priority Traditional Orchard habitat may be present but evidence is either insufficient to determine presence confidently or is in the oldest allowable category', '-'], 'Possible priority habitat')

orchards_gdf['interqual'] = orchards_gdf['interqual'].replace(['Medium (3)', '3', '3 (Medium)'], 3)
orchards_gdf['interqual'] = orchards_gdf['interqual'].replace(['4 (Medium)'], 4)
orchards_gdf['interqual'] = orchards_gdf['interqual'].replace(['2', '2 (Medium)'], 2)
orchards_gdf['interqual'] = orchards_gdf['interqual'].replace(['1', '1 (high)', 'High (1)', '1 (High)'], 1)

orchards_gdf['truthed'] = orchards_gdf['truthed'].replace(['Not done'], 'Not Done')

orchards_gdf['quest'] = orchards_gdf['quest'].replace(['Not done', '0'], 'Not Done')

orchards_gdf['s3habid'] = orchards_gdf['s3habid'].replace(['0'], 'Other')

orchards_gdf['s3status'] = orchards_gdf['s3status'].replace(['0'], 'Management unknown')
orchards_gdf['s3status'] = orchards_gdf['s3status'].replace(['Part managed', 'PArt-managed'], 'Part-managed')
orchards_gdf['s3status'] = orchards_gdf['s3status'].replace(['Active management'], 'Actively managed')

orchards_gdf['s3planting'] = orchards_gdf['s3planting'].replace(['0'], 'No young trees')
orchards_gdf['s3planting'] = orchards_gdf['s3planting'].replace(['Established, few or no ga'], 'Established, few or no gaps')
orchards_gdf['s3planting'] = orchards_gdf['s3planting'].replace(['Active management', 'Management unknown'], 'No young trees')
orchards_gdf['s3planting'] = orchards_gdf['s3planting'].replace(['Young trees', 'Youngtrees in gaps'], 'Young trees in gaps')

orchards_gdf['s4boundary'] = orchards_gdf['s4boundary'].replace(['Tertiart', 'SecondaryS'], ['Tertiary', 'Secondary'])

orchards_gdf['s4habid'] = orchards_gdf['s4habid'].replace(['Other'], '0')

orchards_gdf['s5boundary'] = orchards_gdf['s5boundary'].replace(['0', 'Boundary u', '18/09/2004'], 'Secondary')

orchards_gdf['habconditi'] = orchards_gdf['habconditi'].replace(['n/a'], '0')

orchards_gdf['up_to_100'] = orchards_gdf['up_to_100'].replace(['3'], '0')

orchards_gdf = orchards_gdf.replace('1', 1)
orchards_gdf = orchards_gdf.replace('0', 0)

# COMMAND ----------

orchards_gdf['interqual'] = orchards_gdf['interqual'].astype('int32')

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Exploration
# MAGIC Perform some basic data exploration to check that variables are in the correct format & no more cleaning is needed.

# COMMAND ----------

plt.figure(figsize = (30,35))
for i, j in enumerate(orchards_gdf.columns[:52]):
  plt.subplot(6,11,i+1)
  orchards_gdf[j].value_counts().plot(kind = 'bar', title = j)
  plt.xticks(rotation =45)
plt.show()

# COMMAND ----------

orchards_gdf.dtypes

# COMMAND ----------

orchards_gdf.to_csv("/dbfs/mnt/labr/andrew.simpson@defra.gov.uk/clean_orchards.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Save the dataframe to your lab area to easily load clean data in the future 
# MAGIC 
# MAGIC If you currently haven't got your own area in the lab zone, follow this notebook for more details: https://adb-7480336463633201.1.azuredatabricks.net/?o=7480336463633201#notebook/2951151218561779/command/2951151218561780

# COMMAND ----------

orchards_gdf.to_csv("/dbfs/mnt/labr/FirstName.LastName@defra.gov.uk/clean_orchards.csv")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Load cleaned Dataset 
# MAGIC 
# MAGIC Now load your cleaned dataset or if you skipped that step load the pre cleaned dataset

# COMMAND ----------

orchards = pd.read_csv("/dbfs/mnt/labr/andrew.simpson@defra.gov.uk/clean_orchards.csv", index_col = 0)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Convert to machine readable format
# MAGIC 
# MAGIC - Convert values into binary and one hot encode the categorical variables. This is a way of making a categorical variable machine readable. For more info follow: https://datagy.io/sklearn-one-hot-encode/#:~:text=One-hot%20encoding%20is%20the%20process%20by%20which%20categorical,receives%20a%201.%20Otherwise%2C%20it%20receives%20a%200.
# MAGIC - Isolate the numerical variables
# MAGIC - Join the one hot encoded and numerical dataframes

# COMMAND ----------

one_hot_encode = pd.get_dummies(orchards.select_dtypes('object')).drop(columns = ['pridet_TO priority habitat', 'habconditi_0', 'truthed_Not Done', 'quest_Not Done', 's3habid_Other', 's4boundary_0', 's4habid_0']).astype('int64')
orchards_num = orchards.select_dtypes(exclude = 'object')
orchards_final = pd.concat([one_hot_encode, orchards_num], axis = 1, join = 'inner')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Import relevant libraries
# MAGIC - We'll use sklearn to pre-process data and scale features
# MAGIC - We'll use Keras to create a model and we'll view the training of this in TensorBoard

# COMMAND ----------

from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models, Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# COMMAND ----------

# MAGIC %md
# MAGIC #### Preprocess
# MAGIC - Isolate our target values "apples"
# MAGIC - Split the variables into train & test sets
# MAGIC - Normalise the data

# COMMAND ----------

target = orchards_final['apple']
variables = orchards_final.drop(columns = ['apple'])

X_train, X_test, Y_train, Y_test = train_test_split(variables, target, test_size = 0.2)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Create a Basic Neural Network and then compile it
# MAGIC We'll define a function that will create a basic Neural Network of 2 layers, making sure to set input_shape to the number of variables in the dataset. Also make sure the activation function in the final layer is 'sigmoid' as this is a binary classification problem.

# COMMAND ----------

def create_model(first_layer, second_layer):
  model = Sequential()
  model.add(Dense(first_layer, input_shape = (X_train.shape[1],),   activation = 'relu'))
  model.add(Dense(second_layer, activation = 'relu'))
  model.add(Dense(1, activation = 'sigmoid'))
  return model

# COMMAND ----------

model = create_model(70, 70)
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics=['accuracy'])
model.summary()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Fit our model
# MAGIC - First set a directory for the experiment log and a path for the model checpoints
# MAGIC - Set up the TensorBoard and early stopping callbacks, we use eary stopping callbacks to prevent the model overfitting to the training data.
# MAGIC - Set a modelcheckpoint so only the best model is according to our loss function
# MAGIC - Finally fit the model

# COMMAND ----------

experiment_log_dir = "/dbfs/mnt/labr/andrew.simpson@defra.gov.uk/mlflow"

tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=experiment_log_dir)
monitor_val_acc = EarlyStopping(monitor = 'val_accuracy', patience = 4)

history = model.fit(X_train, Y_train, validation_split=0.2, epochs=30, callbacks=[tensorboard_callback, model_checkpoint, monitor_val_acc])

# COMMAND ----------

#experiment_log_dir = "/dbfs/mnt/labr/<YourUsername>"
#checkpoint_path = "/dbfs/mnt/labr/<YourUsername>/keras_checkpoint_weights.ckpt"

#tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=experiment_log_dir)
#model_checkpoint = ModelCheckpoint(filepath=checkpoint_path, verbose=1, save_best_only=True)
#monitor_val_acc = EarlyStopping(monitor = 'val_accuracy', patience = 4)

#history = model.fit(X_train, Y_train, validation_split=0.2, epochs=30, callbacks=[tensorboard_callback, model_checkpoint, monitor_val_acc])

# COMMAND ----------

# MAGIC %md
# MAGIC ### Use the following commands to start TensorBoard, it will continue to run until the notebook is detached from the cluster
# MAGIC Here in the Tensorboard you can view how the model's train and test set's loss progresses with each epoch. An epoch is the amount of times the training data has beed fed through a neural network to update the weights of each neuron.

# COMMAND ----------

# MAGIC %load_ext tensorboard
# MAGIC %tensorboard --logdir $experiment_log_dir

# COMMAND ----------

# MAGIC %md
# MAGIC ### Check the final train and test accuracy of our model

# COMMAND ----------

train_accuracy = model.evaluate(X_train, Y_train, verbose = 0)[1]
test_accuracy = model.evaluate(X_test, Y_test, verbose = 0)[1]
print("Train set accuracy: "+str(train_accuracy)+" %")
print("Test set accuracy: "+str(test_accuracy)+" %")

# COMMAND ----------

# MAGIC %md
# MAGIC #### Check the accuracy of each class with a confusion matrix
# MAGIC Because there is a large class imbalance with the target values (There are lots more orchards without apples than with) we need to check the accuracy of each class.

# COMMAND ----------

predictions = np.round(model.predict(X_test))
class_names = np.array(['No Apples', 'Apples'])

cm =   confusion_matrix(np.array(Y_test), predictions)
cm_n = confusion_matrix(np.array(Y_test), predictions, normalize = 'true')

disp = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = class_names)
disp_n = ConfusionMatrixDisplay(confusion_matrix = cm_n, display_labels = class_names)
disp.plot(cmap = plt.cm.Blues, values_format = 'd')
disp_n.plot(cmap = plt.cm.Blues)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Class Imbalance
# MAGIC You can see from the confusion matrix that the model predicts orchards without apples at a higher accuracy than orchards with Apples. This is becuase the training set was imbalanced with many more orchards that didn't have apples. There are techniques to combat the issue of an imbalanced dataset, but this is outside the scope of this notebook. 
# MAGIC 
# MAGIC You can find some interesting solutions to this problem here: https://towardsdatascience.com/smote-fdce2f605729

# COMMAND ----------

# MAGIC %md
# MAGIC # MLflow
# MAGIC Here we will use Mlflow to log our model, the model parameters, evaluation metrics as other artifacts (such as our confusion matrix)

# COMMAND ----------

import mlflow
import mlflow.keras
import mlflow.tensorflow
import mlflow.sklearn

# COMMAND ----------

with mlflow.start_run():
  num_hidden_layers = 2
  hidden_layer_1 = 100
  hidden_layer_2 = 100
  activation_function = 'relu'

  model2 = create_model(hidden_layer_1, hidden_layer_2)
  model2.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics=['accuracy'])
  model2.fit(X_train, Y_train, epochs = 30, callbacks = [monitor_val_acc], validation_split = 0.2)

  mlflow.log_param('No of hidden layers', num_hidden_layers)
  mlflow.log_param('size of first hidden layer', hidden_layer_1)
  mlflow.log_param('size of second hidden layer', hidden_layer_2)
  mlflow.log_param('Activation Function', activation_function)

  accuracy = model2.evaluate(X_test, Y_test)[1]
  mlflow.log_metric("Accuracy", accuracy)

  mlflow.keras.log_model(model2, "ANN-Model")
  
  predictions = np.round(model2.predict(X_test))
  class_names = np.array(['No Apples', 'Apples'])
  cm =   confusion_matrix(np.array(Y_test), predictions)
  cm_n = confusion_matrix(np.array(Y_test), predictions, normalize = 'true')

  disp = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = class_names)
  disp_n = ConfusionMatrixDisplay(confusion_matrix = cm_n, display_labels = class_names)

  conf_mat = disp.plot(cmap = plt.cm.Blues, values_format = 'd')
  plt.savefig("confusion_matrix.png")
  mlflow.log_artifact("confusion_matrix.png")

  conf_mat_n = disp_n.plot(cmap = plt.cm.Blues)
  plt.savefig("confusion_matrix_normalized.png")
  mlflow.log_artifact("confusion_matrix_normalized.png")

  mlflow.end_run()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Experiment Tab
# MAGIC You can now click the experiment tab in the top right corner to the our saved model (It looks like a half filled beaker). If you click on 'view run detail' (the square box with an arrow) a seperate tab will open where you will be able to view all the information that was logged in the run, such as parameters, metrics & artifacts.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Perform hyperparameter tuning with Hyperopt
# MAGIC Hyperopt is a package designed to optimize machine learning algorithms. Whereas random & grid searches are two very popular methods, they can be very inefficient and take long amount of time. Hyperopt uses a bayesian approach which can be more efficient and more accurate.
# MAGIC 
# MAGIC To perform tuning with hyperopt we need to:
# MAGIC 1. Define an objective function, this returns a loss function that is to be minimised.
# MAGIC 2. Define a space to search over
# MAGIC 3. Describe the search algorithm that will be used
# MAGIC 
# MAGIC I'll describe these as we go along

# COMMAND ----------

from hyperopt import fmin, hp, tpe, STATUS_OK, SparkTrials
import hyperopt

# COMMAND ----------

#Define a function for creating a model, but this time it takes a dictionary as an input which contains our search space

def create_model2(n):
  model = Sequential()
  model.add(Dense(int(n["dense_l1"]), input_shape=(X_train.shape[1],), activation="relu"))
  model.add(Dense(int(n["dense_l2"]), activation="relu"))
  model.add(Dense(1, activation="sigmoid"))
  return model

# COMMAND ----------

# MAGIC %md
# MAGIC ## Objective Function
# MAGIC Now we have to define a function that is to be minimised, here we are going to use the binary crossentropy loss function that we used on our models before.

# COMMAND ----------

def runNN(n):
  # Log run information with mlflow.tensorflow.autolog()
  mlflow.tensorflow.autolog()
  
  model = create_model2(n)
 
  # Compile model
  model.compile(loss="binary_crossentropy",
                optimizer='adam',
                metrics=["accuracy"])
 
  history = model.fit(X_train, Y_train, validation_split=0.2, epochs=30, callbacks = [monitor_val_acc], verbose=2)
 
  # Evaluate the model
  score = model.evaluate(X_test, Y_test, verbose=0)
  obj_metric = score[0]  
  return {"loss": obj_metric, "status": STATUS_OK}

# COMMAND ----------

# MAGIC %md
# MAGIC ## Search Space
# MAGIC Here we define a search space for our hyperparameters, here we need to find the optimal amount of nodes for the first and second layer of our neural network. we use the hp.quiniform function which will return values as integers uniformly between an upper and lower bound. here the lower & upper bounds are 50 & 120 respectively. For a list of other functions that return different types of values , such as floats or values that are normally distributed see: http://hyperopt.github.io/hyperopt/getting-started/search_spaces/?msclkid=92f4ecc7a9ea11eca79bace9a118f92d

# COMMAND ----------

space = {
  "dense_l1": hp.quniform("dense_l1", 50, 120, 1),
  "dense_l2": hp.quniform("dense_l2", 50, 120, 1)
 }

# COMMAND ----------

# MAGIC %md
# MAGIC ## FMin() Function
# MAGIC FMin() minimises our loss function and saves the best parameters, it takes as inputs our objective function & search space which we have already described.
# MAGIC We now need to select a search algorithm where the two main choices are:
# MAGIC - hyperopt.tpe.suggest: Tree of Parzen Estimators, a Bayesian approach which iteratively and adaptively selects new hyperparameter settings to explore based on past results
# MAGIC - hyperopt.rand.suggest: Random search, a non-adaptive approach that samples over the search space
# MAGIC we'll choose the tpe search algorithm and also set max evaluations to 20. This can be increased for a more exhaustive approcach, but will take more time and use more resources.

# COMMAND ----------

with mlflow.start_run():
  best_hyperparam = fmin(fn=runNN,
                         space=space, 
                         algo=tpe.suggest, 
                         max_evals=20)
  mlflow.end_run()

# COMMAND ----------

# View the best parameters
print(hyperopt.space_eval(space, best_hyperparam))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Now build the final model using the best set of hyperparameters

# COMMAND ----------

first_layer = hyperopt.space_eval(space, best_hyperparam)["dense_l1"]
second_layer = hyperopt.space_eval(space, best_hyperparam)["dense_l2"]

# COMMAND ----------

final_model = create_model(first_layer, second_layer)
final_model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics=['accuracy'])
final_model.summary()

# COMMAND ----------

with mlflow.start_run():
  num_hidden_layers = 2
  activation_function = 'relu'
  
  final_model.fit(X_train, Y_train, epochs = 30, callbacks = [monitor_val_acc], validation_split = 0.2)

  mlflow.log_param('No of hidden layers', num_hidden_layers)
  mlflow.log_param('size of first hidden layer', first_layer)
  mlflow.log_param('size of second hidden layer', second_layer)
  mlflow.log_param('Activation Function', activation_function)
  
  mlflow.keras.log_model(model2, "ANN-Model-Optimized")
  
  predictions = np.round(final_model.predict(X_test))
  cm =   confusion_matrix(np.array(Y_test), predictions)
  cm_n = confusion_matrix(np.array(Y_test), predictions, normalize = 'true')

  disp = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = class_names)
  disp_n = ConfusionMatrixDisplay(confusion_matrix = cm_n, display_labels = class_names)

  conf_mat = disp.plot(cmap = plt.cm.Blues, values_format = 'd')
  plt.savefig("confusion_matrix.png")
  mlflow.log_artifact("confusion_matrix.png")

  conf_mat_n = disp_n.plot(cmap = plt.cm.Blues)
  plt.savefig("confusion_matrix_normalized.png")
  mlflow.log_artifact("confusion_matrix_normalized.png")

  mlflow.end_run()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Distributed Hyperparameter tuning with Hyperopt
# MAGIC You can utilise spark for distributed hyperparamter tuning, this can only be done when using a single-node library. Unfortunately it also dosn't work too well with Keras as Hyperopt uses Pickle to serialise objects and there are compatability issues with using Pickle to serialise Keras objects (models), there are ways of getting round this problem, but that's outside the scope of this notebook. Therefore we will now use a Support Vector Machines (SVM) Classifier to demonstrate distributed hyperparameter tuning and how it speeds things up.

# COMMAND ----------

from sklearn.svm import SVC

# COMMAND ----------

# MAGIC %md
# MAGIC ### The objective function here is much simpler, we're just defining a basic Support Vector Classifier from sklearn and using accuracy as the loss. We have to use the negative of accuracy as we are trying to minimise this function
# MAGIC Also it is best to avoid using cross validation in the objective function, even though this will normally return a more accurate estimate of the loss. This is because if k-folds are used, then k models are fit instead of 1, meaning that the task will run at roughly k times longer.

# COMMAND ----------

def objective(C):
  clf = SVC(C)
  clf.fit(X_train, Y_train)
  accuracy = clf.score(X_test, Y_test)
  
  return {"loss": -accuracy, "status": STATUS_OK}
  

# COMMAND ----------

search_space = hp.lognormal("C", 0, 1)

# COMMAND ----------

best_SVM_hyperparam = fmin(fn=objective, 
                         space=search_space, 
                         algo=tpe.suggest, 
                         max_evals=5)


# COMMAND ----------

best_SVM_hyperparam

# COMMAND ----------

# MAGIC %md
# MAGIC ## Parralised hyperparameter tuning
# MAGIC Notice how this task took 10 minutes, given that only one parameter is being searched over 5 evaluations this is a long time. To speed things up we can use SparkTrials() which distributes the tuning job across a Spark cluster. The parallelism argument sets the maximum number of trials to evaluate concurently.
# MAGIC 
# MAGIC Be careful though as Hyperopt proposes new trials from past results, basically Hyperopt can be more adaptive if has access to more past results. This means that a higher parallelism will speed up the task, but lower parallelism may lead to better results
# MAGIC 
# MAGIC Hyperopt can be more adaptive if has access to more past results

# COMMAND ----------

spark_trials = SparkTrials()

with mlflow.start_run():
  best_SVM_hyperparam2 = fmin(fn=objective, 
                         space=search_space, 
                         algo=tpe.suggest, 
                         max_evals=5,
                         trials=spark_trials)
  mlflow.end_run()

# COMMAND ----------

# MAGIC %md 
# MAGIC #### By using Spark we see that the task now has only taken 1.6 minutes, showing how much quicker it is to hyperparameter search with spark

# COMMAND ----------

best_SVM_hyperparam2

# COMMAND ----------

# MAGIC %md
# MAGIC ## Registering Models
# MAGIC Once a model has been logged with MLflow, it can be registered so it can be loaded in the future to make predictions. We're going to do this with the ANN model we created earlier. To do this open the experiments tab and click on the 'View Experiment UI' button in the top right corner, it is a square with an arrow going through it.
# MAGIC 
# MAGIC From there click on the model that you would like to register and click on register model.

# COMMAND ----------

# MAGIC %md
# MAGIC ![import](/files/tables/model_register.jpg)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Loading your model
# MAGIC To load your registered model use the function mlflow.'pyfunc'.load_model(), so for example if keras yo uwould use mlflow.keras.load_model() whereas sklearn would use mlflow.sklearn.load_model(). You need the model name and also the model version.

# COMMAND ----------

model_name = "ANN-Model-Optimized"
model_version = 1

keras_model = mlflow.keras.load_model(f"models:/{model_name}/{model_version}")

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Now the model is loaded you can make predictions with it.

# COMMAND ----------

keras_model.evaluate(X_test, Y_test, verbose = 0)

# COMMAND ----------

np.round(keras_model.predict(X_test))

# COMMAND ----------

predictions = np.round(keras_model.predict(X_test))
cm =   confusion_matrix(np.array(Y_test), predictions)
cm_n = confusion_matrix(np.array(Y_test), predictions, normalize = 'true')

disp = ConfusionMatrixDisplay(confusion_matrix = cm, display_labels = class_names)
disp_n = ConfusionMatrixDisplay(confusion_matrix = cm_n, display_labels = class_names)
disp.plot(cmap = plt.cm.Blues, values_format = 'd')
disp_n.plot(cmap = plt.cm.Blues)
plt.show()

# COMMAND ----------

df = spark.read.csv('/mnt/labr/andrew.simpson@defra.gov.uk/clean_orchards.csv', header = True, index_col = 0)

# COMMAND ----------

df = df.drop('_c0')

# COMMAND ----------

display(df.select('apple'))

# COMMAND ----------

target_new = df.select('apple')
variables_new = df.drop('apple')

X_train2, X_test2, Y_train2, Y_test2 = train_test_split(variables, target, test_size = 0.2)

# COMMAND ----------

model_new = create_model(50,50)

# COMMAND ----------

model_new.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics=['accuracy'])
model_new.summary()

# COMMAND ----------

X_train2

# COMMAND ----------


