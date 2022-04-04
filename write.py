"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from datetime import datetime, date


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`.
    Roughly, each output row corresponds to the information
    in a single close approach from the `results` stream and
    its associated near-Earth object.

    :param results:
    An iterable of `CloseApproach` objects.
    :param filename:
    A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    # TODO: Write the results to a CSV file,
    # following the specification in the instructions.

    with open(filename, "w", newline="") as outfile:
        # print(outfile)
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        if results:
            for result in results:
                result_dict = {}
                result_dict['datetime_utc'] = result.time
                result_dict['distance_au'] = result.distance
                result_dict['velocity_km_s'] = result.velocity
                result_dict['designation'] = result._designation
                if result.neo.name is not None:
                    result_dict['name'] = result.neo.name
                else:
                    result_dict['name'] = ""
                if result.neo.diameter:
                    result_dict['diameter_km'] = result.neo.diameter
                else:
                    result_dict['diameter_km'] = ""
                if result.neo.hazardous:
                    result_dict['potentially_hazardous'] = "True"
                else:
                    result_dict['potentially_hazardous'] = "False"

                # print (result_dict['datetime_utc'])
                writer.writerow(result_dict)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`.
    Roughly, the output is a list containing dictionaries,
    each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to
    where the data should be saved.
    """
    # TODO: Write the results to a JSON file,
    # following the specification in the instructions.

    data = []
    for result in results:
        result_dict = {}
        result_dict['datetime_utc'] = result.time
        result_dict['distance_au'] = result.distance
        result_dict['velocity_km_s'] = result.velocity
        result_dict['neo'] = {}
        result_dict["neo"]['designation'] = result.neo.designation
        if result.neo.name is not None:
            result_dict["neo"]['name'] = result.neo.name
        else:
            result_dict["neo"]['name'] = ""
        if result.neo.diameter:
            result_dict["neo"]['diameter_km'] = result.neo.diameter
        else:
            result_dict["neo"]['diameter_km'] = ""

        result_dict["neo"]['potentially_hazardous'] = result.neo.hazardous

        data.append(result_dict)

    class ComplexEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.strftime('%Y-%m-%d %H:%M')
            else:
                return json.JSONEncoder.default(self, obj)

    with open(filename, "w") as outfile:
        json.dump(data, outfile, cls=ComplexEncoder)
