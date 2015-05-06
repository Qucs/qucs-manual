


## Qucs manual

This is a demo/exploration for automatic generation of a component reference manual for Qucs.
It makes use of commands built in the Qucs comannd line interface to generate component icons and data.
A Python script transforms the generated data into a reStructured markup language.
The generated files are included into a Sphinx documentation generation project to create `html` and `pdf` outputs.


- Tested with:
  - Python 2.7.8
  - Sphinx 1.2.2
  - LaTex for pdf generation
  - OSX

## Preview (This might change at any time)

**New** with translations: http://guitorri.github.io/qucs-manual/


## How it works

Qucs executable has two commands:

- `$ qucs -icon`:

The command generates all the icons of the registered components as `.png` into the `./bitmaps_generated/` directory.

- `$ qucs -doc`

The command generares the following text files:

- `caterories.txt` containig the name of the caterories (same order as in Qucs)
  - `./[first category]/`
    - `01_data.csv` contains the data of the component object
    - `01_prop.csv` contains the properties of the component
    - ...


The document generation makes use of Sphinx and reStructured markup language.

Based on the above data obtained automatically the *Quick Reference* and *Component Reference* sections of the manual are automatically created.

The icons are copied into the `source` directory

    mkdir source/_static/bitmap
    qucs -icons
    cp ./bitmaps_generated/*.png source/_static/bitmap/

The component data files are also put into the `source` directory:

    mkdir source/component_data
    cd source/component_data
    qucs -doc

To auto-generate the above documentation files:

    cd source/component_data
    python build_component_doc.py

To generate the final `html` and `pdf` documentation:

    cd ../..
    make html
    make latexpdf

Outpus can be found in the `build/` directory.

## Translations

Most of *Quick Reference* and *Component Reference* translations can be retrieved from the Qucs TS files.

See scripts:

- `gen_update.sh` : to update the Sphinx PO files
- `gen_ts2po.py` : to copy translations from Qucs TS to Sphinx PO files
- `gen_html.sh`	: generate the HTML pages



