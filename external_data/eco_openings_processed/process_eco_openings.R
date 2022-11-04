library(tidyverse)
library(bigchess)

setwd("~/Box/repos/Lichess_Trap_Finder/external_data/eco_openings_processed/")

eco_openings_a <- read.delim("../eco_openings/a.tsv", sep="\t", header=TRUE)
eco_openings_b <- read.delim("../eco_openings/b.tsv", sep="\t", header=TRUE)
eco_openings_c <- read.delim("../eco_openings/c.tsv", sep="\t", header=TRUE)
eco_openings_d <- read.delim("../eco_openings/d.tsv", sep="\t", header=TRUE)
eco_openings_e <- read.delim("../eco_openings/e.tsv", sep="\t", header=TRUE)

eco_openings <- rbind(eco_openings_a, eco_openings_b, eco_openings_c, eco_openings_d, eco_openings_e)

rm(eco_openings_a, eco_openings_b, eco_openings_c, eco_openings_d, eco_openings_e)

# Add a number to duplicated opening names
make.unique.2 = function(x, sep='.'){
  ave(x, x, FUN=function(a){if(length(a) > 1){paste(a, 1:length(a), sep=sep)} else {a}})
}
eco_openings$name.unique <- make.unique.2(eco_openings$name, sep=" ")

eco_openings$moves_commas <- gsub(" ", ",", eco_openings$moves)

write.table(eco_openings, file="eco_openings_unique_names.tsv", sep="\t", row.names = FALSE, quote=FALSE)
