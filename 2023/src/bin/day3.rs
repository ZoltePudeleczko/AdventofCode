use aoc::read_file_input;
use hashbrown::HashMap;

fn main() {
    let input = read_file_input("day3.in".to_string());

    let mut symbols: Vec<(usize, usize)> = Vec::new();
    let mut numbers: HashMap<(usize, usize), i32> = HashMap::new();

    for (i, line) in input.lines().enumerate() {
        for (j, character) in line.chars().enumerate() {
            if !character.is_numeric() && character != '.' {
                symbols.push((i, j));
            }
        }
    }

    let mut sum = 0;

    let mut is_adjacent = false;
    let mut number = 0;
    let mut lenght = 0;
    for (i, line) in input.lines().enumerate() {
        for (j, character) in line.chars().enumerate() {
            if character.is_numeric() {
                number = number * 10 + character.to_digit(10).unwrap() as i32;
                lenght += 1;

                if !is_adjacent {
                    is_adjacent = check_symbol_is_adjacent((i, j), &symbols)
                }
            } else if number > 0 {
                if is_adjacent {
                    sum += number;

                    for go_back in 0..lenght {
                        numbers.insert((i, j - 1 - go_back), number);
                    }
                }

                is_adjacent = false;
                number = 0;
                lenght = 0;
            }
        }

        if number > 0 {
            if is_adjacent {
                sum += number;

                for go_back in 0..lenght {
                    numbers.insert((i, line.len() - 1 - go_back), number);
                }
            }

            is_adjacent = false;
            number = 0;
            lenght = 0;
        }
    }

    let mut sum2 = 0;

    for (i, line) in input.lines().enumerate() {
        for (j, character) in line.chars().enumerate() {
            if character == '*' {
                sum2 += check_two_numbers_are_adjacent((i, j), &numbers);
            }
        }
    }

    println!("Part I: {}", sum);
    println!("Part II: {}", sum2);
}

fn check_symbol_is_adjacent(coordinates: (usize, usize), symbols: &Vec<(usize, usize)>) -> bool {
    let options = [
        (coordinates.0 - 1, coordinates.1 - 1),
        (coordinates.0 - 1, coordinates.1),
        (coordinates.0 - 1, coordinates.1 + 1),
        (coordinates.0, coordinates.1 - 1),
        (coordinates.0, coordinates.1 + 1),
        (coordinates.0 + 1, coordinates.1 - 1),
        (coordinates.0 + 1, coordinates.1),
        (coordinates.0 + 1, coordinates.1 + 1),
    ];

    for option in options.iter() {
        if symbols.contains(option) {
            return true;
        }
    }
    return false;
}

fn check_two_numbers_are_adjacent(
    coordinates: (usize, usize),
    numbers: &HashMap<(usize, usize), i32>,
) -> i32 {
    let options = [
        (coordinates.0 - 1, coordinates.1 - 1),
        (coordinates.0 - 1, coordinates.1),
        (coordinates.0 - 1, coordinates.1 + 1),
        (coordinates.0, coordinates.1 - 1),
        (coordinates.0, coordinates.1 + 1),
        (coordinates.0 + 1, coordinates.1 - 1),
        (coordinates.0 + 1, coordinates.1),
        (coordinates.0 + 1, coordinates.1 + 1),
    ];

    let mut first_number = -1;
    let mut second_number = -1;
    for option in options.iter() {
        if numbers.contains_key(option) {
            let number = numbers.get(option).unwrap().clone();
            if first_number == -1 {
                first_number = numbers.get(option).unwrap().clone();
            } else if number != first_number {
                second_number = numbers.get(option).unwrap().clone();
            }
        }
    }

    if first_number != -1 && second_number != -1 {
        return first_number * second_number;
    }
    return 0;
}
