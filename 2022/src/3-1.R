score <- c(letters, LETTERS)

split_in_half <- function(x) {
    half <- length(x) / 2
    intersect(
        head(x, half), tail(x, half)
    )
}

readLines("inputs/day3.txt") %>%
    strsplit(split = "") %>%
    lapply(split_in_half) %>%
    match(score) %>%
    sum() %>%
    print()
