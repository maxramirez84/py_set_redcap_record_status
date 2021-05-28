#!/usr/bin/env python
""" Python script to set the status variable of a bunch of records in a REDCap project."""
import pandas as pd
import redcap
import tokens

__author__ = "Maximo Ramirez Robles"
__copyright__ = "Copyright 2021, ISGlobal Maternal, Child and Reproductive Health"
__credits__ = ["Maximo Ramirez Robles"]
__license__ = "MIT"
__version__ = "0.0.1"
__date__ = "20210528"
__maintainer__ = "Maximo Ramirez Robles"
__email__ = "maximo.ramirez@isglobal.org"
__status__ = "Dev"

if __name__ == '__main__':
    # Connection parameters
    URL = tokens.URL
    PROJECTS = tokens.REDCAP_PROJECTS

    # Arguments
    ARG_PROJECT = "MOZ_CE_HS"
    ARG_RECORDS = range(27, 33)  # Records created during the training and uploaded to the prod project
    ARG_STATUS_FIELD = "profissionais_de_sade_complete"
    ARG_STATUS = 1  # Unverified
    ARG_COMMENTS_FIELD = "comments"  # For the TIPTOP HHS REDCap projects
    ARG_COMMENT = "Record created during the training and uploaded to the prod project. This is not real data!"

    project = redcap.Project(URL, PROJECTS[ARG_PROJECT])

    # Produce DataFrame with the list of records in which we want to modify the status
    record_num = len(ARG_RECORDS)
    data = {
        'record_id': ARG_RECORDS,
        ARG_COMMENTS_FIELD: [ARG_COMMENT] * record_num,
        ARG_STATUS_FIELD: [ARG_STATUS] * record_num
    }
    records = pd.DataFrame(data)

    pd.set_option('display.max_columns', None)
    print(records.head())

    # Import records with the modified status into the REDCap project
    print("Importing data to {}...".format(ARG_PROJECT))
    response = project.import_records(records, overwrite="overwrite")
    print(response)
