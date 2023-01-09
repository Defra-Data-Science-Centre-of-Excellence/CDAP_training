# My first R script
2 + 2


## Functions use brackets ()
sum(2, 2)


## We can use additional libraries or packages to load more functions. 
## There is a suite of packages called the tidyverse which we will use today. 
## we will use the readr package for loading data, and ggplot2 for making plots.
library(readr)
library(ggplot2)


## We can load data into RStudio using read_csv():
penguins <- readr::read_csv("/dbfs/mnt/lab/unrestricted/R_training/penguins.csv")
penguins_raw <- read_csv("/dbfs/mnt/lab/unrestricted/R_training/penguins_raw.csv")


## We can look at the whole dataset using View():
View(penguins)

## We can look at the summary of the dataset (incl types of variables) using summary():
summary(penguins)

## We can look at the structure of the dataset (incl types of variables) using str():
str(penguins)

## we can also look at individual variables, for example using count():
count(penguins, species)


## To make plots in R, ggplot2 is a popular package:
ggplot2::ggplot(data = penguins, aes(x = island, 
                                     y = flipper_length_mm)) +
  geom_point()


## We will now build up a more complex plot:
ggplot(data = penguins, aes(x = island, 
                            y = flipper_length_mm, 
                            colour = bill_length_mm)) +
  geom_point(alpha = 0.8, 
              size = 2) +
  facet_grid(~species) +
  scale_colour_continuous(type = "viridis", 
                          option = "A", 
                          name = "Bill length\nin mm") +
  labs(x = "Island", 
       y = "Flipper length in mm") +
  theme_bw()


