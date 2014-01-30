gapmasker
=========

Masks gaps from simulated alignments according to a template

Installation
------------

Installation is by 

    git clone https://github.com/kgori/gapmasker gapmasker
    cd gapmasker
    python setup.py install

or

    pip install git+https://github.com/kgori/gapmasker

This places ```gapmasker``` into the PATH

Usage
-----

Give gapmasker a template alignment, an alignment to mask, a file format and an optional output file

    gapmasker -t TEMPLATE -i TARGET -f FORMAT (=fasta or phylip) [-o OUTPUT]
  
```gapmasker -h``` displays help 


Example
-------

There's an example in the test directory
    
    cd test
    gapmasker -t template.fas -i target.fas
    
    >one
    xxxxx---xxx
    >two
    xxxxxxxxxxx
    >three
    xx--xxxxxxx
    >four
    xxxxxxxxxxx
