library(purrr)

as_sequences <- function(x) {
    list(seq(x[1], x[2]), seq(x[3], x[4]))
}

fully_contains <- function(x) {
    length(setdiff(unlist(x[1]), unlist(x[2]))) == 0 ||
        length(setdiff(unlist(x[2]), unlist(x[1]))) == 0
}

input <- readLines("inputs/day4.txt") |>
    strsplit("[-,]") |>
    map(as.integer) %>%
    map(as_sequences) %>%
    map_lgl(fully_contains) %>%
    sum() %>%
    print()
