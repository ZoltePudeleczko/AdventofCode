library(tidyr)
library(dplyr)

knots <- data.frame(matrix(data = 0, nrow = 10, ncol = 2))

tail_positions <- data.frame("data" = readLines("inputs/day9")) %>%
    apply(1, function(x) {
        split <- data.frame(strsplit(x, " "))
        move <- as.numeric(split[2, ])

        for (i in seq(move)) {
            knots[1, 1] <<- switch(split[1, ],
                "R" = knots[1, 1] + 1,
                "L" = knots[1, 1] - 1
            )

            knots[1, 2] <<- switch(split[1, ],
                "U" = knots[1, 2] + 1,
                "D" = knots[1, 2] - 1
            )

            for (j in seq(2, 10)) {
                if (
                    abs(knots[1, 1] - knots[j, 1]) <= 1 &&
                        abs(knots[1, 2] - knots[j, 2]) <= 1 &&
                        abs(knots[1, 1] - knots[j, 1]) + abs(knots[1, 2] - knots[j, 2]) <= 2) {
                    next
                }

                if (knots[1, 1] == knots[j, 1]) {
                    tail <<- switch(split[1, ],
                        "U" = c(knots[j, 1], knots[j, 2] + 1),
                        "D" = c(knots[j, 1], knots[j, 2] - 1)
                    )
                } else if (knots[1, 2] == knots[j, 2]) {
                    tail <<- switch(split[1, ],
                        "R" = c(knots[j, 1] + 1, knots[j, 2]),
                        "L" = c(knots[j, 1] - 1, knots[j, 2])
                    )
                } else {
                    if (knots[1, 1] > knots[j, 1]) {
                        tail <<- c(knots[j, 1] + 1, knots[j, 2])
                    } else {
                        tail <<- c(knots[j, 1] - 1, knots[j, 2])
                    }

                    if (knots[1, 2] > knots[j, 2]) {
                        tail <<- c(knots[j, 1], knots[j, 2] + 1)
                    } else {
                        tail <<- c(knots[j, 1], knots[j, 2] - 1)
                    }
                }
            }

            tails <- knots[-1, ]
        }

        tails
    }) %>%
    unlist(recursive = FALSE)

tail_positions %>%
    unique() %>%
    length() %>%
    print()
