#!/bin/sh

# Helper script to generate HTML documentation

# generate localized html documentation
# include 'en', for the sake of consistency
languages=(
  ar
  ca
  cs
  de
  en
  es
  fr
  he
  hu
  it
  jp
  kk
  pl
  pt_BR
  pt_PT
  ro
  ru
  sv
  tr
  uk
  )


# compile
sphinx-intl -c source/conf.py build -d source/locale

#prefix='/Users/guitorri/git/qucs-help.github.io'
prefix='build'

for lang in ${languages[*]}
do
    printf "  %s\n" $dir
    cmd="sphinx-build -a -b html -d build/doctrees/ -D language=$lang source $prefix/html-$lang"
    echo $cmd
    $cmd

done

