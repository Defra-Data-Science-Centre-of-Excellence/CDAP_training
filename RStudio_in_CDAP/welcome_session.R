# My first R script
2 + 2


## Functions use brackets ()
sum(2, 2)


## We can use additional libraries or packages to load more functions:
library(readr)
library(ggplot2)


## We can load data into RStudio using read_csv():
penguins <- readr::read_csv("/dbfs/mnt/lab/unrestricted/R_training/penguins.csv")
penguins_raw <- read_csv("/dbfs/mnt/lab/unrestricted/R_training/penguins_raw.csv")


## We can look at the whole dataset using View():
View(penguins)

## We can look at the structure of the dataset (incl types of variables) using str():
str(penguins)

## We can look at the structure of the dataset (incl types of variables) using str():
str(penguins)


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


