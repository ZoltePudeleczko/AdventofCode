library(tidyverse)

lines <- readLines("inputs/day8.txt")
tokens <- strsplit(lines, "")
token_lengths <- lengths(tokens)

trees <- matrix(NA, nrow = length(lines), ncol = max(token_lengths))

for (i in seq_along(lines)) {
    trees[i, seq_len(token_lengths[i])] <- as.numeric(tokens[[i]])
}

visibility <- matrix(FALSE, nrow = nrow(trees), ncol = ncol(trees))

for (row in seq_len(nrow(trees))) {
    for (col in seq_len(ncol(trees))) {
        if (row == 1 || row == n_row || col == 1 || col == n_col) {
            visibility[row, col] <- TRUE
            next
        }

        tree <- trees[row, col]

        above <- trees[seq(1, row - 1), col]
        below <- trees[seq(n_row, row + 1), col]
        left <- trees[row, seq(1, col - 1)]
        right <- trees[row, seq(n_col, col + 1)]

        if (all(tree > above) ||
            all(tree > below) ||
            all(tree > left) ||
            all(tree > right)) {
            visibility[row, col] <- TRUE
            next
        }
    }
}

sum(res) %>%
    print()
