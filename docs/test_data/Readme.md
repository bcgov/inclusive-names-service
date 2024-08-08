

The following files can be used in testing systems for Indigenous language support:

| Dataset | File/Folder Name | Source |
| ------------- | ------------- | ------------- |
| [Geographical Names (CSV)](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/bcgnis_nonascii.csv)  | bcgnis_nonascii.csv | BCGW: [WHSE_BASEMAPPING.GNS_GEOGRAPHICAL_NAMES_SP](https://catalogue.data.gov.bc.ca/dataset/43805524-4add-4474-ad53-1a985930f352)  |
| [Maskwacis Cree Syllabics (CSV)](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/maskwacis_cree.csv)  | maskwacis_cree.csv | [First Voices](https://www.firstvoices.com/maskwacis-cree/alphabet/startsWith?char=%E1%90%8A&types=phrase)
| [IR Band Names (CSV)](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/ir_bands.csv)  | ir_bands.csv | BCGW: [WHSE_ADMIN_BOUNDARIES.ADM_INDIAN_RESERVES_BANDS_SP](https://catalogue.data.gov.bc.ca/dataset/c2ce81af-78c1-467c-b47e-c392cd0a771f)  |
| [IR Band Names (shapefile)](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/ADM_INDIAN_RESERVES_BANDS_SP/)  | ADM_INDIAN_RESERVES_BANDS_SP/ | BCGW: [WHSE_ADMIN_BOUNDARIES.ADM_INDIAN_RESERVES_BANDS_SP](https://catalogue.data.gov.bc.ca/dataset/c2ce81af-78c1-467c-b47e-c392cd0a771f)  |
| [IR Band Names (DBF)](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/ADM_INDIAN_RESERVES_BANDS_SP/DMNDNRSRVS_polygon.dbf)  | ADM_INDIAN_RESERVES_BANDS_SP/DMNDNRSRVS_polygon.dbf | BCGW: [WHSE_ADMIN_BOUNDARIES.ADM_INDIAN_RESERVES_BANDS_SP](https://catalogue.data.gov.bc.ca/dataset/c2ce81af-78c1-467c-b47e-c392cd0a771f)  |
| [Arts Agreements (CSV)](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/fn_arts_agreements.csv)  | fn_arts_agreements.csv | BCGW: [WHSE_HUMAN_CULTURAL_ECONOMIC.FN_ARTS_AGREEMENTS_SP](https://catalogue.data.gov.bc.ca/dataset/3b229174-d5fe-42a1-8336-c6361d69cf53)  |
| [Community Locations (CSV)](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/community_locations.csv)  | community_locations.csv | BCGW: [WHSE_HUMAN_CULTURAL_ECONOMIC.FN_COMMUNITY_LOCATIONS_SP](https://catalogue.data.gov.bc.ca/dataset/c1a366fe-0212-48ba-a7f5-081036511794) |
| [FPCC Graphemes (CSV)](https://github.com/First-Peoples-Cultural-Council/unicode-resources/blob/main/resources/graphemes.csv)  | graphemes.csv | [First Peoples Cultural Council](https://fpcc.ca/)  |
[FPCC Graphemes - Analyzed (CSV)](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/fpcc_graphemes_encoded.csv)  | fpcc_graphemes_encoded.csv | Produced by a [python script](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/check_fpcc_graphemes.py)  
| [BC Sans characters (CSV)](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/check_bc_sans.csv)  | check_bc_sans.csv | Unicode details for [BC Sans glyph set](https://www2.gov.bc.ca/assets/gov/british-columbians-our-governments/services-policies-for-government/policies-procedures-standards/web-content-development-guides/corporate-identity-assets/bcsans-glyphset-2023.pdf), produced by a [python script](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/check_bc_sans.py) |

Note: BCGW stands for [BC Geographic Warehouse](https://www2.gov.bc.ca/gov/content?id=18B291A12B4F42EA98169892F4B46D61)

## Test Script
This folder also contains a file called [testApi.py](https://github.com/bcgov/inclusive-names-service/tree/main/docs/test_data/testApi.py) which can be used to quickly test an api, we recommend piping the output to a file for easy browsing ( `python3 test_dataApi.py ...params... > output.txt`)

    python3 test_data/testApi.py 

usage: 

    testApi.py [-h] -u URL -m METHOD -f USEFIELD -c CSV [-d ADDITIONALDATA] [-j JWT]

- `-u` the full url you want to test against ie http://127.0.0.1/api/myendpoint
- `-m` the method to use ie GET/POST/PUT/DELETE/HEAD/OPTIONS
- `-f` The field name to use ie name
- `-c` The path to the csv to use, this folder has some good ones
- `-d` (OPTIONAL) other data to send formatted as json ie '{"field1": "value1", "numberfield": 2}'
- `-j` (OPTIONAL) a jwt for jwt authenticated apis
