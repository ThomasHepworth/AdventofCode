use day_01::day1_sol;
use day_01::day_1_alternative_sol;
use std::fs;
use std::time::Instant;

fn main() {
    let input = "./input.txt";
    // let input = "./dummy_input.txt";

    let file = fs::read_to_string(input).unwrap();

    // Solution using a for loop
    let (part1, part2) = day1_sol(&file);
    println!("Solution to part 1 - original sol: {:?}", part1);
    println!("Solution to part 2 - original sol: {:?}", part2);

    // Solution using map
    let (part1, part2) = day_1_alternative_sol(&file);
    println!("Solution to part 1 - secondary sol: {:?}", part1);
    println!("Solution to part 2 - secondary sol: {:?}", part2);

    // Benchmark for day1_sol
    let mut total_duration = std::time::Duration::new(0, 0);
    for _ in 0..10000 {
        let start: Instant = Instant::now();
        let (_, _) = day1_sol(&file);
        let duration = start.elapsed();
        total_duration += duration;
    }
    println!("Average time for day1_sol: {} ms",
        total_duration.as_nanos() / 1000);

    // Benchmark for day_1_alternative_sol
    let mut total_duration = std::time::Duration::new(0, 0);
    for _ in 0..10000 {
        let start = Instant::now();
        let (_, _) = day_1_alternative_sol(&file);
        let duration = start.elapsed();
        total_duration += duration;
    }
    println!("Average time for day_1_alternative_sol: {} ms",
        total_duration.as_nanos() / 1000);
}
