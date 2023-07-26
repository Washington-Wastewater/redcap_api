library(REDCapR)

# contains the credentials and path variables for redccap connection
redcap_url <- "https://redcap.doh.wa.gov/api/"

# redcap token
token <- "YOURTOKENHERE"

# get data from redcap
df_samples <- redcap_read_oneshot(redcap_uri=redcap_url, token=token)$data