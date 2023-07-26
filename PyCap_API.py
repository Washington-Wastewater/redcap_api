import redcap

redcap_api_url = 'https://redcap.doh.wa.gov/api/'
# use your API token assigned in REDCap
redcap_token = "YOURTOKENHERE"

project = redcap.Project(redcap_api_url, redcap_token)

# This exports all fields, if you only want specific columns, you can also specify that here
samples_df = project.export_records(format_type = "df")

samples_df