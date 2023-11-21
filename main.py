import os
import requests
import argparse

def set_key(args):
    """Acquire the API key that will be used to retrieve data from the NIST NVD

    Args:
        args: A list of type [bool(, str)].
            The 0th element will be whether or not the user is providing the key from the command line
            using either the '-k' or '--set-key' option

    Raises:
        ValueError: The API Key could not be found and was not provided by the user

    Returns:
        str: The API Key for accessing the NIST NVD API
    """
    if args[0]:
        return args[1]
    elif not (nvd_key := os.environ("NIST_NVD")):
        raise ValueError("NIST NVD API key is not found. Please either add a 'NIST_NVD' environment variable or use the '--set-key' option")
    return nvd_key

def send_to_user(isExported, cve, file_path = None):
    """Either print or export the CVE(s) 

    Args:
        isExported (bool): Whether the data acquired should be exported to a file. Data is printed to stdout if False.
        cve(List[str]): The list of CVEs found from the search
        file_path (str, optional): The file path to where the CVE values should be saved. Defaults to None.
    """
    # TODO: Complete send_to_user function
    pass

def main():
    # TODO: Evaluate arguments and pass off responsibilities to functions
    pass

if __name__ == "__main__":
    # TODO: Set up argparse and call main()
    pass
