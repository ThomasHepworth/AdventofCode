## Creating a New Day

### Python

```bash
source create_day/advent_of_code_day_py.sh -y {year} -d {day}
```

Replace `{year}` and `{day}` with the appropriate values for the challenge year and day. This script will create a new folder structure under `{year}/python/day-{day}` and will include the following files: `sol.py`, `input.txt`, and `dummy_input.txt`.

### Rust

```bash
source create_day/advent_of_code_day_rust.sh -y {year} -d {day}
```

Replace `{year}` and `{day}` with the appropriate values for the challenge year and day. This script will create a new Rust project using `cargo new --lib` and will generate `input.txt` and `dummy_input.txt` files, along with a `sol.rs` file for your solution.
