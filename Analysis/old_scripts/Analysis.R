library(bigchess)
library(chess)
library(ggrepel)

data_import <- read.csv("../../lichess-api-queries/data_from_queries/position_data_white_attacking.txt", sep="\t")
data_import_2 <- read.csv("../../lichess-api-queries/data_from_queries/position_data_black_attacking.txt", sep="\t")
data_import <- read.csv("../../lichess-api-queries/data_from_queries/position_data_white_attacking_merged.txt", sep="\t")
data_import <- read.csv("../../lichess-api-queries/data_from_queries/old_position_data_white_attacking.txt", sep="\t")
data_import <- read.csv("../../lichess-api-queries/data_from_queries/run_to_above_32000_position_data_white_attacking.txt", sep="\t")
data_import <- read.csv("../../Analysis/processed_data/filtered_data_san_fen_cluster.tsv", sep="\t")
data_import <- read.csv("../../Analysis/processed_data/black_filtered_data_san_fen_cluster.tsv", sep="\t")
cluster_representatives_without_analysis <- read.csv("../../Analysis/processed_data/white_cluster_representatives_without_analysis.tsv", sep="\t")
cluster_representatives_with_analysis <- read.csv("../../Analysis/processed_data/white_cluster_representatives_with_analysis.tsv", sep="\t")

filtered_data <- data_import

# For white
filtered_data <- data_import[data_import$prob_trimmed > 0.1 & data_import$prob > 0.01 & data_import$white_win_prob > 0.55 & data_import$white_wins + data_import$draws + data_import$black_wins > 500,]

# For black
filtered_data_2 <- data_import[data_import$prob_trimmed > 0.1 & data_import$prob > 0.01 & data_import$black_win_prob > 0.55 & data_import$white_wins + data_import$draws + data_import$black_wins > 500,]

# For white
filtered_data <- filtered_data[rev(order(filtered_data$white_win_prob)),]

# For black
filtered_data <- filtered_data[rev(order(filtered_data$black_win_prob)),]
#filtered_data <- head(filtered_data, n=1000)

# This step is a little slow
filtered_data$san <- sapply(gsub(",", " ", filtered_data$UCI_moves), bigchess::lan2san)

View(filtered_data)

as.list(strsplit(gsub("[0-9]+\\. ", "", filtered_data$san[2]), " ")[[1]])

idx <- sample(nrow(data_import), size=1)
bigchess::lan2san(gsub(",", " ", data_import$UCI_moves[idx]))

# Cluster data
filtered_data$cluster <- paste0("C", 1:nrow(filtered_data))
# Merge if one move sequence is a subset of another
for(i in 1:(nrow(filtered_data)-1)) {
  for(j in (i+1):nrow(filtered_data)) {
    if(grepl(filtered_data$UCI_moves[i], filtered_data$UCI_moves[j], fixed=TRUE) | grepl(filtered_data$UCI_moves[j], filtered_data$UCI_moves[i], fixed=TRUE)) {
      for(k in 1:i) {
        if(filtered_data$cluster[k] == filtered_data$cluster[i]) {
          filtered_data$cluster[k] <- filtered_data$cluster[j]
        }
      }
    }
  }
}
# Make any white Bh6 move the same cluster
for(i in 1:nrow(filtered_data)) {
  if(grepl(". Bh6", filtered_data$san[i], fixed=TRUE)) {
    filtered_data$cluster[i] <- paste0("C", nrow(filtered_data) + 1)
  }
}

plot(filtered_data$prob_trimmed, filtered_data$white_win_prob)
plot(filtered_data$prob, filtered_data$white_win_prob)
plot(log(filtered_data$prob_trimmed), filtered_data$white_win_prob)

filtered_data_deduplicated <- filtered_data[!duplicated(filtered_data$cluster_idx),]


plot(filtered_data_deduplicated$prob, filtered_data_deduplicated$white_win_prob)

p1 = c(0,0.75)
p2 <- c(0.07, 0.55)
slope = (p2[2] - p1[2]) / (p2[1] - p1[1])

plot(filtered_data_deduplicated$prob, filtered_data_deduplicated$white_win_prob, col=as.numeric(filtered_data_deduplicated$white_win_prob - p1[2] < slope * (filtered_data_deduplicated$prob - p1[1]))+1)
filtered_data_deduplicated$labels <- paste0("Trap #", filtered_data_deduplicated$cluster_idx)
filtered_data_deduplicated$labels[filtered_data_deduplicated$white_win_prob - p1[2] < slope * (filtered_data_deduplicated$prob - p1[1])] <- NA

ggplot(filtered_data_deduplicated, aes(x = prob, y = white_win_prob)) +
  scale_x_continuous(labels = scales::percent_format(accuracy = 1)) +
  scale_y_continuous(labels = scales::percent_format(accuracy = 1)) +
  geom_point(size = 1) +
  theme_classic(base_size = 16) +
  geom_text_repel(
   aes(label=labels), 
   size=3,
   color="black",
  ) + 
  xlab("Probability of opponent making appropriate moves") +
  ylab("White win probability")

geoView(filtered_data_deduplicated[filtered_data_deduplicated$prob > 0.05,])

shortlist <- filtered_data_deduplicated[filtered_data_deduplicated$prob > 0.05,]

length(grep("Caro", data_import$Opening))
length(grep("French", data_import$Opening))
length(grep("Sicilian", data_import$Opening))

grep("Halloween", filtered_data$Opening)
grep("Halloween", filtered_data_deduplicated$Opening)

View(filtered_data_deduplicated[,c("Opening", "white_win_prob", "prob", "prob_trimmed", "san", "cluster_idx")])

filtered_data$cluster <- paste0("C", as.numeric(fct_inorder(filtered_data$cluster)))

filtered_data$cluster <- paste0("C", as.numeric(fct_inorder(filtered_data$cluster)))

# Some cleanup that was done for the first run because of an initial bug in the stockfish eval that needed to be rerun.
# cluster_representatives_without_analysis contained a stockfish rerun, and had an additional cluster step for Bxd8. 
cluster_representatives_without_analysis[which(cluster_representatives_without_analysis$san %in% setdiff(cluster_representatives_without_analysis$san, cluster_representatives_with_analysis$san)),]$cluster_idx <- 2
cluster_representatives_without_analysis <- cluster_representatives_without_analysis[!duplicated(cluster_representatives_without_analysis$cluster_idx),]
cluster_representatives_without_analysis$cluster_idx <- 1:nrow(cluster_representatives_without_analysis)
out <- merge(cluster_representatives_without_analysis, cluster_representatives_with_analysis[,c("san", "analysis_url")], by="san", all.x = TRUE)
out <- out[,colnames(cluster_representatives_with_analysis)]
out[out$move_index %% 2 == 1,]$stockfish_eval <- - out[out$move_index %% 2 == 1,]$stockfish_eval
write.table(out, file="../../Analysis/processed_data/white_cluster_representatives_with_analysis.tsv", sep="\t", row.names = FALSE, quote=FALSE)