"""
This script takes in a screenplay script and analyzes many aspects of the text.
1st analysis - sentence length.
"""

import argparse

def main(args):

    fname = args.fname

    full_sentence_list = []

    # Open text file.
    with open(fname, 'r') as f:
        content = f.read()

    # Split the text by carriage return.
    lines = content.split('\n')

    # Sentence enders.
    enders = ['.', '!', '?']

    temp_str = ''
    for each_line in lines:

        # Ender checks.
        found_ender = False
        smallest_ender = 99999999
        smallest_char = ''

        for each_ender in enders:
            ender_pos = each_line.find(each_ender)
            if ender_pos >= 0:
                if ender_pos < smallest_ender:
                    smallest_ender = ender_pos
                    smallest_char = each_ender
                    found_ender = True

        if found_ender == True:
                
            temp_sentence = temp_str + each_line[:smallest_ender+1]
            full_sentence_list.append(temp_sentence)
            temp_str = each_line[smallest_ender+1:]

        else:
            temp_str += each_line

    # sentence length container
    full_container = {}

    for i, item in enumerate(full_sentence_list):

        current_item = item
        int_length = int(len(current_item))

        if int_length == 6:
            print(f"Sentence {i}: {current_item}")
            pass

        if int_length in full_container:
            full_container[int_length]['count'] += 1
            full_container[int_length]['list'].append(current_item)

        else:
            full_container[int_length] = {}
            full_container[int_length]['count'] = 1
            full_container[int_length]['list'] = [current_item]

    # Sort the dictionary by key.
    sorted_container = dict(sorted(full_container.items()))

    # print(sorted_container)
    pass


if __name__ == "__main__":
    """ Start Process"""

    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("-f", "--fname", type=str, required=True)

    global_args = parser.parse_args()

    main(global_args)
