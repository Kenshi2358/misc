import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


def create_bar_graph(todays_jobs: list):

    import plotly
    import plotly.express as px

    # Add a count column as another key to todays_jobs list.
    for each_item in todays_jobs:
        each_item["count"] = 1

    internal_color_map = {
        "success": "#02a87c", "failure": "#EF553B", 
        "unknown": "#FFA15A", "running": "#636EFA", 
        "scheduled": "#19D3F3", "aborted": "#AB63FA"}

    fig = px.bar(
        todays_jobs, x="automation_time", y="count", color="last_run_status", 
        hover_name="job_name",
        color_discrete_map=internal_color_map, title="Bar Graph")
    fig.show()
    fig.write_image("fig1.png")

todays_jobs = ['job1', 'job2', 'job3']
create_bar_graph(todays_jobs)

# Attach image.
with open("fig1.png", 'rb') as img_file:
    img_data = MIMEImage(img_file.read())
    img_data.add_header("Content-ID", "<image1>")
    msg.attach(img_data)