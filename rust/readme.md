# **Markdown Notes**

To view a markdown file in VS Code, press Shift + Cmd + V.

# **Rust Notes**

Rust is a statically typed language.
Rust is a compiled language, while Python is an interpeted language.

Clippy is a widely used linter in Rust and usually already comes installed.
To use it, navigate to the related directory and then type: `cargo clippy`

To run a check on your Rust program using Rust's built in linter, type: `cargo check`

Rust uses multi-line comments with /* */
Rust uses single line comments with //

The fn keyword defines a function.

There are 2 ways to run a rust program:
1) Compile the code by typing: `rustc main.rs`
Run the compiled code with: `./main`

2) run: `cargo run`

On a macOS, there is no .exe file extension like on Windows.
MacOS relies on the Unix-like convention where executables don't have any specific extension.

The ./ prefix specifies that the file is in the current directory.
The main() function is a predefined function that acts as an entry point to the program.

To check your versin of Rust, type: `rustc -V`
To check your version of Cargo, type: `cargo -V`
To update rust, type: `rustup update`

To create a new cargo package, type: `cargo new project_name`
Then compile and run with: `cargo run`

Rust packages tend to be more self-contained than pip with Python.

In Python, pip requires a requirements.txt file for the dependencies.
In Rust, cargo uses the Cargo.toml file for the dependencies. Cargo uses Lockfiles, while pip does not.

The toml file for each package is called it's manifest.

The root directory of your Rust project is your project name. In this case, its: hello_world
The Cargo.toml file is the heart of your project configuration.
The src/ directory contains your rust source code.
The main.rs file is the entry point of your executable.

The Cargo.lock file records the exact version of dependencies used in your project.
The target folder is the output location for compiled artifacts (binaries and libraries) produced by cargo.
Always ignore the target folder when working with a version control like Git.

The datatype: %str is a string literal.
Used when the value of a string is known at compile time.

The ! in println! denotes that this function is a macro.
It helps Rust distinguish between macros and regular functions.

To debug a rust program in VSCode on a macOS, you need to install the extension: CodeLLDB
Then in the launch.json file, specify:
"type": "lldb",
"request": "launch",
"program": "${workspaceFolder}/rust/hello_world/target/debug/hello_world",

If you ever want to rename a rust folder:
1) Rename the folder.
2) Update the Cargo.toml and cargo.lock package name to the new name.
3) Remove the target directory since it contains build artifacts and other temporary files.
Can do this with the "cargo clean" command.

4) Run "cargo build" command or cargo run.
