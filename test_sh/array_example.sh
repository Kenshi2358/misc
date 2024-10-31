#!/bin/bash
<< comments
Example of looping through an associative array, with order preserved.
It's preserved due to looping through the indexed array.
Looping through an associative array does not preserve order.

This code is kept separately because it's
only marginally better then manually writing out the steps.
comments

declare -a indexed_array=(
    "Step1" "Step2"
    "Step3" "Step4" "Step5"
)

declare -A associative_array=(
    ["Step1"]="$select1"
    ["Step2"]="$select2"
    ["Step3"]="$select3"
    ["Step4"]="$select4"
    ["Step5"]="$select5"
)

for key in "${indexed_array[@]}"; do
    echo "${key}"
    ${pgcon} -c "${associative_array[${key}]}"
done