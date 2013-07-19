mdconv
======

self-used tool for converting markdown to html

can be used in two ways 
 - `mdconv.py` to convert everything ending in `.md` in current directory
 - `mdconv.py file.md ...` to convert selected files (wildcards may or may not work)

the script will look for `.mdc_header` and `.mdc_footer` for preluding and concluding wrappers for the conversion. they are *not* parsed.

this script uses python package `markdown` and all limitations of that package exist here.
