# Person Name Data Standard

The Person Name Data Standard provides technical specifications on how to input, store, and display people’s names accurately and respectfully while considering the technology required for effective information exchange and usage. 

This directory contains tools that may be useful in implementing the Standard.

## PersonName Schema
The following [Unified Modeling Language (UML)](https://en.wikipedia.org/wiki/Unified_Modeling_Language) diagram illustrates the structure of a PersonName, and its relationship to a person:
![](images/PersonName_UML.jpg)

The diagram shows the five types of PersonName and the associated attributes of each. Any of these names can be shared by many persons (denoted by the “1..*” above the person box). In the other direction, an individual person has:
* Exactly one current (whole)legal name (“1..1”)
* Zero or one alternate spellings (limited legal) (“0..1”)
* Zero or more previous names (“0..*”)
* Zero or more aliases (“0..*”)
* Zero or one NameUsed names (“0..1”)

JSON Schemas provide a way of documenting the structure and constraints of data types, such as “PersonName”. Given a PersonName instance provided as JSON text, the JSON Schema for PersonName can be used to validate that instance. 

A JSON Schema for PersonName can be found [here](https://github.com/bcgov/inclusive-names-service/blob/main/docs/person_name_data_standard/person_name.json). 
Also provided are four sample PersonName JSON data files: [person_name_examples](https://github.com/bcgov/inclusive-names-service/blob/main/docs/person_name_data_standard/person_name_examples)
There are utilities available for validating a JSON data file against a JSON Schema file. On such utility can be found [here](https://www.jsonschemavalidator.net/).

## Person Name Splitting 
The Standard suggests, when practical, to provide and report person names in a single field, rather than splitting it into First/Middle/Last Name parts. There are, however, instances where person names may need to be split into parts in order to exchange data with legacy systems. In those cases, code such as the following can be used to do the splitting.

```

POLYNYM_PREFIXES = {
    "van", "von", "der", "de", "da", "di", "la", "le",
    "bin", "ibn", "al", "el"
}


def split_person_name(full_name: str):
    """
    Splits a full name according to rules aligned with the
    Person Name Data Standard.

    Behaviour:
     - Mononyms are placed in Last Name; First Name gets '.' if required.
    - Polynym-aware splitting for multi-word names.
    """

    full_name = full_name.strip()

    if not full_name:
        return "", "", ""

    parts = full_name.split()

    # Mononym case
    if len(parts) == 1:
        mononym = parts[0]

        # For systems that require First + Last:
        first = "."
        last = mononym
        return first, "", last

    # Two parts → first and last
    if len(parts) == 2:
        return parts[0], "", parts[1]

    # Polynym-aware splitting 
    last_parts = [parts[-1]]
    
    i = len(parts) - 2

    while i >= 0 and parts[i].lower() in POLYNYM_PREFIXES:
        last_parts.insert(0, parts[i])
        i -= 1

    first = parts[0]
    middle = " ".join(parts[1:i+1]) if i >= 1 else ""
    last = " ".join(last_parts)

    return first, middle, last
    
print(split_person_name('Sandra Lee Lenius'))
print(split_person_name('Ollie van der Heide'))
print(split_person_name('stáʔləw George'))
print(split_person_name('Mike'))
```

When run, the program will produce the following output:

('Sandra', 'Lee', 'Lenius')

('Ollie', '', 'van der Heide')

('stáʔləw', '', 'George')

('.', '', 'Mike')


