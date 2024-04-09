"""
This script creates sql code for the extid and datum sections of import_generation for the shell process scripts.
The column names of those extids and datums depend on the user input.
The extid # / datum # also depends on the user input.

Instructions:
Run python3 sql_generator.py and fill out the GUI depending on your needs.
Run with the VE: sql_generator
"""

import PySimpleGUI as GUI


GUI.theme('dark grey 10')

# Primary column layout.
first_column_layout = [

[GUI.Text(text='Extids:', font=('Calibri', 16), justification='center', size=(40, 1))],

[GUI.Text(text="PID column name:", font='Calibri'), GUI.Input(key='pid', font='Calibri', size=(22, 4), default_text='prov_id')],
[GUI.Text(text="NPI column name:", font='Calibri'), GUI.Input(key='npi', font='Calibri', size=(22, 4), default_text='npi_id')],
[GUI.Text(text="TIN column name:", font='Calibri'), GUI.Input(key='tin', font='Calibri', size=(22, 4), default_text='tin_id'),
GUI.Button(button_text='Clear', font=('Calibri'))],

[GUI.Text(text="   FACIL E extids:", font='Calibri'),
GUI.Input(key='fe_extid', font='Calibri', default_text='PID', size=(22, 4)),
GUI.Button(button_text='FACIL E', font='Calibri')],

[GUI.Text(text=" FACIL EL extids:", font='Calibri'),
GUI.Input(key='fel_extid', font='Calibri', default_text='PRS,NPI,TIN', size=(22, 4)),
GUI.Button(button_text='FACIL EL', font='Calibri')],

[GUI.Text(text="FACIL ELI extids:", font='Calibri'),
GUI.Input(key='feli_extid', font='Calibri', size=(22, 4)),
GUI.Button(button_text='FACIL ELI', font='Calibri')],


[GUI.Text(text="     PRO E extids:", font='Calibri'),
GUI.Input(key='pe_extid', font='Calibri', default_text='PID,NPI', size=(22, 4)),
GUI.Button(button_text='PRO E', font='Calibri')],

[GUI.Text(text="   PRO EL extids:", font='Calibri'),
GUI.Input(key='pel_extid', font='Calibri', default_text='PRS,TIN', size=(22, 4)),
GUI.Button(button_text='PRO EL', font='Calibri')],

[GUI.Text(text="  PRO ELI extids:", font='Calibri'),
GUI.Input(key='peli_extid', font='Calibri', size=(22, 4)),
GUI.Button(button_text='PRO ELI', font='Calibri')],

[GUI.Text(text='Datums:', font=('Calibri', 16), justification='center', size=(40, 1))],

[GUI.Text(text="ANP column name:", font='Calibri'), GUI.Input(key='anp', font='Calibri', size=(22, 4), default_text='ANP_column')],
[GUI.Text(text="PCP column name:", font='Calibri'), GUI.Input(key='pcp', font='Calibri', size=(22, 4), default_text='PCP_column')],
[GUI.Text(text="LOCEMAIL column:", font='Calibri'), GUI.Input(key='email', font='Calibri', size=(22, 4), default_text='email_column')],
[GUI.Text(text="  LOCURL column:", font='Calibri'), GUI.Input(key='url', font='Calibri', size=(22, 4), default_text='url_column')],

[GUI.Text(text="   FACIL E datums:", font='Calibri'), GUI.Input(key='fe_datum', font='Calibri', size=(22, 4), default_text='')],
[GUI.Text(text=" FACIL EL datums:", font='Calibri'), GUI.Input(key='fel_datum', font='Calibri', size=(22, 4), default_text='')],
[GUI.Text(text="FACIL ELI datums:", font='Calibri'), GUI.Input(key='feli_datum', font='Calibri', size=(22, 4), default_text='')],

[GUI.Text(text="     PRO E datums:", font='Calibri'), GUI.Input(key='pe_datum', font='Calibri', size=(22, 4), default_text='')],
[GUI.Text(text="   PRO EL datums:", font='Calibri'), GUI.Input(key='pel_datum', font='Calibri', size=(22, 4), default_text='')],
[GUI.Text(text="  PRO ELI datums:", font='Calibri'), GUI.Input(key='peli_datum', font='Calibri', size=(22, 4), default_text='ANP, PCP')],

[GUI.Button(button_text='Exit', font='Calibri')]]


# Secondary column layout for output.
second_column_layout = [
    [GUI.Text(text='Output:', font=('Calibri', 18), justification='center', size=(40, 2))],
    [GUI.Multiline(size=(50, 20), font=('Calibri', 14), key='-multi-line1-', do_not_clear=False, text_color='turquoise3')]
]

full_layout = [
    [GUI.Column(first_column_layout), GUI.Column(second_column_layout)]
]

# Create the window.
# Need finalize=True for the correct window size and when working with 2 windows.
window = GUI.Window('SQL Generator', layout=full_layout, margins=(10, 10), finalize=True)
window1 = window
#window2 = None

# Event loop.
while True:
    #event, values = window1.read()
    window, event, values = GUI.read_all_windows()

    # Check if user wants to quit or window was closed.
    if event in ('Exit', GUI.WIN_CLOSED):
        break
        #window.close()

    if event in ('Clear'):
        window['-multi-line1-'].print('')

    elif event in ['FACIL E', 'FACIL EL', 'FACIL ELI']:

        # Extids:
        pid_str = values['pid']
        npi_str = values['npi']
        tin_str = values['tin']

        current_extid_str = ''
        extid_word = ''

        if event == 'FACIL E':
            current_extid_str = values['fe_extid']
            extid_word = 'facil_'
        elif event == 'FACIL EL':
            current_extid_str = values['fel_extid']
            extid_word = 'facil_addr_'
        elif event == 'FACIL ELI':
            current_extid_str = values['feli_extid']
            extid_word = 'facil_addr_insp1_'

        # Always exists as a string, so this is not a none value.
        if len(current_extid_str) > 0:

            # Break out by comma delimited.
            str_list = current_extid_str.split(",")

            long_str = '/* EXTIDS */\n'

            for i in range(len(str_list)):

                current_num = i + 1
                current_column_name = ''
                cleaned_str = str_list[i].upper().strip()
                null_check_str = 'is not null'

                if cleaned_str == 'PID':
                    current_column_name = pid_str
                elif cleaned_str == 'NPI':
                    current_column_name = npi_str
                elif cleaned_str == 'TIN':
                    current_column_name = tin_str
                elif cleaned_str == 'PRS':
                    current_column_name = f"coalesce({npi_str}, {pid_str}, '')"
                    null_check_str = "<> ''"
                else:
                    print(f'No valid extid name found for: {str_list[i]}')

                long_str += f"case\n    when {current_column_name} {null_check_str} then '{cleaned_str}'\n"
                long_str += f"end as {extid_word}extid{current_num}_source_code,\n"

                long_str += f"case\n    when {current_column_name} {null_check_str} then {current_column_name}\n"
                long_str += f"end as {extid_word}extid{current_num}_value,\n"

                long_str += f"case\n    when {current_column_name} {null_check_str} then 'U'\n"
                long_str += f"end as {extid_word}extid{current_num}_record_status"

                if current_num != len(str_list):
                    long_str += ",\n"
                else:
                    long_str += "\n"

            window['-multi-line1-'].print(long_str)

        # Datums:
        anp_str = values['anp']
        pcp_str = values['pcp']
        loc_email_str = values['email']
        loc_url_str = values['url']

        current_datum_str = ''
        datum_word = ''

        if event == 'FACIL E':
            current_datum_str = values['fe_datum']
            datum_word = 'facil_'
        elif event == 'FACIL EL':
            current_datum_str = values['fel_datum']
            datum_word = 'facil_addr_'
        elif event == 'FACIL ELI':
            current_datum_str = values['feli_datum']
            datum_word = 'facil_addr_insp1_'

        #print(f'current datum str: {current_datum_str}')

        if len(current_datum_str) > 0:
            str_list = current_datum_str.split(",")
            long_str = '/* DATUMS */\n'

            for i in range(len(str_list)):

                current_num = i + 1
                current_column_name = ''
                cleaned_str = str_list[i].upper().strip()
                null_check_str = 'is not null'

                if cleaned_str == 'ANP':
                    current_column_name = anp_str
                    long_str += '-- Accepting New Patient datum:\n'
                elif cleaned_str == 'PCP':
                    current_column_name = pcp_str
                    long_str += '-- Patient Care Provider datum:\n'
                elif cleaned_str == 'LOCEMAIL':
                    current_column_name = loc_email_str
                    long_str += '-- Location Email datum:\n'
                elif cleaned_str == 'LOCURL':
                    current_column_name = loc_url_str
                    long_str += '-- Location URL datum:\n'
                else:
                    print(f'No valid datum name found for: {str_list[i]}')

                long_str += f"case\n    when {current_column_name} {null_check_str} then '{cleaned_str}'\n"
                long_str += f"end as {datum_word}datum{current_num}_type_code,\n"

                long_str += f"case\n    when {current_column_name} {null_check_str} then {current_column_name}\n"
                long_str += f"end as {datum_word}datum{current_num}_value,\n"

                long_str += f"case\n    when {current_column_name} {null_check_str} then 'U'\n"
                long_str += f"end as {datum_word}datum{current_num}_record_status"

                if current_num != len(str_list):
                    long_str += ",\n"
                else:
                    long_str += "\n"

            window['-multi-line1-'].print(long_str)

    elif event in ['PRO E', 'PRO EL', 'PRO ELI']:

        # Extids:
        pid_str = values['pid']
        npi_str = values['npi']
        tin_str = values['tin']

        current_extid_str = ''
        extid_word = ''

        if event == 'PRO E':
            current_extid_str = values['pe_extid']
        elif event == 'PRO EL':
            current_extid_str = values['pel_extid']
            extid_word = 'pra1_'
        elif event == 'PRO ELI':
            current_extid_str = values['peli_extid']
            extid_word = 'pra1_insp1_'


        if len(current_extid_str) > 0:

            str_list = current_extid_str.split(",")
            long_str = '/* EXTIDS */\n'

            for i in range(len(str_list)):

                current_num = i + 1
                current_column_name = ''
                cleaned_str = str_list[i].upper().strip()
                null_check_str = 'is not null'

                if cleaned_str == 'PID':
                    current_column_name = pid_str
                elif cleaned_str == 'NPI':
                    current_column_name = npi_str
                elif cleaned_str == 'TIN':
                    current_column_name = tin_str
                elif cleaned_str == 'PRS':
                    current_column_name = f"coalesce({npi_str}, {pid_str}, '')"
                    null_check_str = "<> ''"
                else:
                    print(f'No valid extid name found for: {str_list[i]}')

                long_str += f"case\n    when {current_column_name} {null_check_str} then '{cleaned_str}'\n"
                long_str += f"end as {extid_word}extid{current_num}_source_code,\n"

                long_str += f"case\n    when {current_column_name} {null_check_str} then {current_column_name}\n"
                long_str += f"end as {extid_word}extid{current_num}_value,\n"

                long_str += f"case\n    when {current_column_name} {null_check_str} then 'U'\n"
                long_str += f"end as {extid_word}extid{current_num}_record_status"

                if current_num != len(str_list):
                    long_str += ",\n"
                else:
                    long_str += "\n"

            window['-multi-line1-'].print(long_str)

        # Datums:
        anp_str = values['anp']
        pcp_str = values['pcp']
        loc_email_str = values['email']
        loc_url_str = values['url']

        current_datum_str = ''
        datum_word = ''

        if event == 'PRO E':
            current_datum_str = values['pe_datum']
        if event == 'PRO EL':
            current_datum_str = values['pel_datum']
            datum_word = 'pra1_'
        elif event == 'PRO ELI':
            current_datum_str = values['peli_datum']
            datum_word = 'pra1_insp1_'

        #print(f'current datum str: {current_datum_str}')

        if len(current_datum_str) > 0:
            str_list = current_datum_str.split(",")
            long_str = '/* DATUMS */\n'

            for i in range(len(str_list)):

                current_num = i + 1
                current_column_name = ''
                cleaned_str = str_list[i].upper().strip()
                null_check_str = 'is not null'

                if cleaned_str == 'ANP':
                    current_column_name = anp_str
                    long_str += '-- Accepting New Patient datum:\n'
                elif cleaned_str == 'PCP':
                    current_column_name = pcp_str
                    long_str += '-- Primary Care Provider datum:\n'
                elif cleaned_str == 'LOCEMAIL':
                    current_column_name = loc_email_str
                    long_str += '-- Location Email datum:\n'
                elif cleaned_str == 'LOCURL':
                    current_column_name = loc_url_str
                    long_str += '-- Location URL datum:\n'
                else:
                    print(f'No valid datum name found for: {str_list[i]}')

                long_str += f"case\n    when {current_column_name} {null_check_str} then '{cleaned_str}'\n"
                long_str += f"end as {datum_word}datum{current_num}_type_code,\n"

                long_str += f"case\n    when {current_column_name} {null_check_str} then {current_column_name}\n"
                long_str += f"end as {datum_word}datum{current_num}_value,\n"

                long_str += f"case\n    when {current_column_name} {null_check_str} then 'U'\n"
                long_str += f"end as {datum_word}datum{current_num}_record_status"

                if current_num != len(str_list):
                    long_str += ",\n"
                else:
                    long_str += "\n"

            window['-multi-line1-'].print(long_str)

window.close()
