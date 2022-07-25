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
# MAGIC "Mounted" data is in storage that has been made accessible to this cluster (e.g. the CDAP datalake). There are different zone's located within the mounted data:
# MAGIC - base
# MAGIC - lab
# MAGIC - migrated-lab
# MAGIC - migrated-landing
# MAGIC 
# MAGIC ### base folder
# MAGIC 
# MAGIC The **base** folder is where you find data that has been processed and ready for consumption. All users will have 'read access' to the unrestricted folder. Each dataset will be catalogued in the [Data Catalogue](https://defra.sharepoint.com/:x:/r/teams/Team552/_layouts/15/Doc.aspx?sourcedoc=%7B7C345456-E15C-4F47-B474-985D0AAE7F14%7D&file=CDAP%20Data%20Catalogue.xlsx&action=default&mobileredirect=true)
# MAGIC 
# MAGIC ### lab folder
# MAGIC 
# MAGIC The **lab** folder will contain data that is created by users as part of their exploratory analytics and data science work. Users will access data from the base zone, once performing cleaning & transformations to the data it will be stored in the lab zone within an individual's directory. Be aware that data here is readable by all, this can help stop duplication of cleaned datasets. 
# MAGIC 
# MAGIC ### migrated-landing, migrated-lab
# MAGIC 
# MAGIC This is the data that was stored in the **landingr** & **labr** folders respectively in the previous release of CDAP. These are temporary storage areas and will be available until the CDAP team has agreed with users what loaded data is required. It will be communicated well in advance with users before these folders are removed.
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

# DBTITLE 1,We can check just the folder 'mnt' with the following command:
# MAGIC %fs ls "mnt/"

# COMMAND ----------

# DBTITLE 1,We can access the unrestricted subfolder of the base folder with:
# MAGIC %fs ls "mnt/base/unrestricted"

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
flood_gdf = gpd.read_file("/dbfs/mnt/base/unrestricted/source_defra_data_services_platform/dataset_flood_risk_areas/format_GEOJSON_flood_risk_areas/LATEST_flood_risk_areas/Flood_Risk_Areas.json")
display(flood_gdf)

# COMMAND ----------

# MAGIC %md
# MAGIC **We are only interested in flood sources from surface water so we make a new dataframe to just include this.**

# COMMAND ----------

surface_water = flood_gdf[flood_gdf["flood_source"] == "Surface Water"]
display(surface_water)

# COMMAND ----------

# DBTITLE 1,This creates your own directory in the 'lab' folder
#Replace <YourUsername> with joe.bloggs@defra.gov.uk and remove the '#'

# %fs mkdirs /mnt/lab/<YourUsername>/

# COMMAND ----------

#surface_water.to_file("/dbfs/mnt/labr/<YourUsername>/surface_water.json")

# COMMAND ----------

# DBTITLE 1,Now you can see the file saved in your directory
# %fs ls /mnt/lab/<YourUsername>

# COMMAND ----------


