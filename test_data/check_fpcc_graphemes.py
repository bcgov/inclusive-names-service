# purpose: read a list of potential broken links, produced by the FME script running on the PROD ETL FME server, and verify that they are actually broken.
# Any difference might be due to the firewall rules on the PROD ETL FME server.
 
# written by: mdwilkie

import requests
import argparse
import csv
import cx_Oracle
import getpass
from time import sleep


def verify_link(result_list,url,broken_or_suspicious,password):
    global record_counter

    connection = cx_Oracle.connect(user="WHSE_CORP", password=password,
                               dsn="bcgw.bcgov/idwprod1.bcgov",
                               encoding="UTF-8")
    cursor = connection.cursor()

    try:
        record_counter = record_counter + 1
        # test the URL -- use fake user-agent as described in https://www.pythonfixing.com/2022/01/fixed-aborted-remotedisconnected-end.html
        myheaders = {
"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
        resp = requests.head(url,timeout=10.0,headers=myheaders,allow_redirects=True)
        if resp.status_code == 200 or resp.status_code == 429:
            print(f"{broken_or_suspicious} link {url}: is reachable, status_code: {resp.status_code}")
            cursor.execute("""
                                delete from bcdc_broken_links_to_report where broken_link = :url
                           """,
                url=url)

            result_dict = dict(url=url,response=resp.status_code)
            result_list.append(result_dict)
            connection.commit()
        else:
            print(f"{broken_or_suspicious} link {url}: is Not reachable, status_code: {resp.status_code}")
            result_dict = dict(url=url,response=resp.status_code)
            result_list.append(result_dict)
    except requests.exceptions.RequestException as error:
        print(f"{broken_or_suspicious} link {url}: is Not reachable, Err: {error}")
        result_dict = dict(url=url,response='error')
        result_list.append(result_dict)
   
def get_urls_from_csv(results, input_csv):
    print( 'getting url list now') 

    input_list = []
    with open(input_csv, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            url_dict = {}
            for key in row.keys():
                url_dict[key] = row[key]
            line_count += 1
            input_list.append(url_dict)
        print( "Processed "+str(line_count)+' lines.')
    return input_list

def write_results_to_csv(result_list, result_csv):
    print( 'writing results') 

    with open(result_csv, mode='w', encoding = 'UTF8', newline='') as csv_file:
        fieldnames = ['url','response']
        csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        csv_writer.writeheader
        csv_writer.writerows(result_list)
    return

# ------ process -----
# iterate through array and patch package
if __name__ == "__main__":
    record_counter = 0
    argParser = argparse.ArgumentParser(description='Verifies if URLs in a list of URLs can be reached successfully')
    argParser.add_argument('-i', dest='urlcsv', action='store', default=None, required=True, help='a csv file containing the urls to verify')
    argParser.add_argument('-o', dest='resultcsv', action='store', default=None, required=True, help='a csv file containing the results')


    try:
        args = argParser.parse_args()
    except argparse.ArgumentError as e:
        argParser.print_help()
        sys.exit(1)

    print('Enter password for WHSE_CORP in IDWPROD1')
    password = getpass.getpass()

    input_csv = args.urlcsv
    result_csv = args.resultcsv
# process the csv file entries
    result_list = []
    input_list = get_urls_from_csv(result_list,input_csv)
   
    for url_dict in input_list:
        verify_link(result_list,url_dict["BROKEN_LINK"],url_dict["BROKEN_OR_SUSPICIOUS"],password)
        sleep(2)
    print(str(record_counter) + ' links checked')
    write_results_to_csv(result_list,result_csv)
