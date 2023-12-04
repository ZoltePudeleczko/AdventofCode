use aoc::read_file_input;

fn main() {
    let input = read_file_input("day2.in".to_string());

    let red = 12;
    let green = 13;
    let blue = 14;

    let mut result_one = 0;
    let mut result_two = 0;
    input.lines().for_each(|line| {
        let split_line = line.split(": ");

        let mut game_number = -1;
        let mut impossible = false;
        for a in split_line {
            if a.contains("Game") {
                game_number = a[5..].parse().unwrap();
                impossible = false;
                continue;
            } else {
                let sets = a.split("; ");
                let mut min_reds = -1;
                let mut min_greens = -1;
                let mut min_blues = -1;
                for set in sets {
                    let elements = set.split(", ");
                    for element in elements {
                        let number: i32 = element[..element.find(" ").unwrap()].parse().unwrap();

                        if element.contains("red") {
                            if number > red {
                                impossible = true;
                            }

                            if min_reds == -1 {
                                min_reds = number;
                            } else if number > min_reds {
                                min_reds = number;
                            }
                        } else if element.contains("green") {
                            if number > green {
                                impossible = true;
                            }

                            if min_greens == -1 {
                                min_greens = number;
                            } else if number > min_greens {
                                min_greens = number;
                            }
                        } else if element.contains("blue") {
                            if number > blue {
                                impossible = true;
                            }

                            if min_blues == -1 {
                                min_blues = number;
                            } else if number > min_blues {
                                min_blues = number;
                            }
                        } else {
                            if number > red + green + blue {
                                impossible = true;
                            }
                        }
                    }
                }

                result_two += min_reds * min_blues * min_greens;
            }

            if !impossible {
                result_one += game_number;
            }
        }
    });

    println!("Part I: {}", result_one);
    println!("Part II: {}", result_two);
}
