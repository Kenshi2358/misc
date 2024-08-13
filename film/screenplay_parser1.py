"""
This script takes in a text file of a screenplay script and analyzes it.
1) converts bad characters.
2) runs grammar checker.
3) runs general statistics.

"""
# Standard library
import argparse
import math

# 3rd party libaries
import language_tool_python


def convert_bad_characters(content) -> None:
    """Converts bad characters to good characters"""

    print("Converting bad characters")

    replace_dictionary = {
        "’": "'",
        '“': '"',
        '”': '"'
    }
    translation_table = str.maketrans(replace_dictionary)
    content = content.translate(translation_table)
    return content


def run_grammar_checker(content) -> int:
    """Returns the # of grammar errors"""

    print("Running grammar checker")

    # Initialize the tool
    tool = language_tool_python.LanguageTool('en-US')

    matches = tool.check(content)
    ignore_rules = ['MORFOLOGIK_RULE_EN_US', 'EN_UNPAIRED_QUOTES', 'DOUBLE_PUNCTUATION']

    num_matches = 0
    for each_match in matches:
        if each_match.ruleId not in ignore_rules:
            num_matches += 1

    print(f"Total # grammar errors: {num_matches}\n")

    for each_match in matches:
        if each_match.ruleId not in ignore_rules:
            output = f"""
            Error: {each_match.ruleId}
            Message: {each_match.message}
            Correction: {each_match.replacements}
            Context: {each_match.context}"""
            print(output)

    return num_matches


def create_containers(content):

    full_sentence_list = []

    # Split the text by carriage return.
    lines = content.split('\n')

    # Sentence enders.
    enders = ['.', '!', '?']

    temp_str = ''
    for each_line in lines:

        # Ender checks.
        found_ender = False
        smallest_ender = 99999999
        # smallest_char = ''

        for each_ender in enders:
            ender_pos = each_line.find(each_ender)
            if ender_pos >= 0:
                if ender_pos < smallest_ender:
                    smallest_ender = ender_pos
                    # smallest_char = each_ender
                    found_ender = True

        if found_ender:
            temp_sentence = temp_str + each_line[:smallest_ender+1]
            full_sentence_list.append(temp_sentence)
            temp_str = each_line[smallest_ender+1:]

        else:
            temp_str += each_line

    # sentence length container.
    full_container = {}

    for i, item in enumerate(full_sentence_list):

        current_item = item
        int_length = int(len(current_item))

        # if int_length == 6:
        #     print(f"Sentence {i}: {current_item}")
        #     pass

        if int_length in full_container:
            full_container[int_length]['sentence_count'] += 1
            full_container[int_length]['list'].append(current_item)

        else:
            full_container[int_length] = {}
            full_container[int_length]['sentence_count'] = 1
            full_container[int_length]['list'] = [current_item]

    # Sort the dictionary by key.
    sorted_container = dict(sorted(full_container.items()))

    return full_sentence_list, sorted_container


def run_stats(full_sentence_list: list, sorted_container: dict, num_errors: int):
    """Runs all statistics"""

    total_num_sentences = len(full_sentence_list)
    print('--- Stats ---')

    total_num_characters = 0
    for key1, value1 in sorted_container.items():
        total_num_characters += (int(key1) * value1['sentence_count'])

    avg_characters_per_sentence = round(total_num_characters / total_num_sentences, 1)

    total_word_count = 0
    for each_item in full_sentence_list:
        word_count = len(each_item.split(' '))
        total_word_count += word_count

    avg_word_count = round(total_word_count / total_num_sentences, 1)

    print(f'total sentences: {total_num_sentences:,} - avg characters per sentence: {avg_characters_per_sentence}')
    print(f'total word count: {total_word_count:,} - avg words per sentence: {avg_word_count}')
    print(f'total grammatical errors: {num_errors}')

    return total_word_count


def get_screenplay_time(content, total_word_count) -> None:
    """get the total amount of time to get through this screenplay."""

    average_speaking_rate = 150
    total_seconds = (total_word_count / average_speaking_rate) * 60

    mod_seconds = total_seconds % 60
    remaining_seconds = round(mod_seconds, 0)
    total_minutes = math.floor(total_seconds / 60)

    print(f"time: {total_minutes:}:{remaining_seconds:02.0f}")


def main(args):

    fname = args.fname

    # Open text file.
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Open PDF file - not working correctly.
    # from pypdf import PdfReader
    # reader = PdfReader(fname)
    # page = reader.pages[0]
    # content = ''
    # for each_page in reader.pages:
    #     content += each_page.extract_text()

    content = convert_bad_characters(content)

    num_errors = run_grammar_checker(content)

    full_sentence_list, sorted_container = create_containers(content)

    total_word_count = run_stats(full_sentence_list, sorted_container, num_errors)

    get_screenplay_time(content, total_word_count)


if __name__ == "__main__":
    """ Start Process"""

    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("-f", "--fname", type=str, required=True)

    global_args = parser.parse_args()

    main(global_args)
