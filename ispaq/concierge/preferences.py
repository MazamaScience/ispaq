"""
ISPAQ Preferences Loader and Container.

:copyright:
    Mazama Science
:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lesser.html)
"""
import json
import ispaq.utils.preferences as preferences

from obspy import UTCDateTime


# Dummy UserRequest object
class DummyUserRequest(object):
    def __init__(self):
        """
        Creates a dummy UserRequest object with sufficient properties for testing.

        .. rubric:: Example

        >>> my_request =  DummyUserRequest()
        >>> my_request.sncl_patterns
        ['US.OXF..*']
        """
        self.starttime = UTCDateTime("2002-04-20")
        self.endtime = UTCDateTime("2002-04-21")
        self.event_url = "IRIS"
        self.station_url = "IRIS"
        self.dataselect_url = "IRIS"
        self.metric_names = ["num_gaps"]  # TODO:  to be removed
        self.sncl_patterns = ["US.OXF..*"]
        self.metric_dictionary = {'simple': {'basicStats': ['sample_min','sample_max'],
                                             'gaps': ['num_gaps']} }
        # More to be added as needed


# Real UserRequest object
class UserRequest(object):
    def __init__(self, requested_start_time, requested_end_time, requested_metric_set, requested_sncl_alias, pref_file,
                 json_user_request=None):
        """
        Creates a UserRequest object.

        .. rubric:: Example

        TODO:  Generate doctest examples by loading from json.
        """

        #     Load json data if requested     ---------------------------------

        if json_user_request is not None:
            # Load json dictionary from file (or string)
            # TODO:  Test whether the `json` argument is a file or a string and
            # TODO:  use json.load() or json.loads() accordingly

            # Create new 'args' object
            # TODO:
            print("'json'_file argument not supported yet.")

        #     Assign basic internal properties     ----------------------------

        # times
        self.starttime = UTCDateTime(requested_start_time)
        if requested_end_time is None:
            self.endtime = self.starttime + 24 * 3600
        else:
            self.endtime = UTCDateTime(requested_end_time)

        # TODO:  remove these when preferences get loaded
        self.event_url = "IRIS"
        self.station_url = "IRIS"
        self.dataselect_url = "IRIS"

        # More to be added as needed

        #     Load preferences from file     ----------------------------------

        self.custom_metric_sets, self.sncl_aliases = preferences.load(pref_file)

        #     Create metric_dictionary     ------------------------------------

        # NOTE:  metric_sets are defined in irismustangmetrics/metrics.py but will
        # NOTE:  ultimately come from the R package. Current sets include:
        # NOTE:  basicStats, gaps, spikes, stateOfHealth and STALTA (slow).

        # TODO:  After loading the preferences file, we need to load the
        # TODO:  dictionary of function meatadata organized as:
        # TODO:    metric_set > logic_type > metric name
        # TODO:
        # TODO:  We need to winnow this dictionary to omit any metrics
        # TODO:  who do not have any metrics namded in self.metric_names.
        # TODO:
        # TODO:  Finally, we restructure into another dictionary organized as:
        # TODO:    logic_type > metric_set > metric_name

    def json_dump(self):
        """
        Dump a dictionary of UserRequest properties as a json string
        
        # TODO:  If a file argument is given, dump to a file with json.dump.
        # TODO:  Otherwise, return the json string.
        """

        properties_dict = {}
        
        # TODO:  Fill in properties_dict with all properties, converting from
        # TODO:  UTCDateTime with str(self.starttime) and str(self.endtime).
        
        properties_json = json.dumps(properties_dict)
        
        return properties_json
        

if __name__ == '__main__':
    import doctest
    doctest.testmod(exclude_empty=True)

