# CDAP training
Here you can find training materials for using the Common Data Analytics Platform (CDAP). These materials were created by members of the Data Analytics and Science Hub (DASH) in core Defra. Feedback is welcome!  

To get an overview of the CDAP platform, head to the [DASH SharePoint site](https://defra.sharepoint.com/sites/Community448/SitePages/CDAP-The-Common-Data-Analytics-Platform.aspx).  

If you are completely new to coding, you can get an overview of different coding languages through the Government Analysis Function [here](https://analysisfunction.civilservice.gov.uk/training/awareness-of-new-coding-tools/).


## DASH playbook *link to follow*  

The DASH playbook gives a detailed account of how the Data Analytics and Science Hub (DASH) will operate over the next few years, and details all the features of CDAP, as well as governance around the platform.  


## [Introduction to CDAP](https://studious-fortnight-b9bc26d6.pages.github.io/introduction_to_cdap/)  

Click on the heading above to get an introduction to CDAP. It contains:  
- Logging in  
- Environments  
- Clusters 
- Data  
- Databricks workspace  

You can find a video showing how to access the platform through the browser [here](https://defra.sharepoint.com/sites/Community448/Comms/Forms/AllItems.aspx?id=%2Fsites%2FCommunity448%2FComms%2FRecordings%2FCDAP%5Fdemo%5FPart1%5Faccess%2Emp4&parent=%2Fsites%2FCommunity448%2FComms%2FRecordings&nav=%7B%22playbackOptions%22%3A%7B%22startTimeInSeconds%22%3A1%2E938248%7D%7D).  It contains:  
- Accessing Databricks notebooks  
- Accessing RStudio in CDAP  
- Databricks Filestore  

## [Databricks notebooks](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_demo_notebooks/tree/main/Databricks_notebooks)

Databricks notebooks can be used for writing Python, SQL, and R code, as well as a combination of the languages all within the same notebook.  

You can find a video showing an example workflow in Databricks, using geospatial data from the governed data in CDAP to create a dashboard using Python, [here](https://defra.sharepoint.com/sites/Community448/Comms/Forms/AllItems.aspx?id=%2Fsites%2FCommunity448%2FComms%2FRecordings%2FCDAP%5Fdemo%5FPart2%5Fapples%5FTrim%2Emp4&parent=%2Fsites%2FCommunity448%2FComms%2FRecordings&nav=%7B%22playbackOptions%22%3A%7B%22startTimeInSeconds%22%3A0%2E95829%7D%7D).  

Here you can find demo and training notebooks that work in Databricks itself.  
- CDAP Demo - Data Combine (this is the notebook used in the videos linked above)   
- Data access user guide  
- ML flow and tensorboard user guide  

You can access the Databricks documentation [here](https://docs.microsoft.com/en-gb/azure/databricks/).

To access Databricks Learning, follow the steps outlined [here](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training/blob/main/Databricks_notebooks/DEFRA%20-%20Free%20Learning%20Path%20Registration%20Instructions%20(1).pdf).


## [Access Notebooks from Dataricks](https://studious-fortnight-b9bc26d6.pages.github.io/Databricks_git/)

Click the heading to access a guide on accessing this repo from Databricks.

## Databricks Training

Databricks offer lots of training materials that are free to DEFRA employees to help utilise the Databricks workspace. Most of these courses are Python & SQL based will require some prior knwoledge so I recommend looking at the beginners courses that are highlighted further on.

### Python on Databricks 
Databricks offer lots of training materials that are free to DEFRA employees to help utilise the Databricks workspace. Most of these courses will require some prior knowledge of Python so I recommend looking at the beginners Python training first.

### [Apache Spark<sup>TM</sup> Programming with Databricks](https://customer-academy.databricks.com/learn/course/63/apache-spark-programming-with-databricks)

Because Databricks is built upon spark clusters this is a good course to start with in order ot make use of the Databricks workspace.
Spark can optimize queries, especially for big data.

#### Learning Objectives
- Identify core features of Spark & Databricks
- Apply the DataFrame transformation API to process and analyse data
- Apply Delta & Structured streaming to process streaming data

### [Scalable Machine Learning with Apache Spark](https://customer-academy.databricks.com/learn/course/128/scalable-machine-learning-with-apache-spark)

This course navigates the process of building machine learning solutions using Spark. You will build and tune ML models with SparkML using transformers, estimators, and pipelines. This course highlights some of the key differences between SparkML and single-node libraries such as scikit-learn. You will also reproduce your experiments and version your models using MLflow.

#### Learning Objectives
- Create data processing pipelines with Spark.
- Build and tune machine learning models with Spark ML.
- Track, version, and deploy models with MLflow.
- Perform distributed hyperparameter tuning with Hyperopt.
- Use Spark to scale the inference of single-node models.

### SQL on Databricks

### [Data Analysis with Databricks SQL](https://customer-academy.databricks.com/learn/course/1035/data-analysis-with-databricks-sql)
This course provides a comprehensive introduction to Databricks SQL. Learners will ingest data, write queries, produce visualizations and dashboards, and configure alerts. 
#### Learning Objectives
- Import data and persist it in Databricks SQL as tables and views
- Query data in Databricks SQL 
- Use Databricks SQL to create visualizations and dashboards
- Create alerts to notify stakeholders of specific events
- Share queries and dashboards with others


## RStudio training

Here you can find training for working in RStudio in CDAP.  

- [Getting started with RStudio in CDAP](https://studious-fortnight-b9bc26d6.pages.github.io/RStudio_in_CDAP/getting_started): This is a guide for using RStudio within CDAP, for those familiar with R and RStudio, but new to CDAP. It contains:  
    - Opening and closing RStudio 
    - RStudio workspace  
    - Accessing and working with CDAP data from RStudio   
    - Uploading files into your workspace in RStudio  

- [Connecting RStudio to git and GitHub](https://studious-fortnight-b9bc26d6.pages.github.io/RStudio_in_CDAP/git_and_github/): This course is a short version of getting connected as described in Jenny Bryan’s book, Happy Git with R, adapted to work for CDAP. See the book here: [Let’s Git started | Happy Git and GitHub for the useR](https://happygitwithr.com). It contains:  
    - Connecting everything using GitHub's Personal Access Tokens  
    - Adding your GitHub repo to RStudio
    - Working with GitHub and your RStudio project  
    - For more about how to use GitHub, you can sign up for a Government Analysis Function course: [Intro to Git](https://analysisfunction.civilservice.gov.uk/training/introduction-to-git/).

- Dashboards with Shiny and RStudio Connect *coming soon*  
    - Creating dashboards  
    - Publishing dashboards  
    - For more detailed information on building Shiny apps, see the [Shiny RStudio pages](https://shiny.rstudio.com/).  
    - For more information on RStudio Connect, see the [RStudio Connect pages](https://www.rstudio.com/products/connect/).


### Next steps with R and RStudio  


If you have used R and RStudio previously, the environment will look very familiar to you. If you are new to R and RStudio, we recommend you take a look at [courses from the Government Analysis Function](https://analysisfunction.civilservice.gov.uk/training-courses/?keyword=&training_category=&type=online&participation=&provider=&training_location=&submit=Go). These courses are open to analysts and scientists working in government.  

There is a whole host of introductory courses including:  
- [Introduction to R course](https://analysisfunction.civilservice.gov.uk/training/introduction-to-r/)    
- [Data visualisation in R and Python](https://analysisfunction.civilservice.gov.uk/training/data-visualisation-in-r-and-python/)  
- [Data linkage in R](https://analysisfunction.civilservice.gov.uk/training/data-linkage-in-r/)  
- [R control flow loops and functions](https://analysisfunction.civilservice.gov.uk/training/r-control-flow-loops-and-functions/)  
- [Data linkage in R](https://analysisfunction.civilservice.gov.uk/training/introduction-to-sparklyr/)   



There are also more advanced courses:  
- [Introduction to sparklyr](https://analysisfunction.civilservice.gov.uk/training/introduction-to-sparklyr/)  
- [Introduction to Reproducible Analytical Pipelines (RAP)](https://analysisfunction.civilservice.gov.uk/training/introduction-to-reproducible-analytical-pipelines-rap/)  
- [Machine learning in R](https://analysisfunction.civilservice.gov.uk/training/machine-learning-in-r/) 

## Python training

### Beginners Python Training
Just like for R, the Government Analysis Function offer lots of courses in R:
- [Introduction to Python](https://analysisfunction.civilservice.gov.uk/training/introduction-to-python/)
    - Perform basic coding
    - Import & export data
    - Manipulate basic Data
    - Perform a linear regression
    - Basic visualisation
- [Editing & imputation in Python](https://analysisfunction.civilservice.gov.uk/training/editing-and-imputation-in-python/)
    - Identifying missing values, visualising the missing value & finding duplicates in data.
    - Auto editing where you can apply restrictions, check which restrictions have been violated and correct them.
    - Impute missing values using model-based methods such as mean, meadian, ratio & regression imputation.
    - Impute missing values using donor-based imputations such as: random hot-deck, sequential hot-deck, hierarchical hot-deck & K-nearest neighbours imputation.
- [Python control flow loops & functions](https://analysisfunction.civilservice.gov.uk/training/python-control-flow-loops-and-functions/)
    - Use For & While loops
    - Use If, Elif & Else Control Flow
    - Write your own basic functions
    - Awareness of how functions can be applied to DataFrames 
    
## SQL Training
The Government Analysis Function offers just the one course for SQL.
### [Foundations of SQL](https://analysisfunction.civilservice.gov.uk/training/foundations-of-sql/)
This course will give you experience using the SQL methods of database querying, manipulation and editing. The course uses the SQLite flavour to give a solid foundation in the principles of relational databases and how to use them.
#### Learning Outcomes

- Query databases
- Join tables
- Edit tables
- Manipulate databases
This course will increase the participants confidence when working with databases for analysis and data science.

## Further resources

These government resources are relevant for good practice of writing code and undertaking analysis.  

- [Quality Assurance of Code for Analysis and Research](https://best-practice-and-impact.github.io/qa-of-code-guidance/intro.html)
    - This guide is about quality assurance of code  in government  
    - This includes core programming practices, structuring your project, code documentation, project documentation, version control, configuration, dData management, peer review, and testing code  
- [Reproducible Analytical Pipeline learning materials from the Data Science Campus](https://github.com/datasciencecampus/gov-uk-rap-materials)  
    - These training materials cover Reproducible Analytical Pipelines (RAP)
    - Includes introduction to RAP, using the RMySQL R package, git and git with R presentations and glossaries, tutorial on creating GANTT charts in R, and a template for using RMarkdown to create word documents  
- [Reproducible Analytical Pipeline companion](https://ukgovdatascience.github.io/rap_companion/)  
    - More on Reproducible Analytical Pipelines  
    - Includes chapters on version control, packaging code, unit testing, automated testing, code coverage, dependency and reproducibility, quality assurance of the pipeline, and producing the publication  
- [Spark at the ONS](https://best-practice-and-impact.github.io/ons-spark/intro.html)  
    - For readers familiar with Python or R  
    - If you need to process big data using PySpark in Python or sparklyr in R  
    - Python and R code cells throughout the book to help explain the topics covered  
