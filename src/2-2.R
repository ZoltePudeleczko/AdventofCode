library(tidyr)
library(dplyr)

data.frame("data" = readLines("inputs/day2.txt")) %>%
    apply(1, function(x) {
        x <- data.frame(strsplit(x, " "))
        switch(x[1, ],
            "A" = switch(x[2, ],
                "X" = 3,
                "Y" = 1,
                "Z" = 2
            ),
            "B" = switch(x[2, ],
                "X" = 1,
                "Y" = 2,
                "Z" = 3
            ),
            "C" = switch(x[2, ],
                "X" = 2,
                "Y" = 3,
                "Z" = 1
            )
        ) + switch(x[2, ],
            "X" = 0,
            "Y" = 3,
            "Z" = 6
        )
    }) %>%
    sum() %>%
    print()
