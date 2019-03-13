# 1000*30000 matrix
x <- matrix(rnorm(1000*30000), nrow=1000)

# sort and then get min of every rows

# use for loop
system.time({
  min.for <- rep(NA, nrow(x))
  for(i in 1:nrow(x)) min.for[i] <- sort(x[i,])[1]
})


# use lapply
system.time(min.lapply <- lapply(1:nrow(x), function(z) sort(x[z,])[1]))


# use multiprocessing
library('parallel')

# how many core we use
cl <- makeCluster(7)

# export
clusterExport(cl, "x")

# run
system.time(min.par <- parLapply(cl,1:nrow(x), function(z) sort(x[z,])[1]))

# must stop cluster after finish
stopCluster(cl)
