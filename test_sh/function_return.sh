#!/bin/bash

column="user_id"
code="A1234"
echo "column: ${column} code: ${code}\n"

get_column_code_string() {
    local column_name="$1"
    local code="$2"
    local alternate_value="${3:-}"

    local value=$column_name
    if [ ! -z "${alternate_value}" ]; then
        value=$alternate_value
    fi

    local result="Column: ${column_name}, Code: ${code} value: ${value} alternate_value: ${alternate_value}"
    
    echo "$result"
}

# function parameters: column_name, code, and an optional alternate_value.
returned_string=$(get_column_code_string "$column" "$code" "dog")
echo "Returned String: $returned_string"

fel_select="some_text_"
fel_select+=$(get_column_code_string "$column" "$code")
echo "fel_select: $fel_select"

echo "\ncolumn: ${column} code: ${code}"

# Shows how to take the output and store it in a file.
# echo "$fel_select" > file1.txt
