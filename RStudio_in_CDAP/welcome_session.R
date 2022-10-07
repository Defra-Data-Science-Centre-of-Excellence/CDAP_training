# My first R script
2 + 2


## Functions use brackets ()
sum(2, 2)


## We can use additional libraries or packages to load more functions:
library(tidyverse)


## We can load data into RStudio using read_csv():
prices <- read_csv("/dbfs/mnt/migrated-landing/General Access/AgriPricing/API-csv-10dec20.csv")


## We can look at the types of variables in our dataset using str():
str(prices)


## To mkake plots in R, ggplot2 is a popular package:
ggplot(data = prices, aes(x = type, y = index)) +
  geom_boxplot()


## We can add more libraries by installing them first:
install.packages("palmerpenguins")
library(palmerpenguins)


## The palmerpenguin package contains data:
data(package = 'palmerpenguins')
str(penguins)


## We will now build up a more complex plot:
ggplot(data = penguins, aes(x = island, 
                            y = flipper_length_mm, 
                            colour = bill_length_mm)) +
  geom_jitter(alpha = 0.8, 
              size = 2)# +
  facet_grid(~species) +
  scale_colour_continuous(type = "viridis", 
                          option = "A", 
                          name = "Bill length\nin mm") +
  labs(x = "Island", 
       y = "Flipper length in mm") +
  theme_bw()


