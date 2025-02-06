#!/bin/bash

declare -A prov_array
prov_array["A"]="100"
prov_array["B"]="200"
prov_array["C"]="300"
prov_array["D"]="400"
prov_array["E"]="500"

import_str1=""

for ((i=1; i<=5; i++)); do

    # Add grouped "or" statement.
    if (( ${i} != 1 )); then
        import_str1+="or"
    fi

    # Add opening parantheses.
    import_str1+="("
    for each_key in "${!prov_array[@]}"; do
        each_value="${prov_array[$each_key]}"

        import_str1+="
        (field1_${i} = '${each_key}' and field2_${i} = '${each_value}') or"
    done

    # Remove last ' or' in string.
    import_str1="${import_str1% or}"

    # Add closing parentheses.
    import_str1+=")
    "

done

echo "${import_str1}"