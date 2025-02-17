"""Extract data on near-Earth objects.

and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided
at the command line, and uses the resulting collections
to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
from re import A

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path:
    A path to a CSV file containing data about near-Earth objects.
    :return:
    A collection of `NearEarthObject`s.
    """
    # initializing a neo collection list

    neo_collection = []

    with open(neo_csv_path) as neo_file:
        all_neos = csv.DictReader(neo_file)
        for each_neo in all_neos:
            neo_collection.append(NearEarthObject(**each_neo))
    return neo_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path:
    A path to a JSON file containing data about close approaches.
    :return:
    A collection of `CloseApproach`es.
    """
    # initializing a close approach list

    approach_collection = []

    with open(cad_json_path) as approach_file:
        all_approaches = json.load(approach_file)
        headers = all_approaches['fields']
        counts = int(all_approaches['count'])
        detail = all_approaches['data']

        for count in range(counts):
            approach_dict = {}
            for each in range(11):
                approach_dict[headers[each]] = detail[count][each]
            # print(approach_dict)
            approach_collection.append(CloseApproach(**approach_dict))

    # print(approach_collection)
    return approach_collection
