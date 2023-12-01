use aoc::read_file_input;

fn main() {
    let input = read_file_input("day1.in".to_string());

    let replaced = input
        .replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine");

    println!("Part I: {}", calibrate(&input));
    println!("Part II: {}", calibrate(&replaced));
}

fn calibrate(input: &str) -> i32 {
    let mut result = 0;
    for line in input.lines() {
        let mut first = -1;
        let mut last = -1;
        for character in line.chars() {
            if character.is_numeric() {
                if first == -1 {
                    first = character.to_digit(10).unwrap() as i32;
                    last = first;
                } else {
                    last = character.to_digit(10).unwrap() as i32;
                }
            }
        }

        result += first * 10 + last;
    }
    return result;
}
