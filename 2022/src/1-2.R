input <- readLines("inputs/day1.txt") |>
  as.numeric()

calories <- split(input, cumsum(is.na(input))) |>
  vapply(sum, na.rm = TRUE, FUN.VALUE = numeric(1)) |>
  sort(decreasing = TRUE)

print(sum(result[1:3]))
