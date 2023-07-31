![dashbanner](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training/blob/main/images/DASH.png)

# DASH Platform training
Here you can find training materials for using the DASH Platform. These materials were created by members of the Data Analytics and Science Hub (DASH) in core Defra. Feedback is welcome! Please raise any issues in the [Issues](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training/issues) tab.
  
The training is structured around the technologies available on the platform.
Each folder has a description of the technology as well as how to access it.
Sub-folders are designed to be modular and task based to be both an induction as well as reference guide.

## DASH team Sharepoint

[DASH SharePoint site](https://defra.sharepoint.com/sites/Community448/SitePages/Welcome-to-the-Data-Science-Centre-of-Excellence.aspx)

For an overview of the DASH platform visit the [DASH Platform SharePoint site](https://defra.sharepoint.com/sites/Community448/SitePages/CDAP-The-Common-Data-Analytics-Platform.aspx). Where you can watch a [Video on accessing the DASH Platform and combining data](https://defra.sharepoint.com/sites/Community448/Comms/Forms/AllItems.aspx?id=%2Fsites%2FCommunity448%2FComms%2FRecordings%2FCDAP%5Fdemo%5FPart1%5Faccess%2Emp4&parent=%2Fsites%2FCommunity448%2FComms%2FRecordings&nav=%7B%22playbackOptions%22%3A%7B%22startTimeInSeconds%22%3A1%2E938248%7D%7D)
  
[DASH Platform SharePoint site](https://defra.sharepoint.com/sites/Community448/SitePages/CDAP-The-Common-Data-Analytics-Platform.aspx). Where you can watch a [video]- [Video on accessing the DASH Platform and combining data](https://defra.sharepoint.com/sites/Community448/Comms/Forms/AllItems.aspx?id=%2Fsites%2FCommunity448%2FComms%2FRecordings%2FCDAP%5Fdemo%5FPart1%5Faccess%2Emp4&parent=%2Fsites%2FCommunity448%2FComms%2FRecordings&nav=%7B%22playbackOptions%22%3A%7B%22startTimeInSeconds%22%3A1%2E938248%7D%7D)

  - This video talks through accessing Databricks notebooks
  - Accessing RStudio on the DASH Platform
  - Databricks Filestore 


## The DASH Platform playbook

The DASH Platform playbook gives a detailed account of how the platform will operate over the next few years, detailing all the features as well as governance around the platform.  
It is available on the Posit server:
[DASH Platform playbook](https://dap-prd2-connect.azure.defra.cloud/DASH-Playbook/)

## Datalake

- The Data catalogue is a Power BI dashboard giving a search for location of the governed dataset available.

- [Importing your own data to the DASH Platform](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/Upload_data/)
  - Learn to load data onto the platform
  - Moving data to your folder in the lab zone

There a 2G limit on importing files in this method. Dataset above this limit or if they are of potential use to others can be requested to be added through the issue tracker on Teams.

## Databricks notebooks

Databricks notebooks can be used for writing Python, SQL, and R code, as well as a combination of the languages all within the same notebook.  

- [Example workflow in Databricks](https://defra.sharepoint.com/sites/Community448/Comms/Forms/AllItems.aspx?id=%2Fsites%2FCommunity448%2FComms%2FRecordings%2FCDAP%5Fdemo%5FPart2%5Fapples%5FTrim%2Emp4&parent=%2Fsites%2FCommunity448%2FComms%2FRecordings&nav=%7B%22playbackOptions%22%3A%7B%22startTimeInSeconds%22%3A0%2E95829%7D%7D): This video gives you an idea of what is possible
  - This example uses geospatial data from the DASH Platform
  - See how to create a dashboard using Python  

- [Databricks documentation](https://docs.microsoft.com/en-gb/azure/databricks/) offers lots of information easily accessible in one place, for a variety of tasks.
  - The documentation is based on a general set-up of Databricks, not all of which can be done on the DASH Platform; for example, you can use existing clusters, but not create your own.

### [DASH Platform training notebooks in Databricks](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/Databricks/Databricks_git/)

We have created training notebooks that you can load from this GitHub page into your DASH Platform workspace for practicing. Click the heading to access a guide on accessing this repo from Databricks, so you can load the notebooks into the platform and run the code.  

The following notebooks are available:  
- DASH Platform Demo - Data Combine (this is the notebook used in the videos linked above)   
- Data access user guide  
- ML flow and tensorboard user guide  

### Databricks Training

Databricks offer lots of training materials that are free to DEFRA employees to help utilise the Databricks workspace. Most of these courses are Python & SQL based and will require some prior knowledge so we recommend looking at the beginners courses that are highlighted further on.  

To access Databricks Learning, you can sign up [here](https://customer-academy.databricks.com/learn)
When using these notebooks provided by Databricks, it is important that you attach the notebook to the training cluster. The other clusters do not support the set up of the notebooks.

#### Python on Databricks 

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

- [Data Analysis with Databricks SQL](https://customer-academy.databricks.com/learn/course/internal/view/elearning/1035/data-analysis-with-databricks-sql): This course provides a comprehensive introduction to Databricks SQL. Learners will ingest data, write queries, produce visualizations and dashboards, and configure alerts. 
  - Import data and persist it in Databricks SQL as tables and views
  - Query data in Databricks SQL 
  - Use Databricks SQL to create visualizations and dashboards
  - Create alerts to notify stakeholders of specific events
  - Share queries and dashboards with others


## R and RStudio on the DASH Platform  

We have created training materials for working in RStudio on the DASH Platform.  

- [Getting started with RStudio on the DASH Platform](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/RStudio_Server/getting_started/): This is a guide for using RStudio within the DASH platform, for those familiar with R and RStudio, but new to the DASH platform. It contains:  
    - Opening and closing RStudio 
    - RStudio workspace  
    - Accessing and working with DASH Platform data from RStudio   
    - Uploading files into your workspace in RStudio  
    - This also includes instructions on how you can install packages and upload data, which you need to be able to do the [Introduction to R course](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training#training-materials-for-beginners)

- [Connecting RStudio to git and GitHub](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/RStudio_Server/git_and_github/): This course is a short version of getting connected as described in Jenny Bryan’s book, Happy Git with R, adapted to work for the DASH Platform. See the book here: [Let’s Git started. Happy Git and GitHub for the useR](https://happygitwithr.com). It contains:  
    - Connecting everything using GitHub's Personal Access Tokens  
    - Adding your GitHub repo to RStudio
    - Working with GitHub and your RStudio project  
    - For more about how to use GitHub, you can sign up for a Government Analysis Function course: [Intro to Git](https://analysisfunction.civilservice.gov.uk/training/introduction-to-git/).

- [Dashboards with Shiny and RStudio Connect](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/RStudio_Server/Create_dashboards/): This is a guide for creating a dashboard through Shiny in RStudio and publishing it on the Posit Connect Server (formerly RStudio Connect server). It contains:
    - Creating dashboards  
    - Publishing dashboards  
    - For more detailed information on building Shiny apps, see the [Shiny RStudio pages](https://shiny.rstudio.com/).  
    - For more information on RStudio Connect, see the [Posit Connect pages](https://posit.co/products/enterprise/connect/).

## Connecting VScode from the AVD (Azure Virtual Desktop) to Databricks

- [VScode guide](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/VSCode/VScode_guide/): This is a guide that will walk you through all the relevant steps to get you started on VScode

- This guide will show how to add init scripts to your personal cluster so you can manage your own environment.


## [Further training resources](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/further_training)  

This page details more courses that are available to you. These courses are not specific to the DASH Platform, but are useful for those new to programming in R, Python, or SQL, and also link to more advanced courses to make the most of the capabilities of the DASH Platform, such as Spark:  

- [Training for beginners](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/further_training/#Training_for_beginners)
    - R and RStudio training  
    - Python training  
    - SQL training  
- [More advanced training](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/further_training/#More_advanced_training)
    - Government Analysis Function courses  
    - Geospatial courses  
- [Resources for good practice](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/further_training/#Resouces_for_good_practice)
- [Table of links](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/further_training/#Table_of_links)
