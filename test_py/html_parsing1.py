"""
This script shows how to take in an html parsed data-set,
search for a set of text using regular expressions,
then return that result.

This is a partially completed file, as this is a backup of an ad-hoc script ran.
"""

# Standard library imports
import argparse
import os
import csv
import re

# 3rd party imports
from bs4 import BeautifulSoup

# Local imports
from settings import logger

# List containing all jenkins jobs.
# Each item is a dictionary of details about that job.
feed_table = []


def is_useful_job(job_name: str) -> bool:
    """
    Checks whether a given job name is a useful job.
    """
    is_useful_name = True
    invalid_text = ['deprecate', 'test']

    for each_text in invalid_text:
        if each_text in job_name:
            is_useful_name = False
            break

    return is_useful_name


def do_disabled_results_exist(bs_data, search_str) -> bool:
    """
    Checks whether the results of a bs4 tag exists.
    """
    does_value_exist = False
    string_results = bs_data.find_all(search_str)

    if len(string_results) > 0:
        if len(string_results[0].contents) > 0:
            if string_results[0].contents[0] == 'true':
                does_value_exist = True

    return does_value_exist


def do_workon_results_exist(bs_data, search_str) -> bool:
    """
    Checks whether the results of a bs4 tag exists.
    """
    does_value_exist = False
    all_workon_results = []

    all_string_pos = [m.start() for m in re.finditer('workon', bs_data.text)]
    if len(all_string_pos) > 0:
        for i in range(len(all_string_pos)):
            temp_cut_str = bs_data.text[all_string_pos[i]:]
            final_temp_str = temp_cut_str.split('\n')[0]

            all_workon_results.append(final_temp_str)

    string_pos = bs_data.text.find('workon')
    final_str = ''
    if string_pos >= 0:
        cut_string = bs_data.text[string_pos:]
        final_str = cut_string.split('\n')[0]

    if len(all_workon_results) > 0:
        does_value_exist = True

    
    all_workon_results = list(dict.fromkeys(all_workon_results))
    str_full = ''.join(all_workon_results)

    return does_value_exist, str_full


def main(args):
    """
    Main procedure for scheduled run.
    """

    logger.main("Starting main procedure ...")

    main_folder = args.folder_path
    output_folder = args.output_path

    num_useful_folders = 0

    # Loop through all folders.
    for each_item in os.listdir(main_folder):
        full_item_path = os.path.join(main_folder, each_item)

        if os.path.isdir(full_item_path):

            if is_useful_job(each_item):

                logger.info(f"Current folder: {each_item}")
                num_useful_folders += 1

                for each_sub_item in os.listdir(full_item_path):

                    sub_item_path = os.path.join(full_item_path, each_sub_item)
                    if os.path.isfile(sub_item_path):

                        # Look at the config.xml file.
                        if each_sub_item == 'config.xml':

                            logger.debug(f"Current file: {each_sub_item}")

                            curr_dictionary = {}

                            # Grab job name and add it to dictionary.
                            curr_dictionary["jenkins_job_name"] = each_item

                            # Read config.xml file.
                            with open(sub_item_path, 'r') as f:
                                data = f.read()
                            bs_data = BeautifulSoup(data, 'xml')

                            # Check if it's a disabled job. If true, log that information.
                            disabled_str = "disabled"

                            disabled_results = do_disabled_results_exist(bs_data, disabled_str)
                            if disabled_results:
                                curr_dictionary["disabled_job"] = "True"
                            else:
                                curr_dictionary["disabled_job"] = "False"

                            workon_results, final_str = do_workon_results_exist(bs_data, "workon")
                            if workon_results:
                                curr_dictionary["workon"] = "True"
                                curr_dictionary["details"] = final_str
                            else:
                                curr_dictionary["workon"] = "False"
                                curr_dictionary["details"] = final_str

                            logger.info(f'{num_useful_folders} - {curr_dictionary}')

                            # Add dictionary to the list.
                            feed_table.append(curr_dictionary)

    logger.info(f"There are {num_useful_folders} total useful jobs")
    logger.debug(f"List results: {feed_table}")

    # keys is a tuple.
    keys = ('jenkins_job_name', 'disabled_job', 'workon', 'details')

    # Export list to a csv file called results.csv
    with open(f'{output_folder}/results.csv', 'w') as output_file:
        writer = csv.DictWriter(output_file, keys)
        writer.writeheader()
        writer.writerows(feed_table)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("-f", "--folder_path", type=str, help="enter folder path of jobs", required=True)
    parser.add_argument("-o", "--output_path", type=str, help="where to output the csv results", required=True)

    global_args = parser.parse_args()

    main(global_args)
