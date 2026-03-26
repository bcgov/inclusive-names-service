
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
