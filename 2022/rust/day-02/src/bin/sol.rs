use day_02::day2_sol;
use std::fs;

fn main() {
    let input = "./input.txt";
    // let input = "./input_dummy.txt";

    let file = fs::read_to_string(input).unwrap();

    let (part1, part2) = day2_sol(&file);
    println!("{part1}");
    println!("{part2}");
}
