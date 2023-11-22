import argparse
import datetime
import os
import sys
import requests

def set_key(key):
    """Acquire the API key that will be used to retrieve data from the NIST NVD

    Args:
        key (str):
            The key from the command line
                provided using either the '-k' or '--set-key' option

    Raises:
        KeyError: The API Key could not be found and was not provided by the user

    Returns:
        str: The API Key for accessing the NIST NVD API
    """
    try:
        if key:
            return key
        return os.environ['NIST_NVD']
    except KeyError:
        print('NIST NVD API key is not found. \
            Please either add a "NIST_NVD" environment variable or use the "-k"/"--set-key" option')
        sys.exit()


def send_to_user(cve, is_exported, file_path = None):
    """Either print or export the CVE(s) 

    Args:
        is_exported (bool): Whether the data acquired should be exported to a file. 
                                Data is printed to stdout if False.
        cve(List[str]): The list of CVEs found from the search
        file_path (str, optional): The file path to where the CVE values should be saved.
                                    Defaults to None.
    """
    # TODO: Complete send_to_user function
    # For now, we'll focus on just printing the CVE.
    # Additional CVEs and exporting to a file can be done at a later time
    print(cve)


def set_date(day):
    day.hour = 0
    day.minute = 0
    day.second = 0
    start_day = day
    end_day = day
    end_day.day = day.day + 1
    return [start_day, end_day]


def get_cve(key, day):
    base_url = 'https://services.nvd.nist.gov/rest/json/cves/2.0'
    time_span = set_date(day)
    payload = {'apiKey': key, 'lastModStartDate': time_span[0], 'lastModEndDate': time_span[0]}
    r = requests.get(base_url, params=payload)
    # TODO: double check contents of request, deal with problem if not 200
    return r
    

def main(parser):
    # TODO: Evaluate arguments and pass off responsibilities to functions
    args = parser.parse_args()
    api_key = set_key(args.get('key'))
    day_to_check = args.day if args.get('day') else datetime.now()
    cve = get_cve(api_key, day_to_check)
    send_to_user(cve, False)

if __name__ == "__main__":
    # TODO: Set up argparse and call main()
    parser = argparse.ArgumentParser(description='Select a random CVE from a chosen day')
    parser.add_argument('-k', '--set-key', dest='key', default=None)
    parser.add_argument('-d', '--set-date', dest = 'day', default=None)
    main(parser)
