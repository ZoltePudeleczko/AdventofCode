input <- readLines("inputs/day6.txt") %>%
    strsplit("") %>%
    unlist()

for (i in seq_len(length(input) - 13)) {
    if (length(unique(input[seq(i, i + 13)])) == 14) {
        break
    }
}

print(i + 13)
