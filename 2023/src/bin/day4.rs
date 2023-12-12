use aoc::read_file_input;
use hashbrown::HashMap;

fn main() {
    let input = read_file_input("day4.in".to_string());

    let mut result = 0;
    let mut card_copies: HashMap<i32, i32> = HashMap::new();

    for line in input.lines() {
        let mut split_line = line.split(": ").collect::<Vec<&str>>();

        let card_number = split_line[0].split_whitespace().collect::<Vec<&str>>()[1]
            .parse::<i32>()
            .unwrap();
        if card_copies.contains_key(&card_number) {
            let card_copies_value = card_copies.get(&card_number).unwrap().clone();
            card_copies.insert(card_number, card_copies_value + 1);
        } else {
            card_copies.insert(card_number, 1);
        }

        split_line = split_line[1].split(" | ").collect::<Vec<&str>>();
        let winning_numbers = split_line[0].split_whitespace().collect::<Vec<&str>>();

        let mut card_result = 0;
        let mut matching_numbers = 0;
        for number in split_line[1].split_whitespace() {
            if winning_numbers.contains(&number) {
                matching_numbers += 1;
                if card_result == 0 {
                    card_result = 1;
                } else {
                    card_result *= 2;
                }
            }
        }

        result += card_result;

        let additional_card_copies_value = card_copies.get(&card_number).unwrap().clone();
        for card in card_number + 1..=card_number + matching_numbers {
            if card_copies.contains_key(&card) {
                let card_copies_value = card_copies.get(&card).unwrap().clone();
                card_copies.insert(card, card_copies_value + additional_card_copies_value);
            } else {
                card_copies.insert(card, additional_card_copies_value);
            }
        }
    }

    let mut result_two = 0;
    for (_card, copies) in card_copies {
        result_two += copies;
    }

    println!("Part I: {}", result);
    println!("Part II: {}", result_two);
}
