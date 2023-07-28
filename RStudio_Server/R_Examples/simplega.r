# A simple GA example based on http://www.r-bloggers.com/genetic-algorithms-a-simple-r-example/
# Knapsack problem

# Needs to make use of two libraries - genalg for the GA and ggplot for the plotting:
# Need to make these available
# Can follow instructions here - http://www.r-bloggers.com/installing-r-packages/
# Or alternatively just type 
install.packages("genalg") 
library(genalg)
# Similarly:
install.packages("ggplot2") 
library(ggplot2)
# you can skip the install.packages step once both of this have been installed

# The next stage is to make the data available to the program. 
# This is going to be in the form of a dataframe (basically a table):
# we'll also assume the unions should be onions!
dataset <- data.frame(item = c("pocketknife", "beans", "potatoes", "onions", "sleeping bag", "rope", "compass"), 
survivalpoints = c(10, 20, 15, 2, 30, 10, 30), 
weight = c(1, 5, 10, 1, 7, 5, 1))
# See http://www.r-tutor.com/r-introduction/data-frame  for more details on data frames

# Then declare the maximum weight limit for the knapsack
weightlimit <- 20

# Representation
# A GA operates on chromosomes - vectors of 1's and 0's - so we need to consider how the 
# various solutions can be captured in this form
# Each element in the chromosome is going to correspond to one of the items in the dataset
# and a 1 means that item is going to be included, a 0 means it is not
# For example the definition, 
chromosome = c(1, 0, 0, 1, 1, 0, 0) 
# selects items 1, 4 and 5
# We can check this as follows:
chromosome == 1  
# will return TRUE FALSE FALSE TRUE TRUE FALSE FALSE
# and 
dataset[chromosome == 1, ] 
# will return the rows corresponding to the TRUE values i.e.
#           item survivalpoints weight
# 1  pocketknife             10      1
# 4       onions              2      1
# 5 sleeping bag             30      7
# (remember that the data frame is initially specified in terms of 3 columns)

# Fitness function
# The other important calculation is to determine how good a solution this is.
# The survival points corresponding to the solution can be found using the inner product
# of the chromosome and the survivalpoints element of the datasets
cat(chromosome %*% dataset$survivalpoints)
# i.e. this will multiply the elements of chromosome by the corresponding survival points entry
# and then sum the resulting values putting the results in a vector
# cat(...) then outputs the value in the resultant vector
# This forms the basic computation of the fitness function
#
# The genalg package tries to optimise towards minimum values, but we need to reward high values.
# One approach is to just negate the value (you could also try inverting it)
# Solutions which exceed the weight limit also need to be penalised, so when negative values
# are used then these are give the value 0. (This would not work if we were inverting it)
# This gives the entire fitness function (the parameter "x" will be passed each chromosome 
# - a vector of 1's and 0's corresponding to a solution - in turn by the GA):

evalFunc <- function(x) {  
    current_solution_survivalpoints <- x %*% dataset$survivalpoints
    current_solution_weight <- x %*% dataset$weight

    if (current_solution_weight > weightlimit) 
        return(0) else return(-current_solution_survivalpoints)
}

# This is pretty much the only programming that needs to be done!

# The next step is to configure and run the GA - which just needs several parameters
# and the fitness function to be supplied (all hard work is done for you).
GAmodel <- rbga.bin(size = 7, popSize = 200, iters = 100, mutationChance = 0.01, 
  elitism = T, evalFunc = evalFunc)
# rbga.bin is the algorithm within the genalg library that optimises binary chromosomes
# (there are anothers which optimise real numbers - floats 
# see documentation at http://cran.r-project.org/web/packages/genalg/index.html)
# The parameters are as follows:
# size is the lengths of the chromosome  (the string of 1's and 0's)
# popSize is the size of the population i.e. how many solutions it holds at any one time
# iters is how many times the algorithm iterates
# mutationChance is the probability of mutation (default is 1/size+1
# elitism defines the proportion of chromosomes that go forward to the next generation (about 20%)
# evalFunc is the evaluation (fitness function)
#
# You could also try adding in the argument verbose=TRUE which provides feedback when the GA
# is running - often helpful if you're not sure about how it is progressing. i.e.
GAmodel <- rbga.bin(size = 7, popSize = 200, iters = 100, mutationChance = 0.01, 
  elitism = T, evalFunc = evalFunc, verbose=TRUE)

# Otherwise the GA will just run quietly. To find out the results, make a call to the summary function
# and provide the model as an argument, and use cat to return the output:
cat(summary(GAmodel)) # packae upddates - used to be rbga.summary

# Amongst other things, this produces the best solution: 1 1 0 1 1 1 1 
# (slightly different to the value in the blog)
# To find out which items these correspond to, create a vector from the solution and 
# then use this to get a row slice of the dataset:
solution = c(1, 1, 0, 1, 1, 1, 1)
dataset[solution == 1, ]
# which will return
#           item survivalpoints weight
# 1  pocketknife             10      1
# 2        beans             20      5
# 4       onions              2      1
# 5 sleeping bag             30      7
# 6         rope             10      5
# 7      compass             30      1


# Finally it is useful to get an idea of just how good a solution this is (in relative terms)
# The code below calculates the number of survival points in the solution, the total possible and the total weight.
# paste then converts these all into a string and cat will output this
cat(paste(solution %*% dataset$survivalpoints, "/", sum(dataset$survivalpoints), "points with a weight of ", solution %*% dataset$weight))



