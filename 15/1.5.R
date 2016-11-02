#!/usr/bin/env Rscript
png(file = "1-5.png", width=1000, height=500)
continueslengths <- read.csv("continueslengthswithzeros", header=FALSE, sep=",")
continueslengths.ecdf = ecdf(continueslengths)
plot(continueslengths.ecdf, main=("Empirical cumulative distributions of flow lengths (zeros included)"), xlab=("Flow length (seconds)"), ylim=c(0, 1), xlim=c(0, 150))
dev.off()
