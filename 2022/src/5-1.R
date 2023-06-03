library(tidyverse)

input <- read_lines("inputs/day5.txt")

cargo <- input[seq(1, which(input == "") - 2)] %>%
    strsplit("") %>%
    lapply(function(x) {
        gsub(" |\\]|\\[", "", x)
    }) %>%
    transpose() %>%
    lapply(setdiff, "") %>%
    setdiff(list())

cargo <- cargo[-1]

instructions <- input[seq(which(input == "") + 1, length(input))] %>%
    str_extract_all("[0-9]+") %>%
    map(as.integer)

for (inst in instructions) {
    from <- inst[2]
    to <- inst[3]
    amount <- inst[1]
    cargo[[to]] <- c(rev(head(cargo[[from]], amount)), cargo[[to]])
    cargo[[from]] <- tail(cargo[[from]], -amount)
}

map(cargo, head, 1) %>%
    unlist() %>%
    paste(collapse = "") %>%
    print()
