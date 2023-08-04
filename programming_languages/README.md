# inclusive-names-service
Repository of code and other information useful to software developers and system managers wishing to make systems capable of storing Unicode names of people, places, and businesses

[![Lifecycle:Experimental](https://img.shields.io/badge/Lifecycle-Experimental-339999)](<Redirect-URL>)

All examples use the utf8.txt file in this parent directory as the file they read from so you can make similar files or use/modify that one (basically one entry per line)

Currently has javascript/nodejs/python2/python3/go/c/c++/c#/java working examples, gotchas in each of the readmes. Databases to come

## Common Gotchas
This section is for common gotchas that are not language specific
- Even with using only UTF-8 it's even more important to parse user provided text as a SINGLE utf-8 character can be infinitely large as there is no limit to how many combining marks can be in one character

## Appendices
[Glossary](glossary.md)

[For Further Reading](references.md)