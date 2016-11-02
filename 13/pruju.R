#!/usr/bin/env Rscript

png(file = "pairgraphic.png", width=900, height=400)

datas <- read.csv("pairdata", header=FALSE, sep=",")

plot(datas$V1, datas$V2, col="red", main=("Flow count with netmask  (source on x-axis)"), xlab=" ", ylab=("Flow count"), xaxt="n", log="y")

axis(1, las=3, cex.axis=0.7, at=seq(0, 470, by=18.8), labels=c("1.0.0.0", "10.0.0.0", "20.0.0.0", "30.0.0.0", "40.0.0.0", "50.0.0.0", "60.0.0.0", "70.0.0.0", "80.0.0.0", "90.0.0.0", "100.0.0.0", "110.0.0.0", "120.0.0.0", "130.0.0.0", "140.0.0.0", "150.0.0.0", "160.0.0.0", "170.0.0.0", "180.0.0.0", "190.0.0.0", "200.0.0.0", "210.0.0.0", "220.0.0.0", "230.0.0.0", "240.0.0.0", "250.0.0.0"))

dev.off()
