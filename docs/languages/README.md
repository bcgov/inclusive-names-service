# Specifying Languages in Web Services

Modern web services (web pages and API's) are often designed for an international setting, and they attempt to respond to users according to certain settings specified by the user in requesting the web page or API response.

One such setting is the language, which can be specified as one or more *language codes* in the HTTP [Accept-language](https://http.dev/accept-language) request header or in an API query parameter, as described later on this page.

The responsibility of defining specific language codes sits with the [ISO/TC37](https://en.wikipedia.org/wiki/ISO/TC_37) standards committee. [ISO 639-3](https://iso639-3.sil.org/) defines 3-letter language codes for all the world's living languages. In this set, `eng` stands for English, `fra` for French, `deu` for German, etc.  [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) is a much simpler set, using 2-letter codes. ISO 639-1 is often used for major languages such as English (`en`) or French (`fr`). **For the purposes of the Accept-language header, ISO 639-1 is used where possible, with ISO 639-3 being used in cases where the language is not defined in ISO 639-1.**  

## Language codes for B.C. Indigenous languages

The following is a partial list of B.C. Indigenous languages and their corresponding ISO 639-3 language codes. 

|Language|Language Code|[First Voices](https://www.firstvoices.com/) Link|
|--------|-------------|-----------------|
|Hul'qumi'num (Halkomelem)| hur |https://www.firstvoices.com/halqemeylem |
|Nuu-chah-nulth (Nuu-chah-nulth, Nuuchahnulth)| nuk |https://www.firstvoices.com/nuu-chah-nulth-barkley |
|Sexqeltqin (Shuswap)|shs |https://www.firstvoices.com/secwepemc |

## Content Negotiation

Content Negotiation refers to the process of a user requesting a certain form of content (e.g., the language used in the response) and the service provider attempting to act on that request. In general there is no guarantee that the service provider can fulfill the request, so requests can take the form of a prioritized list of options (e.g., `nuk` as the first choice for `Accept-language` and `en` as the second choice).

## Specifying language preference to a service

When specifying a language preference in a message sent to a web service, the user can specify the value either as `Accpet-language` in the request  header or as a parameter along with the other query parameters. For web pages, which are requested by web browsers and served by web servers, `Accept-language` is specified in the request header. For API's, the language can be specified either in the message headers, as a query parameter. Since the API code has control over how to interpret the language specification, the name of the parameters does not need to be `Accept-language`. Often `lang=` or `language=` are used. 

### Request Header

When navigating to www.google.com in my Chrome browser and right-clicking `Inspect` I see the following line in the request headers:

![Accept-language setting from my browser](../images/header_accept_language.png)

These preferences are set in my Chrome browser `Language` settings:
* Top priority (Canadian English)
* Second priority (USA English)
* Third priority (generic English)

The `q=` values are [*Quality* values](https://developer.mozilla.org/en-US/docs/Glossary/Quality_values), indicating the weights (0-1) of my preferences.

### Query parameter

Here's an example of specifying Nuu-chah-nulth as the preferred language in an API call:
```
https://api.example.com/v1/endpoint?lang=nuk
```

## What does the service do with the language preference?

For web pages served by a web server, the type of response to an `Accept-language` request will depend on how the web server has been configured. For example, the web server may show a different version of a page depending on the requested language.

For a language specified to an API, code at the API endpoint may do the following:

* write the response using the requested language, and/or
* take actions appropriate to the customs of speakers of the requested language.

