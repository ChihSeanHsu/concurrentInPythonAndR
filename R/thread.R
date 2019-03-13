# Examples for the R and Parallel Computing blog in COS website （cos.name)
# Author: Peng Zhao, 8/30/2016

# Example 2: Using MultiThreading Functions
# comparison of single thread and multiple threads run
# using Internal function to set thread numbers, not very grace, but don't find a good way till now.
# Ang suggestion?
setNumThreads <- function(nums=1) {
  .Internal(setMaxNumMathThreads(nums));
  .Internal(setNumMathThreads(nums));
}

# Testing dist funciton with single (1) and multiple (20) threads
for(i in 6:11) {
  print(paste0('-------', i, '---------'))
  ORDER <- 2^i
  m <- matrix(rnorm(ORDER*ORDER),ORDER,ORDER);
  setNumThreads(1)
  res <- system.time(d <- dist(m))
  print(res)
  setNumThreads(20)
  res <- system.time(d <- dist(m))
  print(res)
}

# [1] "-------6---------"
# user  system elapsed 
# 0       0       0 
# user  system elapsed 
# 0.000   0.001   0.000 
# [1] "-----------"
# [1] "-------7---------"
# user  system elapsed 
# 0.001   0.001   0.002 
# user  system elapsed 
# 0.004   0.000   0.001 
# [1] "-----------"
# [1] "-------8---------"
# user  system elapsed 
# 0.024   0.000   0.024 
# user  system elapsed 
# 0.048   0.000   0.006 
# [1] "-----------"
# [1] "-------9---------"
# user  system elapsed 
# 0.201   0.000   0.202 
# user  system elapsed 
# 0.418   0.000   0.049 
# [1] "-----------"
# [1] "-------10---------"
# user  system elapsed 
# 2.415   0.000   2.416 
# user  system elapsed 
# 4.751   0.003   0.492 
# [1] "-----------"
# [1] "-------11---------"
# user  system elapsed 
# 30.467   0.006  30.496 
# user  system elapsed 
# 81.429   0.116   8.025 