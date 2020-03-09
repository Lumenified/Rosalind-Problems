#without an external library
import re
import urllib.request

def three_to_one_online(three_letter_code):
    url = "http://www.ebi.ac.uk/pdbe-srv/pdbechem/chemicalCompound/show/" + three_letter_code
    with urllib.request.urlopen(url) as response:
        single_letter_code = re.search('\s*<td\s*>\s*<h3>One-letter code.*</h3>\s*</td>\s*<td>\s*([A-Z])\s*</td>', response.read().decode('utf-8')).group(1)
    return single_letter_code
