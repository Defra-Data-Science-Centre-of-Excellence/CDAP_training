# CDAP training
Here you can find training materials for using the Common Data Analytics Platform (CDAP). These materials were created by members of the Data Analytics and Science Hub (DASH) in core Defra. Feedback is welcome! Please raise any issues in the [Issues](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training/issues) tab.

To get an overview of the CDAP platform, head to the [DASH SharePoint site](https://defra.sharepoint.com/sites/Community448/SitePages/CDAP-The-Common-Data-Analytics-Platform.aspx).  

If you are completely new to coding, you can get an overview of different coding languages through the Government Analysis Function [here](https://analysisfunction.civilservice.gov.uk/training/awareness-of-new-coding-tools/).  

These pages contain information and further links about the following topics:
- CDAP playbook  
- [Introduction to CDAP](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training#introduction-to-cdap) - get an overview of the platform   
- [Databricks notebooks](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training#databricks-notebooks) - used for analysis in Python, SQL, and R
- [Importing your own data to CDAP](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/Upload_data/)
- [Using Jupyter notebooks in databricks](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/jupyter_conversion/) - Using jupyter notebooks from GitHub in databricks
- [R and RStudio on CDAP](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training#r-and-rstudio-on-cdap) - find out how to work in R and RStudio on CDAP   
- [Training materials for beginners](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training#training-materials-for-beginners) - these materials are not specific to CDAP   
- [More advanced training and resources](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training#more-advanced-training-and-resources) - these materials are not specific to CDAP   


## CDAP playbook *links to follow*  

The CDAP playbook gives a detailed account of how CDAP will operate over the next few years, detailing all the features as well as governance around the platform.  


## [Introduction to CDAP](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/introduction_to_cdap/)  

Click on the heading above to get an introduction to CDAP. It contains:  
- Accessing CDAP  
- Environments , clusters and data  
- Databricks and RStudio workspaces  

You can find a video showing how to access the platform through the browser [here](https://defra.sharepoint.com/sites/Community448/Comms/Forms/AllItems.aspx?id=%2Fsites%2FCommunity448%2FComms%2FRecordings%2FCDAP%5Fdemo%5FPart1%5Faccess%2Emp4&parent=%2Fsites%2FCommunity448%2FComms%2FRecordings&nav=%7B%22playbackOptions%22%3A%7B%22startTimeInSeconds%22%3A1%2E938248%7D%7D).  It contains:  
- Accessing Databricks notebooks  
- Accessing RStudio in CDAP  
- Databricks Filestore  

## Databricks notebooks

Databricks notebooks can be used for writing Python, SQL, and R code, as well as a combination of the languages all within the same notebook.  

You can find a video showing an example workflow in Databricks, using geospatial data from the governed data in CDAP to create a dashboard using Python, [here](https://defra.sharepoint.com/sites/Community448/Comms/Forms/AllItems.aspx?id=%2Fsites%2FCommunity448%2FComms%2FRecordings%2FCDAP%5Fdemo%5FPart2%5Fapples%5FTrim%2Emp4&parent=%2Fsites%2FCommunity448%2FComms%2FRecordings&nav=%7B%22playbackOptions%22%3A%7B%22startTimeInSeconds%22%3A0%2E95829%7D%7D). This gives you an idea of what is possible!  

Databricks documentation offers lots of information easily accessible in one place, for a variety of tasks. You can access the Databricks documentation [here](https://docs.microsoft.com/en-gb/azure/databricks/).  

### [CDAP training notebooks in Databricks](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/Databricks_git/)

Click the heading to access a guide on accessing this repo from Databricks, so you can load the notebooks into CDAP and run the code.  

The following notebooks are available:  
- CDAP Demo - Data Combine (this is the notebook used in the videos linked above)   
- Data access user guide  
- ML flow and tensorboard user guide  

### Databricks Training

Databricks offer lots of training materials that are free to DEFRA employees to help utilise the Databricks workspace. Most of these courses are Python & SQL based will require some prior knwoledge so I recommend looking at the beginners courses that are highlighted further on.  

To access Databricks Learning, you can sign up [here](https://customer-academy.databricks.com/learn)
When using these notebooks provided by databricks, it is important that you attatch the notebook to the training cluster. The other clusters do not support the set up of the notebooks.

<!-- ![Training cluster](Databricks_git/images/Screenshot (96)_LI.jpg) -->
![Training cluster](https://github.com/Defra-Data-Science-Centre-of-Excellence/CDAP_training/blob/main/Databricks_git/images/Screenshot%20(96)_LI.jpg)


#### Python on Databricks 
Databricks offer lots of training materials that are free to DEFRA employees to help utilise the Databricks workspace. Most of these courses will require some prior knowledge of Python so I recommend looking at the beginners Python training first, see bottom of this page.

#### [Apache Spark<sup>TM</sup> Programming with Databricks](https://customer-academy.databricks.com/learn/course/internal/view/elearning/63/apache-spark-programming-with-databricks)

Because Databricks is built upon spark clusters this is a good course to start with in order ot make use of the Databricks workspace.
Spark can optimize queries, especially for big data.

##### Learning Objectives
- Identify core features of Spark & Databricks
- Apply the DataFrame transformation API to process and analyse data
- Apply Delta & Structured streaming to process streaming data

#### [Scalable Machine Learning with Apache Spark](https://customer-academy.databricks.com/learn/course/internal/view/elearning/128/scalable-machine-learning-with-apache-spark)

This course navigates the process of building machine learning solutions using Spark. You will build and tune ML models with SparkML using transformers, estimators, and pipelines. This course highlights some of the key differences between SparkML and single-node libraries such as scikit-learn. You will also reproduce your experiments and version your models using MLflow.

##### Learning Objectives
- Create data processing pipelines with Spark.
- Build and tune machine learning models with Spark ML.
- Track, version, and deploy models with MLflow.
- Perform distributed hyperparameter tuning with Hyperopt.
- Use Spark to scale the inference of single-node models.

#### SQL on Databricks

#### [Data Analysis with Databricks SQL](https://customer-academy.databricks.com/learn/course/internal/view/elearning/1035/data-analysis-with-databricks-sql)
This course provides a comprehensive introduction to Databricks SQL. Learners will ingest data, write queries, produce visualizations and dashboards, and configure alerts. 
##### Learning Objectives
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


## Training materials for beginners

If you have not coded before, there are lots of resources you can use to get you started. We recommend you take a look at [courses from the Government Analysis Function](https://analysisfunction.civilservice.gov.uk/training-courses/?keyword=&training_category=&type=online&participation=&provider=&training_location=&submit=Go). These courses are open to analysts and scientists working in government. 

### R and RStudio training 

There is a whole host of introductory courses for R and RStudio including:  
- [Introduction to R course](https://analysisfunction.civilservice.gov.uk/training/introduction-to-r/)  
    - For this course you need to be able to access R and RStudio, and some packages installed, and upload some data  
    - This is described in [Getting started with RStudio in CDAP](https://defra-data-science-centre-of-excellence.github.io/CDAP_training/RStudio_in_CDAP/getting_started/), so have a look at this together with the precourse information  
    - Do not install packages as described in the precourse information but follow the CDAP-specific instructions  
    - Upload the data as described in the CDAP specific information  
- [Data visualisation in R and Python](https://analysisfunction.civilservice.gov.uk/training/data-visualisation-in-r-and-python/)  
- [Data linkage in R](https://analysisfunction.civilservice.gov.uk/training/data-linkage-in-r/)  
- [R control flow loops and functions](https://analysisfunction.civilservice.gov.uk/training/r-control-flow-loops-and-functions/)  
- [Data linkage in R](https://analysisfunction.civilservice.gov.uk/training/introduction-to-sparklyr/)   


### Python training

Just like for R, the Government Analysis Function offer lots of courses in Python:
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
    
### SQL Training
The Government Analysis Function offers just the one course for SQL.
#### [Foundations of SQL](https://analysisfunction.civilservice.gov.uk/training/foundations-of-sql/)
This course will give you experience using the SQL methods of database querying, manipulation and editing. The course uses the SQLite flavour to give a solid foundation in the principles of relational databases and how to use them.
##### Learning Outcomes

- Query databases
- Join tables
- Edit tables
- Manipulate databases
This course will increase the participants confidence when working with databases for analysis and data science.

## More advanced training and resources  

### Government Analysis Function courses

The Government Analysis Function also offers more advanced courses, for example:  
- [Introduction to Reproducible Analytical Pipelines (RAP)](https://analysisfunction.civilservice.gov.uk/training/introduction-to-reproducible-analytical-pipelines-rap/) 
- [Introduction to sparklyr](https://analysisfunction.civilservice.gov.uk/training/introduction-to-sparklyr/)  
- [Introduction to Pyspark](https://analysisfunction.civilservice.gov.uk/training/introduction-to-pyspark/)  
- [Machine learning in R](https://analysisfunction.civilservice.gov.uk/training/machine-learning-in-r/)  
- [Introduction to machine learning in Python](https://analysisfunction.civilservice.gov.uk/training/introduction-to-machine-learning-in-python/)  

### Geospatial analysis

There are lots of resources for undertaking geospatial analysis in Python or R. CDAP has a geospatial cluster which is optimised for running geospatial analysis in Python, therefore making for much faster running of code.  Here are some examples of available courses:

- [University of Helsinki, Automating GIS-processes (Python)](https://autogis-site.readthedocs.io/en/latest/index.html)  
- [University of Liverpool, Geographic Data Science , Dani Arribas-Bel (Python)](https://darribas.org/gds_course/content/home.html)  
- [University of Colorado, EarthLab courses, tutorials and tools, Leah Wasser (Python and R)](https://www.earthdatascience.org/)  
- [University of Chicago, Spatial Data Science tutorials, Luc Anselin (R)](https://spatialanalysis.github.io/tutorials/)  


### Resouces for good practice  

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
    
# Table of links
    
| **Task**                                                                             | Training for using RStudio                                  | Training for using Python                                   |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **Introductory courses**                                                             | [GAF Introduction to R](https://analysisfunction.civilservice.gov.uk/training/introduction-to-r/)                                       | [GAF Introduction to Python](https://analysisfunction.civilservice.gov.uk/training/introduction-to-python/)                                  |
| **Data cleaning and wrangling including merging data and dealing with missing data** | [GAF Data Linkage in R](https://learninghub.ons.gov.uk/enrol/index.php?id=1245)                                       | [GAF Data Linkage in Python](https://learninghub.ons.gov.uk/enrol/index.php?id=1313)                                 |
| ****                                                                                 | [GAF Editing and imputation in R](https://analysisfunction.civilservice.gov.uk/training/editing-and-imputation-in-r/)                             | [GAF Editing and imputation in Python](https://analysisfunction.civilservice.gov.uk/training/editing-and-imputation-in-python/)                        |
| **Data visualisation**                                                               | [GAF Data visualisation in R and Python](https://analysisfunction.civilservice.gov.uk/training/data-visualisation-in-r-and-python/)                      | [GAF Data visualisation in R and Python](https://analysisfunction.civilservice.gov.uk/training/data-visualisation-in-r-and-python/)                      |
| **Creating dashboards**                                                              | [R Shiny dashboards](https://shiny.rstudio.com/tutorial/)                                          |                                                             |
| **Statistical modelling**                                                            | [GAF Statistics in R](https://gss.civilservice.gov.uk/training/statistics-in-r/)                                        |                                                             |
| ****                                                                                 | [Introduction to Bayesian data analysis](https://analysisfunction.civilservice.gov.uk/training/introduction-to-bayesian-data-analysis/)                      | [Introduction to Bayesian data analysis](https://analysisfunction.civilservice.gov.uk/training/introduction-to-bayesian-data-analysis/)                      |
| **Machine learning**                                                                 | [GAF Machine learning in R](https://analysisfunction.civilservice.gov.uk/training/machine-learning-in-r/)                                  | [GAF Machine learning in Python](https://analysisfunction.civilservice.gov.uk/training/introduction-to-machine-learning-in-python/)                             |
| **Spark programming for handling big data**                                          | [GAF Introduction to Sparklyr](https://analysisfunction.civilservice.gov.uk/training/introduction-to-sparklyr/)                                | [GAF Introduction to Pyspark](https://analysisfunction.civilservice.gov.uk/training/introduction-to-pyspark/)                                 |
| **Version control**                                                                  | [GAF command line basics](https://analysisfunction.civilservice.gov.uk/training/command-line-basics/)                                     | [GAF command line basics](https://analysisfunction.civilservice.gov.uk/training/command-line-basics/)                                     |
| ****                                                                                 | [GAF Introduction to git](https://analysisfunction.civilservice.gov.uk/training/introduction-to-git/)                                    | [GAF Introduction to git](https://analysisfunction.civilservice.gov.uk/training/introduction-to-git/)                                     |
| ****                                                                                 | [GitHub skills](https://skills.github.com/)                                               | [GitHub skills](https://skills.github.com/)                                               |
| **Reproducible analytical pipelines (RAP)**                                          | [GAF Introduction to Reproducible Analytical Pipelines (RAP)](https://analysisfunction.civilservice.gov.uk/training/introduction-to-reproducible-analytical-pipelines-rap/) | [GAF Introduction to Reproducible Analytical Pipelines (RAP)](https://analysisfunction.civilservice.gov.uk/training/introduction-to-reproducible-analytical-pipelines-rap/) |
