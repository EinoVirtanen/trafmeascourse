#!/usr/bin/env Rscript
png(file = "13.png", width=1000, height=500)
csv <- read.csv("pairs", header=FALSE, sep=",")
plot(csv$V1, csv$V2, main=("Amount of flows between source and destination pairs with netmask /8 (source on x-axis)"), xlab=" ", ylab=("Number of flows (N)"), xaxt="n", log="y")
axis(1, las=3, cex.axis=0.8, at=seq(0, 470, by=18.8), labels=c("1.0.0.0/8", "10.0.0.0/8", "20.0.0.0/8", "30.0.0.0/8", "40.0.0.0/8", "50.0.0.0/8", "60.0.0.0/8", "70.0.0.0/8", "80.0.0.0/8", "90.0.0.0/8", "100.0.0.0/8", "110.0.0.0/8", "120.0.0.0/8", "130.0.0.0/8", "140.0.0.0/8", "150.0.0.0/8", "160.0.0.0/8", "170.0.0.0/8", "180.0.0.0/8", "190.0.0.0/8", "200.0.0.0/8", "210.0.0.0/8", "220.0.0.0/8", "230.0.0.0/8", "240.0.0.0/8", "250.0.0.0/8"))
dev.off()
