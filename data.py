try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

class Data(object):

    def __init__(self, url=None):
        self.url = url

    def set_url(self, url):
        self.url = url

    def get_data(self, to_file=False):
        response = urlopen(self.url)
        data = response.read().decode("utf-8")
        json_data = json.loads(data)

        if to_file:
            with open("outfile.json", "w") as outfile:
                out = json.dump(json_data, outfile, indent=4, sort_keys=True)
            return ""
        return json_data    

if __name__ == "__main__":
    govdata = Data("https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=planning-applications-since2010-test&facet=extractdate&facet=publisherlabel&facet=organisationlabel&facet=casereference&facet=casedate&facet=servicetypelabel&facet=classificationlabel&facet=casetext&facet=locationtext&facet=decisiontargetdate&facet=status&facet=coordinatereferencesystem&facet=decisiondate&facet=decision&facet=decisiontype&facet=decisionnoticedate&facet=geoarealabel&facet=groundarea&facet=agent")
    govdata.get_data(to_file=True)

    govdata = Data()
    govdata.set_url("https://opendata.bristol.gov.uk/api/records/1.0/search/?dataset=planning-applications-since2010-test&facet=extractdate&facet=publisherlabel&facet=organisationlabel&facet=casereference&facet=casedate&facet=servicetypelabel&facet=classificationlabel&facet=casetext&facet=locationtext&facet=decisiontargetdate&facet=status&facet=coordinatereferencesystem&facet=decisiondate&facet=decision&facet=decisiontype&facet=decisionnoticedate&facet=geoarealabel&facet=groundarea&facet=agent")
    print(govdata.get_data())