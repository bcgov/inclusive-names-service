### Test Datasets

The following files can be used in testing for Indigenous language support:

| Dataset | File/Folder Name | Source |
| ------------- | ------------- | ------------- |
| [Geographical Names (CSV)](./bcgnis_nonascii.csv)  | bcgnis_nonascii.csv | BCGW: [WHSE_BASEMAPPING.GNS_GEOGRAPHICAL_NAMES_SP](https://catalogue.data.gov.bc.ca/dataset/43805524-4add-4474-ad53-1a985930f352)  |
| [Ethno-Historic Sites (CSV)](./ethno_historic_sites.csv)  | ethno_historic_sites.csv | BCGW: [WHSE_HUMAN_CULTURAL_ECONOMIC.FN_ETH_HIST_RPT_SITES_POINT](https://catalogue.data.gov.bc.ca/dataset/43a7ae04-d4f9-40b3-8ddb-6724a01ffa02) <br> BCGW: [WHSE_HUMAN_CULTURAL_ECONOMIC.FN_ETH_HIST_RPT_SITES_POLY](https://catalogue.data.gov.bc.ca/dataset/c3768031-e90f-4ddb-891a-c7a8d8729f79) |
| [IR Band Names (CSV)](./ir_bands.csv)  | ir_bands.csv | BCGW: [WHSE_ADMIN_BOUNDARIES.ADM_INDIAN_RESERVES_BANDS_SP](https://catalogue.data.gov.bc.ca/dataset/c2ce81af-78c1-467c-b47e-c392cd0a771f)  |
| [IR Band Names (shapefile)](./ADM_INDIAN_RESERVES_BANDS_SP/)  | ADM_INDIAN_RESERVES_BANDS_SP/ | BCGW: [WHSE_ADMIN_BOUNDARIES.ADM_INDIAN_RESERVES_BANDS_SP](https://catalogue.data.gov.bc.ca/dataset/c2ce81af-78c1-467c-b47e-c392cd0a771f)  |
| [IR Band Names (DBF)](./ADM_INDIAN_RESERVES_BANDS_SP/DMNDNRSRVS_polygon.dbf)  | ADM_INDIAN_RESERVES_BANDS_SP/DMNDNRSRVS_polygon.dbf | BCGW: [WHSE_ADMIN_BOUNDARIES.ADM_INDIAN_RESERVES_BANDS_SP](https://catalogue.data.gov.bc.ca/dataset/c2ce81af-78c1-467c-b47e-c392cd0a771f)  |
| [Arts Agreements (CSV)](./fn_arts_agreements.csv)  | fn_arts_agreements.csv | BCGW: [WHSE_HUMAN_CULTURAL_ECONOMIC.FN_ARTS_AGREEMENTS_SP](https://catalogue.data.gov.bc.ca/dataset/3b229174-d5fe-42a1-8336-c6361d69cf53)  |
| [Community Locations (CSV)](./community_locations.csv)  | community_locations.csv) | BCGW: [WHSE_HUMAN_CULTURAL_ECONOMIC.FN_COMMUNITY_LOCATIONS_SP](https://catalogue.data.gov.bc.ca/dataset/c1a366fe-0212-48ba-a7f5-081036511794) |
| [FPCC Graphemes (CSV)](https://github.com/First-Peoples-Cultural-Council/fv-web-ui/blob/master/resources/graphemes.csv)  | graphemes.csv | [First Peoples Cultural Council](https://fpcc.ca/)  |
[FPCC Graphemes - Analyzed (CSV)](./grapheme_encoding_utf8.csv)  | grapheme_encoding_utf8.csv | Produced by a [python script](./process_graphemes_utf8.py)  
| [BC Sans characters (CSV)](./bcsans_version2.csv)  | bcsans_version2.csv | Unicode details for [BC Sans glyph set](https://www2.gov.bc.ca/assets/gov/british-columbians-our-governments/services-policies-for-government/policies-procedures-standards/web-content-development-guides/corporate-identity-assets/bcsans-glyphset-2023.pdf), produced by a [python script](./check_bc_sans.py) |

Note: BCGW stands for [BC Geographic Warehouse](https://www2.gov.bc.ca/gov/content?id=18B291A12B4F42EA98169892F4B46D61)
