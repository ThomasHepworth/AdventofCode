pub fn day1_sol(calories: &str) -> (i32, i32) {
    let calories: Vec<&str> = calories
        .split("\n\n")
        .collect();

        let mut totals: Vec<i32> = Vec::new();

    for c in &calories {

        let line_total: i32 = c.lines()
            .map(|x| x.parse::<i32>().unwrap())
            .fold(0, |acc: i32, x: i32| acc + x);

        totals.push(line_total);
    }

    totals.sort();
    let part2: i32 = totals.iter().skip(totals.len() - 3).sum();

    return (totals[totals.len()-1], part2);
}

pub fn day_1_alternative_sol(calories: &str) -> (i32, i32) {
    let mut totals: Vec<i32> = calories
        .split("\n\n")
        .map(|c: &str|
            c.lines()
            .map(|x| x.parse::<i32>().unwrap())
            .fold(0, |acc: i32, x: i32| acc + x)
        )
        .collect();

    totals.sort();
    let part2: i32 = totals.iter().skip(totals.len() - 3).sum();

    return (totals[totals.len()-1], part2);

}


#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "1000
2000
3000

4000A

5000
6000

7000
8000
9000

10000";

    #[test]
    fn it_works() {
        let (part1_sol, part2_sol) = day1_sol(INPUT);
        assert_eq!(part1_sol, 24000);
        assert_eq!(part2_sol, 45000);
    }

}