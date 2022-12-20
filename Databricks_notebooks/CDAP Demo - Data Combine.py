# Databricks notebook source
# MAGIC %md 
# MAGIC # The DASH Platform Quick Tour Notebook
# MAGIC 
# MAGIC Covering:
# MAGIC - The Databricks Workspace in the DASH Platform
# MAGIC - RStudio
# MAGIC - Accessing data
# MAGIC - Example notebook workflow
# MAGIC - Sharing results through a Dashboard
# MAGIC 
# MAGIC  More advanced preview:
# MAGIC  - Spark capabilities

# COMMAND ----------

# MAGIC %md
# MAGIC ## The Databricks Notebook Environment
# MAGIC 
# MAGIC The main prod-zone of the platform is built around a Databricks workspace. 
# MAGIC 
# MAGIC Databricks Notebooks are one way of working in this space

# COMMAND ----------

# MAGIC %md
# MAGIC ### DASH Platform High level Design
# MAGIC 
# MAGIC Notebooks can be *documented* with **markdown** cells 
# MAGIC 
# MAGIC This can include images
# MAGIC 
# MAGIC ![High Level Design](files/Demo/HighLevelDesign.png) 
# MAGIC 
# MAGIC This image of the architecture is only available internally on the platform

# COMMAND ----------

# MAGIC %md
# MAGIC Multiple languages (Python, R and SQL) can be used in the same notebook. RStudio is accessed through  compute > select RStudio cluster > Apps > Launch RStudio

# COMMAND ----------

# MAGIC %r 
# MAGIC x <- "Demo Using R in a notebook"
# MAGIC print(x)

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Run SQL"

# COMMAND ----------

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
# MAGIC "Mounted" data is in storage that has been made accessible to this cluster (e.g. the DASH Platform datalake).
# MAGIC 
# MAGIC ___
# MAGIC **Governed Data in the Data Catalogue**
# MAGIC 
# MAGIC This is data stored in the Azure Data Lake **base** container, with information available in the [Data Catalogue](https://defra.sharepoint.com/:x:/r/teams/Team552/_layouts/15/Doc.aspx?sourcedoc=%7B7C345456-E15C-4F47-B474-985D0AAE7F14%7D&file=CDAP%20Data%20Catalogue.xlsx&action=default&mobileredirect=true)
# MAGIC 
# MAGIC ---
# MAGIC **Using dbutils**
# MAGIC 
# MAGIC %fs is shorthand for dbutils.fs which provides utilities for working with FileSystems

# COMMAND ----------

# MAGIC %fs ls mnt/base/unrestricted

# COMMAND ----------

dbutils.fs.mounts()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Upload data into Filestore manually
# MAGIC 
# MAGIC Small datasets can be uploaded ad-hoc into the filestore through browsing or drag and drop

# COMMAND ----------

# MAGIC %md
# MAGIC # Example Problem: Planning (or preventing) an Apple Heist on the National Trails
# MAGIC 
# MAGIC **Question: How many apple orchards are accessible to walkers on the national trail in the Cotswolds?**
# MAGIC 
# MAGIC Sample question to demonstrate the benefits of combining datasets on the DASH Platform using open datasets that are already available in data lake

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Import libraries
# MAGIC 
# MAGIC Each databricks notebook has it's own environment, pre-approved libraries can be installed onto the driver node using %pip on each notebook. Available libraries can be listed with %pip list.

# COMMAND ----------

# MAGIC %pip list

# COMMAND ----------

# If cluster has been restarted need to reinstall these libraries
%pip install geopandas
%pip install rtree

# COMMAND ----------

#Bring in geopandas and matplotlib so we can analyse and look at the geospatial data
import geopandas as gpd
import matplotlib as plt

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Read in Datasets
# MAGIC 
# MAGIC We will use Natural England's traditional orchards dataset and the National Trails dataset from "General Access" as well as a local authority file that was manually uploaded to the Filestore.

# COMMAND ----------

#Path to the general access folder
path = ('/dbfs/mnt/migrated-landing/General Access/')

#Read in traditional orchards dataset
orchards_gdf = gpd.read_file(path+'traditional_orchards/JSON/Traditional_Orchards_HAP_England.json')

#Read in national trail dataset
trail_gdf = gpd.read_file(path+'national_trails_england/JSON/National_Trails_England.json')

#Read in english local authority borders (manually uploaded to Filestore) for plotting
boundary_gdf = gpd.read_file('/dbfs/FileStore/Demo/LA.json')

#Reproject the local authority boundaries to British National Grid: Most of the governed geospatial data is already in BNG
boundary_gdf = boundary_gdf.set_crs("epsg:4326").to_crs("epsg:27700")

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Have a Look at the orchards and trails using Geopandas and MatPlotlib

# COMMAND ----------

#Get the bounding box for england from the local authorities dataset
minx, miny, maxx, maxy = boundary_gdf.boundary.total_bounds

#Plot the national trails and traditional orchards across England
ax = orchards_gdf.plot(kind = 'geo', color='green', figsize=(18,9), aspect='equal')
ax.axis('off')
trail_gdf.plot(ax = ax, column = 'name', cmap = 'rainbow', legend = True, legend_kwds={'loc': 'upper left'})
boundary_gdf.boundary.plot(ax=ax, color='k', linewidth=.1)
ax.set_xlim(minx-100000, maxx)
ax.set_ylim(miny, maxy)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Focus in on apples and the Cotswold Way

# COMMAND ----------

# DBTITLE 1,Find Orchards that contain Apples
#Count the number of orchards in dataset
num_orchards = orchards_gdf.objectid.count()

apples_gdf = orchards_gdf[orchards_gdf.apple=='Y']
num_apples = apples_gdf.objectid.count()

print("There are {} traditional orchards of which {} contain apples".format(num_orchards, num_apples))

# COMMAND ----------

# DBTITLE 1,Filter down to just the Cotswold Way
#Hard coding this for now, better practice would be to have a trail vairiable so different trails could be explored
cotswold_gdf = trail_gdf[trail_gdf['name'] == 'Cotswold Way']

#find route bounding box  of the Cotswold way 
cminx, cminy, cmaxx, cmaxy = cotswold_gdf.boundary.total_bounds

# COMMAND ----------

ax = cotswold_gdf.plot(kind = 'geo', color='blue', figsize=(18,9), aspect='auto')
boundary_gdf.boundary.plot(ax=ax, color='k', linewidth=.1)
orchards_gdf.plot(ax = ax, color = 'green') #plot all orchards in green
apples_gdf.plot(ax = ax, color = 'red') # plot apple orchards in red
ax.set_xlim(cminx- 7000, cmaxx)
ax.set_ylim(cminy, cmaxy)
# ax.set_xlim(cminx - 5000, cmaxx - 20000)
# ax.set_ylim(cminy + 27000, cmaxy - 25000)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Perform Geospatial join to find apples within certain distance of the route

# COMMAND ----------

# DBTITLE 1,Choose a distance from path with a widget
#Using either 300m or the distance selected in widget create a buffered geometry of the Cotswold Way
#dist = 300

#Create a widget
dbutils.widgets.dropdown("Distance(m)", "300", ["10", "100", "300", "1000"])

dist = dbutils.widgets.get("Distance(m)")

#Make the polygon describing the area within dist of the selected route
buffered_gdf = cotswold_gdf.buffer(int(dist))

# COMMAND ----------

#Remove all widgets
dbutils.widgets.removeAll()

# COMMAND ----------

# DBTITLE 1,Perform Geospatial Join to find apple orchards within buffer zone
buffer_gdf = gpd.GeoDataFrame(geometry=buffered_gdf.geometry)
close_apples = gpd.sjoin(apples_gdf, buffer_gdf, how='inner', predicate='intersects')

# COMMAND ----------

targets = close_apples.objectid.count()
print("There are {} orchards that can be targeted within {}m of the Cotswold way route to steal apples".format(targets, dist))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Dashboard
# MAGIC 
# MAGIC Dashboards can be set up quickly from notebooks and shared with other DASH Platform users. Dashboarding also available through RShiny
# MAGIC 
# MAGIC These can be updated by re-running the notebook either through the dashboard using the "Update" button or by scheduling the notebook to run at a regular time.

# COMMAND ----------

#Plot the route with the buffer zone, zoom into an area to make orchards more visible
ax = orchards_gdf.plot(color = 'green', figsize=(18,9), aspect='auto') #plot all orchards in green
boundary_gdf.boundary.plot(ax=ax, color='k', linewidth=.1)
cotswold_gdf.plot(ax=ax, color = 'blue')
buffered_gdf.plot(ax = ax, color='blue', alpha=0.2)
apples_gdf.plot(ax = ax, color = 'red') # plot apple orchards in red
ax.set_xlim(cminx - 4000, cmaxx - 20000)
ax.set_ylim(cminy + 27000, cmaxy - 25000)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Save data into lab/unrestricted zone

# COMMAND ----------

#Make a directory folder in the lab container if it doesn't already exist
#%fs mkdirs /mnt/lab/unrestricted/firstname.lastname@defra.gov.uk/

# COMMAND ----------

#Save our apples dataset
close_apples.to_file("/dbfs/mnt/lab/unrestricted/firstname.lastname@defra.gov.uk/apples_within_" + str(dist) + "m.json")


# COMMAND ----------

# MAGIC %md
# MAGIC ## Use Spark to efficiently explore larger datasets
# MAGIC 
# MAGIC Using packages like geopandas is great as long as the dataset is not too large. Big datasets can be more efficiently explored using Spark

# COMMAND ----------

# MAGIC %md
# MAGIC Image from files.training.databricks.com
# MAGIC ![](https://files.training.databricks.com/images/sparkcluster.png)

# COMMAND ----------

orchards_sdf = (spark.read
                .option("inferSchema", True)
                .json("/mnt/migrated-landing/General Access/traditional_orchards/JSON/Traditional_Orchards_HAP_England.json"))

# COMMAND ----------

from pyspark.sql.functions import *

orchards_simple_sdf = (orchards_sdf.withColumn("features", explode("features"))
                                     .select("features.attributes.objectid","features.attributes.habconditi", "features.attributes.area_ha", "features.attributes.apple","features.attributes.pear", "features.attributes.brambles"))
orchards_simple_sdf.count()


# COMMAND ----------

contains_fruit_sdf = (orchards_simple_sdf.withColumn("habitat_condition",
                                                     when(col("habconditi")==" ", "n/a")
                                                     .otherwise(col("habconditi")))
                      .withColumn("contains_apples", col("apple").isin("Y", "y"))
                      .withColumn("contains_pears", col("pear").isin("Y", "y"))
                      .withColumn("contains_brambles", col("brambles").isin("Y", "y"))
                      .drop("apple", "habconditi", "pear", "brambles"))

# COMMAND ----------

display(contains_fruit_sdf)

# COMMAND ----------

apple_orchard_conditions = contains_fruit_sdf.groupBy("habitat_condition", "contains_apples").agg(
  avg("area_ha").alias("Average Orchard Area (Ha)"),
  sum("area_ha").alias("Total area (Ha)"),
  sum(col("contains_apples").cast("long")).alias("Contains apples"),
  sum(col("contains_pears").cast("long")).alias("Contains pears"), 
  sum(col("contains_brambles").cast("long")).alias("Contains brambles"), 
).orderBy(col("contains_apples"), col("Total area (Ha)").desc())

# COMMAND ----------

display(apple_orchard_conditions)

# COMMAND ----------

contains_fruit_sdf.createOrReplaceTempView("orchards") 

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT habitat_condition, area_ha  FROM orchards WHERE habitat_condition IN ("Poor", "Good", "Excellent")

# COMMAND ----------

# MAGIC %md
# MAGIC Currently the spark and SQL capabilities are not suited to geospatial operations, but options to work efficiently with large geospatial datasets have been explored in Proof of Value projects 1 (raster data) and 2 (vector data). Cluster configurations can be adapted to this type of work.

# COMMAND ----------


