input <- readLines("inputs/day6.txt") %>%
    strsplit("") %>%
    unlist()

for (i in seq_len(length(input) - 3)) {
    if (length(unique(input[seq(i, i + 3)])) == 4) {
        break
    }
}

print(i + 3)
