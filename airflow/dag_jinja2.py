
# Standard library imports
# import os

# 3rd party imports
# from airflow.models import Variable
# from jinja2 import Environment, FileSystemLoader

# Local imports
# current_dir = os.getcwd()
# parent_dir = os.path.dirname(current_dir)
# report_dir = f'{parent_dir}/dags/templates/email/report'
# email_dir = f'{parent_dir}/dags/templates/email'

# Add relative path to the template directories.
# report_dir2 = os.path.join(os.path.dirname(__file__), 'templates/email/report')
# email_dir2 = os.path.join(os.path.dirname(__file__), 'templates/email')
# all_directories = [report_dir2, email_dir2]

    # logging.info(f"current_dir: {current_dir}")
    # logging.info(f"parent_dir: {parent_dir}")

    # logging.info(f"report_dir: {report_dir}")
    # logging.info(f"email_dir: {email_dir}")

    # des_noreply = Variable.get("des_noreply")
    # execution_date = default_args['start_date']

    # ----------------------------------
    # --------- Option 1 ---------------
    # Send data to Jinja template, render it, and return results.

    # email_template = 'templates/email/report/de_wh_report.html'

    # html_answered = render_template(
    #     email_template, tables=job_tables, stats=stats, **kwargs)

    # ----------------------------------
    # --------- Option 2 ---------------
    # Send data to Jinja template, render it, and return results.
    # template_environment = Environment(loader=FileSystemLoader(all_directories))

    # logging.info(f"Template directory: {template_environment.loader.searchpath}")

    # for each_template in template_environment.list_templates():
    #     logging.debug(f"Found template: {each_template}")

    # template1 = template_environment.get_template("de_wh_report.html")

    # var = {
    #     'json': None,
    #     'value': f'{des_noreply}'
    # }

    # html_answered = template1.render(
    #     tables=job_tables, stats=stats, execution_date=execution_date, var=var
    # )
    # ----------------------------------

    # for each_container in import_details:
    #     rowspan = sum(detail.get('tablename') == each_container['tablename'] for detail in import_details)
    #     rowspan = rowspan + 1 if rowspan != 1 else rowspan
    #     each_container['rowspan'] = rowspan


    # Add everything to kwargs.
    # kwargs_list = [
    #     table_server_style, td_server_css1, td_server_css2, table_counts_style,
    #     pre_timestamp, post_timestamp, td_header_counts_css1, td_header_counts_css2,
    #     td_counts_css1, td_counts_css2, params, report_results
    # ]
    # for each_item in kwargs_list:
    #     for variable_name, variable_value in list(globals().items()):
    #         if each_item == variable_value:
    #             kwargs[variable_name] = each_item