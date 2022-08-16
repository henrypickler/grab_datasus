#install.packages("read.dbc") You need this package
library("read.dbc")

dbc2dbf <- function(rawDir, convertedDir, file) {
    # reads dbc file
    x <- read.dbc(paste(rawDir, file, sep=""))
    # write it to csv
    write.csv(x, file=paste(convertedDir, substring(file, 1, nchar(file)-4), ".csv", sep=""), fileEncoding = "UTF-8")
}

args = commandArgs(trailingOnly=TRUE)
dbc2dbf(args[1], args[2], args[3])