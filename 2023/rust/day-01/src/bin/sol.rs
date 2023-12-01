use day_01::day1_sol;


fn main() {
    let input = "./input.txt";
    // let input = "./dummy_input.txt";
    let (sum_part1, sum_part2) = day1_sol(input);
    println!("Sum Part 1: {}", sum_part1);
    println!("Sum Part 2: {}", sum_part2);
}