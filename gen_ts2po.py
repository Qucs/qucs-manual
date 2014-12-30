
import polib
import glob
from subprocess import Popen, PIPE, call
import os

'''
This script copies the translated strings from
the Qucs TS files to the Sphinx PO files.

Set the ts_dir to the Qucs repo clone.

Dependencies:
- polib
- lconvert (Qt SDK)

'''

# source TS files location
# TODO nice argument parser
ts_dir = "/Users/guitorri/git/qucs/qucs/translations/"

# ge list of Sphinx languages that need attention
languages = os.listdir("source/locale/")

# convert TS to PO, need lconvert (from Qt)
# get TS from Qucs repo clone
# save PO locally TODO use a temp dir
for lang in languages:
    ts_file = "%s/qucs_%s.ts" %(ts_dir, lang)
    po_file = "build/qucs_%s.po" %(lang)
    cmd = "lconvert %s -o %s" %(ts_file, po_file)
    print cmd
    p = Popen(cmd.split(" "), stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    if p.returncode != 0:
        print stderr
        print stdout

# copy translations from TS->PO to Sphinx->PO
for lang in languages:
    print lang

    # grab sphinx PO files by language, ex:
    #  ./source/locale/pt_BR/LC_MESSAGES/component_reference.po
    #  ./source/locale/pt_BR/LC_MESSAGES/quick_reference.po
    locale = glob.glob("./source/locale/%s/*/*_reference.po" %(lang))
    for sx_file in locale:
        A = "build/qucs_%s.po" %(lang)
        B = sx_file

        print 'source: ', A
        print 'target: ', B

        ts = polib.pofile(A)
        sx = polib.pofile(B)

        # look for tranlations in TS files
        for sphinx in sx.untranslated_entries():
            for source in ts.translated_entries():
                if sphinx.msgid == source.msgid:
                    # pick translation from TS
                    sphinx.msgstr = source.msgstr

        # overwrite
        print 'saving: ', B
        print
        sx.save( B )


