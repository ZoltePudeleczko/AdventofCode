score <- c(letters, LETTERS)

get_badge <- function(x) {
    intersect(x[[1]], x[[2]]) |>
        intersect(x[[3]])
}

input <- readLines("inputs/day3.txt") %>%
    strsplit(split = "")

split(input, rep(seq_len(length(input) / 3), each = 3)) %>%
    lapply(get_badge) %>%
    match(score) %>%
    sum() %>%
    print()
