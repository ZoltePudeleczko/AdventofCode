input <- readLines("inputs/day1.txt") |>
  as.numeric()

result <- split(input, cumsum(is.na(input))) |>
  vapply(sum, na.rm = TRUE, FUN.VALUE = numeric(1)) |>
  max()

print(result)
