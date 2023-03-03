import csv
import xmltodict

# open the input XML file and parse it into a dictionary
with open('ToParse.xml') as xml_file:
    data = xmltodict.parse(xml_file.read())

# open the output CSV file and write the header row
with open('output.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['id', 'acctnumber', 'TRANS_AM', 'TRANS_DT', 'COMMENT_TX', 'REFERENCE_NO_TX'])

    # loop through all LOAD_REQUEST elements in the XML file
    for request in data['XML_LOAD']['LOAD_REQUEST']:
        # extract the data we want from the XML and write it to the CSV
        writer.writerow([
            request['@id'],
            request['@acctnumber'],
            request['TRANSACTION']['TRANS_AM'],
            request['TRANSACTION']['TRANS_DT'],
            request['TRANSACTION']['COMMENT_TX'],
            request['TRANSACTION']['REFERENCE_NO_TX'],
        ])
