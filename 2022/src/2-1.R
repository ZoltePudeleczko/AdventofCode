library(tidyr)
library(dplyr)

data.frame("data" = readLines("inputs/day2.txt")) %>%
    apply(1, function(x) {
        x <- data.frame(strsplit(x, " "))
        switch(x[1, ],
            "A" = switch(x[2, ],
                "X" = 3,
                "Y" = 6,
                "Z" = 0
            ),
            "B" = switch(x[2, ],
                "X" = 0,
                "Y" = 3,
                "Z" = 6
            ),
            "C" = switch(x[2, ],
                "X" = 6,
                "Y" = 0,
                "Z" = 3
            )
        ) + switch(x[2, ],
            "X" = 1,
            "Y" = 2,
            "Z" = 3
        )
    }) %>%
    sum() %>%
    print()
