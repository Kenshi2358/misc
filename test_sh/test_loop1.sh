#!bin/bash

echo $SHELL

declare -A cat=( ["datum_type"]="cat_EXCLUDE" ["table"]="cat_npi_exclusion" )
declare -A dog=( ["datum_type"]="dog_EXCLUDE" ["table"]="dog_npi_exclusion" )
declare -a exclusions=("cat" "dog")

for exclusion_key in "${exclusions[@]}"; do

    declare -n ref="$exclusion_key"
    echo "Datum type: ${ref[datum_type]}"
    echo "Table: ${ref[table]}"

done
