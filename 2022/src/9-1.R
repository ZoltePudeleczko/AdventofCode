library(tidyr)
library(dplyr)

head <- c(0, 0)
tail <- c(0, 0)

tail_positions <- data.frame("data" = readLines("inputs/day9")) %>%
    apply(1, function(x) {
        split <- data.frame(strsplit(x, " "))
        move <- as.numeric(split[2, ])

        tails <- list(toString(c(0, 0)))

        for (i in seq(move)) {
            head <<- switch(split[1, ],
                "R" = c(head[1] + 1, head[2]),
                "L" = c(head[1] - 1, head[2]),
                "U" = c(head[1], head[2] + 1),
                "D" = c(head[1], head[2] - 1)
            )

            if (
                abs(head[1] - tail[1]) <= 1 &&
                    abs(head[2] - tail[2]) <= 1 &&
                    abs(head[1] - tail[1]) + abs(head[2] - tail[2]) <= 2) {
                next
            }

            if (head[1] == tail[1]) {
                tail <<- switch(split[1, ],
                    "U" = c(tail[1], tail[2] + 1),
                    "D" = c(tail[1], tail[2] - 1)
                )
            } else if (head[2] == tail[2]) {
                tail <<- switch(split[1, ],
                    "R" = c(tail[1] + 1, tail[2]),
                    "L" = c(tail[1] - 1, tail[2])
                )
            } else {
                if (head[1] > tail[1]) {
                    tail <<- c(tail[1] + 1, tail[2])
                } else {
                    tail <<- c(tail[1] - 1, tail[2])
                }

                if (head[2] > tail[2]) {
                    tail <<- c(tail[1], tail[2] + 1)
                } else {
                    tail <<- c(tail[1], tail[2] - 1)
                }
            }

            tails <- c(tails, toString(tail))
        }

        tails
    }) %>%
    unlist(recursive = FALSE)

tail_positions %>%
    unique() %>%
    length() %>%
    print()
