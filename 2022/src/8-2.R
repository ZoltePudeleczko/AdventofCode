library(tidyverse)

lines <- readLines("inputs/day8.txt")
tokens <- strsplit(lines, "")
token_lengths <- lengths(tokens)

trees <- matrix(NA, nrow = length(lines), ncol = max(token_lengths))

for (i in seq_along(lines)) {
    trees[i, seq_len(token_lengths[i])] <- as.numeric(tokens[[i]])
}

scenic_score <- matrix(FALSE, nrow = nrow(trees), ncol = ncol(trees))

distances <- function(trees, tree, rows, cols) {
    above <- trees[rows, cols]
    suppressWarnings(distance <- min(which(!(tree > above))))
    if (distance == Inf) {
        distance <- length(above)
    }
    distance
}

for (row in seq_len(nrow(trees))) {
    for (col in seq_len(ncol(trees))) {
        tree <- trees[row, col]
        total <- 1

        if (row > 1) {
            distance <- distances(trees, tree, seq(row - 1, 1), col)
            total <- total * distance
        }

        if (row < n_row) {
            distance <- distances(trees, tree, seq(row + 1, n_row), col)
            total <- total * distance
        }

        if (col > 1) {
            distance <- distances(trees, tree, row, seq(col - 1, 1))
            total <- total * distance
        }

        if (col < n_col) {
            distance <- distances(trees, tree, row, seq(col + 1, n_col))
            total <- total * distance
        }
        scenic_score[row, col] <- total
    }
}

max(scenic_score) %>%
    print()
