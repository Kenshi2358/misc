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

select1="First step"
select2="Second step"
select3="Third step"
select4="Fourth step"
select5="Fifth step"

declare -A associative_array=(
    ["Step1"]="$select1"
    ["Step2"]="$select2"
    ["Step3"]="$select3"
    ["Step4"]="$select4"
    ["Step5"]="$select5"
)

# Looped check.
for key in "${indexed_array[@]}"; do
    echo "${key}"
done

# Looped check.
for result in "${associative_array[@]}"; do
    echo "${result}"
done

# Individual check.
#echo "${associative_array["Step1"]}"
#echo "${associative_array["Step2"]}"