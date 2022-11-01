# CDAP training
Here you can find training materials for using the Common Data Analytics Platform (CDAP). These materials were created by members of the Data Analytics and Science Hub (DASH) in core Defra. Feedback is welcome! Please raise any issues in the [Issues](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training/issues) tab.

To get an overview of the CDAP platform, head to the [DASH SharePoint site](https://defra.sharepoint.com/sites/Community448/SitePages/CDAP-The-Common-Data-Analytics-Platform.aspx).  

These pages contain information and further links about the following topics:
- CDAP playbook (under development - link to follow)
- [Introduction to CDAP](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training#introduction-to-cdap) - get an overview of the platform
- [Importing your own data to CDAP](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/Upload_data/)
- [Working with Databricks](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training#databricks-notebooks) - used for analysis in Python, SQL, and R
- [R and RStudio on CDAP](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training#r-and-rstudio-on-cdap) - find out how to work in R and RStudio on CDAP   
- [Further training resources](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/further_training)     


## CDAP playbook *link to follow*  

The CDAP playbook gives a detailed account of how CDAP will operate over the next few years, detailing all the features as well as governance around the platform.  


## Getting started with CDAP

- [Introduction to CDAP](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/introduction_to_cdap/)
    - Lean about clusters and data on CDAP
    - Accessing Databricks and RStudio workspaces  

- [Video on accessing CDAP and combining data](https://defra.sharepoint.com/sites/Community448/Comms/Forms/AllItems.aspx?id=%2Fsites%2FCommunity448%2FComms%2FRecordings%2FCDAP%5Fdemo%5FPart1%5Faccess%2Emp4&parent=%2Fsites%2FCommunity448%2FComms%2FRecordings&nav=%7B%22playbackOptions%22%3A%7B%22startTimeInSeconds%22%3A1%2E938248%7D%7D)
    - This video talks through accessing Databricks notebooks  
    - Accessing RStudio in CDAP  
    - Databricks Filestore  

- [Importing your own data to CDAP](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/Upload_data/)
    - Learn to load data into CDAP  
    - Moving data to your folder in the lab zone


## Databricks notebooks

Databricks notebooks can be used for writing Python, SQL, and R code, as well as a combination of the languages all within the same notebook.  

- [Example workflow in Databricks](https://defra.sharepoint.com/sites/Community448/Comms/Forms/AllItems.aspx?id=%2Fsites%2FCommunity448%2FComms%2FRecordings%2FCDAP%5Fdemo%5FPart2%5Fapples%5FTrim%2Emp4&parent=%2Fsites%2FCommunity448%2FComms%2FRecordings&nav=%7B%22playbackOptions%22%3A%7B%22startTimeInSeconds%22%3A0%2E95829%7D%7D): This video gives you an idea of what is possible
    - This example uses geospatial data from CDAP  
    - See how to create a dashboard using Python  

- [Databricks documentation](https://docs.microsoft.com/en-gb/azure/databricks/) offers lots of information easily accessible in one place, for a variety of tasks.
  - The documentation is based on a general set-up of Databricks, not all of which can be done on CDAP; for example, you can use existing clusters, but not create your own.

### [CDAP training notebooks in Databricks](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/Databricks_git/)

We have created training notebooks that you can load from this GitHub page into your CDAP workspace for practising. Click the heading to access a guide on accessing this repo from Databricks, so you can load the notebooks into CDAP and run the code.  

The following notebooks are available:  
- CDAP Demo - Data Combine (this is the notebook used in the videos linked above)   
- Data access user guide  
- ML flow and tensorboard user guide  

### Databricks Training

Databricks offer lots of training materials that are free to DEFRA employees to help utilise the Databricks workspace. Most of these courses are Python & SQL based will require some prior knwoledge so I recommend looking at the beginners courses that are highlighted further on.  

To access Databricks Learning, you can sign up [here](https://customer-academy.databricks.com/learn)
When using these notebooks provided by Databricks, it is important that you attach the notebook to the training cluster. The other clusters do not support the set up of the notebooks.

<!-- ![Training cluster](Databricks_git/images/Screenshot (96)_LI.jpg) -->
![Training cluster](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training/blob/main/Databricks_git/images/Screenshot%20(96)_LI.jpg)


#### Python on Databricks 
Databricks offer lots of training materials that are free to DEFRA employees to help utilise the Databricks workspace. Most of these courses will require some prior knowledge of Python so I recommend looking at the beginners Python training first, see bottom of this page.

- [Apache Spark<sup>TM</sup> Programming with Databricks](https://customer-academy.databricks.com/learn/course/internal/view/elearning/63/apache-spark-programming-with-databricks): Because Databricks is built upon spark clusters this is a good course to start with in order ot make use of the Databricks workspace.
Spark can optimize queries, especially for big data.

  - Identify core features of Spark & Databricks
  - Apply the DataFrame transformation API to process and analyse data
  - Apply Delta & Structured streaming to process streaming data

- [Scalable Machine Learning with Apache Spark](https://customer-academy.databricks.com/learn/course/internal/view/elearning/128/scalable-machine-learning-with-apache-spark): This course navigates the process of building machine learning solutions using Spark. You will build and tune ML models with SparkML using transformers, estimators, and pipelines. This course highlights some of the key differences between SparkML and single-node libraries such as scikit-learn. You will also reproduce your experiments and version your models using MLflow.

  - Create data processing pipelines with Spark.
  - Build and tune machine learning models with Spark ML.
  - Track, version, and deploy models with MLflow.
  - Perform distributed hyperparameter tuning with Hyperopt.
  - Use Spark to scale the inference of single-node models.

#### SQL on Databricks

-[Data Analysis with Databricks SQL](https://customer-academy.databricks.com/learn/course/internal/view/elearning/1035/data-analysis-with-databricks-sql): This course provides a comprehensive introduction to Databricks SQL. Learners will ingest data, write queries, produce visualizations and dashboards, and configure alerts. 
  - Import data and persist it in Databricks SQL as tables and views
  - Query data in Databricks SQL 
  - Use Databricks SQL to create visualizations and dashboards
  - Create alerts to notify stakeholders of specific events
  - Share queries and dashboards with others


## R and RStudio on CDAP  

We have created training materials for working in RStudio in CDAP.  

- [Getting started with RStudio in CDAP](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/RStudio_in_CDAP/getting_started/): This is a guide for using RStudio within CDAP, for those familiar with R and RStudio, but new to CDAP. It contains:  
    - Opening and closing RStudio 
    - RStudio workspace  
    - Accessing and working with CDAP data from RStudio   
    - Uploading files into your workspace in RStudio  
    - This also includes instructions on how you can install packages and upload data, which you need to be able to do the [Introduction to R course](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training#training-materials-for-beginners)

- [Connecting RStudio to git and GitHub](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/RStudio_in_CDAP/git_and_github/): This course is a short version of getting connected as described in Jenny Bryan’s book, Happy Git with R, adapted to work for CDAP. See the book here: [Let’s Git started. Happy Git and GitHub for the useR](https://happygitwithr.com). It contains:  
    - Connecting everything using GitHub's Personal Access Tokens  
    - Adding your GitHub repo to RStudio
    - Working with GitHub and your RStudio project  
    - For more about how to use GitHub, you can sign up for a Government Analysis Function course: [Intro to Git](https://analysisfunction.civilservice.gov.uk/training/introduction-to-git/).

- [Dashboards with Shiny and RStudio Connect](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/Create_dashboards/): This is a guide for creating a dashboard through Shiny in RStudio and publishing it with RStudio Connect. It contains:
    - Creating dashboards  
    - Publishing dashboards  
    - For more detailed information on building Shiny apps, see the [Shiny RStudio pages](https://shiny.rstudio.com/).  
    - For more information on RStudio Connect, see the [RStudio Connect pages](https://www.rstudio.com/products/connect/).


## [Further training resources](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/further_training)

This page details more courses that are available to you. these courses are not specific to CDAP, but are useful for those new to programming in R, Python, or SQL, and also link to more advanced courses to make the most of the capabilities of CDAP, such as Spark:  

- Training for beginners  
    - R and RStudio training  
    - Python training  
    - SQL training  
- More advanced training  
    - Government Analysis Function courses  
    - Geospatial courses  
- Resources for good practice  
- Table of links  
