# Databricks notebook source
# MAGIC %md
# MAGIC ## Explore available data
# MAGIC There are a few ways to explore the accessible data
# MAGIC 
# MAGIC ___
# MAGIC 
# MAGIC **DataBricks File System:**
# MAGIC 
# MAGIC The workspace uses the the [Databricks File System (DBFS)](https://docs.databricks.com/data/databricks-file-system.html)
# MAGIC 
# MAGIC 
# MAGIC "Mounted" data is in storage that has been made accessible to this cluster (e.g. the CDAP datalake).
# MAGIC 
# MAGIC There are different zone's located within the mounted data, the 'landingr' folder is where you find data that has been processed ready to function.
# MAGIC The 'labr' folder will contain data that is created by users as part of their exploratory analytics and data science work.
# MAGIC 
# MAGIC 
# MAGIC ___
# MAGIC **Governed Data in the Data Catalogue**
# MAGIC 
# MAGIC This is data stored in the Azure Data Lake **landingr** container, with information available in the [Data Catalogue](https://defra.sharepoint.com/:x:/r/teams/Team552/_layouts/15/Doc.aspx?sourcedoc=%7B7C345456-E15C-4F47-B474-985D0AAE7F14%7D&file=CDAP%20Data%20Catalogue.xlsx&action=default&mobileredirect=true)
# MAGIC 
# MAGIC ---
# MAGIC **Using dbutils**
# MAGIC 
# MAGIC %fs is shorthand for dbutils.fs which provides utilities for working with FileSystems
# MAGIC 
# MAGIC %fs mounts can be used to display data that has been mounted to the cluster from the data lake
# MAGIC 
# MAGIC %fs ls "path" can be used to display files from a specific folder

# COMMAND ----------

# MAGIC %fs mounts

# COMMAND ----------

# MAGIC %fs ls "mnt/"

# COMMAND ----------

# MAGIC %fs ls "mnt/landingr/General Access"

# COMMAND ----------

# MAGIC %md
# MAGIC **FileStore**
# MAGIC 
# MAGIC You can also upload your own data to use into the FileStore. See the following image for how to do this.

# COMMAND ----------

# MAGIC %md
# MAGIC ![import](/files/tables/import.jpg)

# COMMAND ----------

# DBTITLE 1,How to view the contents of the FileStore
# MAGIC %fs ls /FileStore

# COMMAND ----------

# MAGIC %md
# MAGIC ## Saving Data
# MAGIC 
# MAGIC Follow these next steps for an example of loading data, manipulating it, and then saving it into your personal directory in the 'labr' folder.

# COMMAND ----------

import geopandas as gpd

# COMMAND ----------

# DBTITLE 1,Read in the flood risk areas dataset
flood_gdf = gpd.read_file("/dbfs/mnt/landingr/General Access/FloodRiskAreas/JSON/Flood_Risk_Areas.json")
display(flood_gdf)

# COMMAND ----------

# MAGIC %md
# MAGIC **We are only interested in flood sources from surface water so we make a new dataframe to just include this.**

# COMMAND ----------

surface_water = flood_gdf[flood_gdf["flood_source"] == "Surface Water"]
display(surface_water)

# COMMAND ----------

# DBTITLE 1,This creates your own directory in the 'labr' folder
#For example replace <YourUsername> with joe.bloggs@defra.gov.uk

%fs mkdirs /mnt/labr/<YourUsername>/

# COMMAND ----------

surface_water.to_file("/dbfs/mnt/labr/<YourUsername>/surface_water.json")

# COMMAND ----------

# DBTITLE 1,Now you can see the file saved in your directory
# MAGIC %fs ls /mnt/labr/andrew.simpson@defra.gov.uk

# COMMAND ----------


