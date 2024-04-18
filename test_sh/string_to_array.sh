#!/bin/bash

<< comments
Converts a string variable into an array in shell.
Additionally, checks that the array is not null.
Then loops through the array and runs each function name found.
The function name must exist somewhere else in the script.
comments

# Define the input string containing function names.
input="step_one,step_two,step_three"

# Convert the input string into an array.
IFS=',' read -ra function_array <<< "$input"

if [ -n "${#function_array[@]}" ]; then
    for func_name in "${function_array[@]}"; do
        "$func_name"
    done
fi
