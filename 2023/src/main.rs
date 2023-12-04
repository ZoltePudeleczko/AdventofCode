use std::process::Command;

fn main() {
    for day in 1..=2 {
        let day = format!("day{day}");
        let cmd = Command::new("cargo")
            .args(["run", "--release", "--bin", &day])
            .output()
            .unwrap();

        println!("----------");
        println!("| {} |", day);
        println!("----------");

        let output = String::from_utf8(cmd.stdout).unwrap();
        println!("{}", output.trim());
    }
}
