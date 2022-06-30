# CDAP training
Here you can find training materials for using the Common Data Analytics Platform (CDAP). These materials were created by members of the Data Analytics and Science Hub (DASH) in core Defra. Feedback is welcome!  

To get an overview of the CDAP platform, head to the [DASH SharePoint site](https://defra.sharepoint.com/sites/Community448/SitePages/CDAP-The-Common-Data-Analytics-Platform.aspx).  

If you are completely new to coding, you can get an overview of different coding languages through the Government Analysis Function [here](https://analysisfunction.civilservice.gov.uk/training/awareness-of-new-coding-tools/).


## [DASH playbook]() **add link**  

The DASH playbook gives a detailed account of how the Data Analytics and Science Hub (DASH) will operate over the next few years, and details all the features of CDAP, as well as governance around the platform.  


## [Introduction to CDAP](https://studious-fortnight-b9bc26d6.pages.github.io/introduction_to_cdap/)  

Click on the heading above to get an introduction to CDAP. It contains:  
- Logging in  
- Environments  
- Clusters  
- The Databricks workspace  
- Databricks notebooks and RStudio  

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


## RStudio training

Here you can find training for working in RStudio in CDAP.  

- [Getting started with RStudio in CDAP](https://studious-fortnight-b9bc26d6.pages.github.io/RStudio_in_CDAP/getting_started):  
    - Accessing RStudio 
    - Closing a session  
    - RStudio workspace  
    - Accessing CDAP data from RStudio  
    - Working with CDAP data in RStudio  
    - Uploading data into your workspace in RStudio  

- [Connecting RStudio to git and GitHub](https://studious-fortnight-b9bc26d6.pages.github.io/RStudio_in_CDAP/git_and_github/) *under construction*  

This course is a short version of getting connected as described in Jenny Bryan’s book, Happy Git with R, adapted to work for CDAP. See the book here: [Let’s Git started | Happy Git and GitHub for the useR](happygitwithr.com)  

    - Connecting everything using GitHub's Personal Access Tokens  
    - Adding your GitHub repo to RStudio
    - Working with GitHub and your RStudio project  

For more about how to use git and GitHub, you can sign up for a Government Statistical Service course: [Intro to Git](https://gss.civilservice.gov.uk/training/introduction-to-git/).

- RStudio connect *coming soon*  
    - Creating dashboards  
    - Publishing dashboards  


### Next steps with R and RStudio  


If you have used R and RStudio previously, the environment will look very familiar to you. If you are new to R and RStudio, we recommend you take a look at [courses from the Government Analysis Function](https://analysisfunction.civilservice.gov.uk/training-courses/?keyword=&training_category=&type=online&participation=&provider=&training_location=&submit=Go). These courses are open to There is a whole host of introductory courses including  
- [Introduction to R course](https://analysisfunction.civilservice.gov.uk/training/introduction-to-r/)    
- [Data visualisation in R and Python](https://analysisfunction.civilservice.gov.uk/training/data-visualisation-in-r-and-python/)  
- [Data linkage in R](https://analysisfunction.civilservice.gov.uk/training/data-linkage-in-r/)  
- [R control flow loops and functions](https://analysisfunction.civilservice.gov.uk/training/r-control-flow-loops-and-functions/)  
- [Data linkage in R](https://analysisfunction.civilservice.gov.uk/training/introduction-to-sparklyr/)   



There are also more advanced courses:  
- [Introduction to sparklyr](https://analysisfunction.civilservice.gov.uk/training/introduction-to-sparklyr/)  
- [Introduction to Reproducible Analytical Pipelines (RAP)](https://analysisfunction.civilservice.gov.uk/training/introduction-to-reproducible-analytical-pipelines-rap/)  
- [Machine learning in R](https://analysisfunction.civilservice.gov.uk/training/machine-learning-in-r/) 


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
    - Python and R code cells throughout the book to help explain the topics  