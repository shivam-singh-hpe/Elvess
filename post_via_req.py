from datetime import datetime
import logging
import os
from urllib.parse import urljoin
import requests


def post_asup_to_nsdiag(serial_number, dmp_dir, dmp_file, dmp_type, url, **kwargs):
    """
    Function to post tar bundles to the nsdiag server.
    Only tar bundles are accepted by the server.

    :param serial_number: new array name
    :param dmp_dir: path of the dump file
    :param dmp_file: dump filename
    :param dmp_type: asup type i.e. daily or statsstream
    :param url: nsdiag url
    :param kwargs: curl max time and cert options
    """

    max_time = kwargs.get("max_time", 7200)
    cert = kwargs.get("cert", None)
    dmp_data = os.path.join(dmp_dir, dmp_file)
    dmp_size = str(os.path.getsize(dmp_data))
    job_id = "0"

    print(dmp_data)

    headers = {
        "Nsdiag-Serial": serial_number,
        "Nsdiag-Size": dmp_size,
        "Nsdiag-Name": dmp_file,
        "Nsdiag-Type": dmp_type,
        "Nsdiag-Jobid": job_id,
    }

    try:
        logging.info("Posting to server")
        res = requests.post(
            url,
            headers=headers,
            data=open(dmp_data, "rb").read(),
            timeout=max_time,
            cert=cert,
        )
    except Exception as e:
        logging.error(e)
        logging.info("Error on posting to NSdiag")
        print("failed")
    else:
        if res:
            print(res.status_code)
            print(res.content)
            logging.info("Successfully posted to NSdiag")
            print("Success")
        else:
            logging.info("Error on posting to NSdiag")
            print("failed")