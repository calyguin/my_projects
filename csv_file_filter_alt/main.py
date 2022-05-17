# This is an alternative version of csv_file_filter
# This script is doing all the same job but without any communication with SQL
# I decided to refuse using this because of tremendous amount of resources and time this script consumes
# (My PC requires about 10 minutes to finish running this script)
# But even though this script is pretty bad, it is still capable of doing its job
# So here it is, an alternative option :)

import pandas as pd

# Naming columns
col_names = ['TUI',
             'PRICE',
             'DATE_OF_TRANSFER',
             'POSTCODE',
             'PROPERTY_TYPE',
             'OLD_OR_NEW',
             'DURATION',
             'PAON',
             'SAON',
             'STREET',
             'LOCALITY',
             'TOWN_OR_CITY',
             'DISTRICT',
             'COUNTY',
             'PPD_CATEGORY_TYPE',
             'RECORD_STATUS']

# Opening .csv file and applying column names to it
df = pd.read_csv('pp-complete.csv', names=col_names, skiprows=[1])

# Searching for duplicates and exporting them to a new .csv file
duplicates = df[df.duplicated(['PAON', 'SAON', 'STREET', 'LOCALITY', 'TOWN_OR_CITY', 'DISTRICT', 'COUNTY'], keep='last')]
df_out = pd.DataFrame(duplicates)
df_out.to_csv('pp-complete-duplicates.csv', header=False, index=False)