------------------------------------------------------------------------------------------------------------------------------------------
# PART 1  - PERCEPTRON  IMPLEMENTATION #

### perceplearn.py ###

To create model file after learning from training data

* Achievers **30 iterations** of learning, or ** accuracy > .99** which ever happens first.

### percepclassify.py ###

Clasifies a single line of input, from STDIN and writes class in STDOUT.

* Classifies **one-line-at-a-time** only

### File formats... ###

1. training_file 

```
#!python

CLASS1 FEATURE11 FEATURE12 ...
.
.
CLASSR FEATURER1 FEATURER2 ...

```
## Instructions on use ##
*All scripts print usage instructions on wrong invoke*

1. Learn from training file and generate model


```
#!python

./perceplearn.py <training_file> <model_file>
```
2. classify single line of text from STDIN and write class to STDOUT

```
#!python

./percepclassify <model_file_name>  <  test_file
```
or

```
#!python

./percelclassify <model_file_name>  
#your test input here for STDIN#
```

----------------------------------------------------------------------------------------------------------------------------
# POS tagging #

## Files ##

### postraing.py ###

Uses **perceplearn.py** to create model file from part of speech training data

### postag.py ###

Takes n lines given from STDIN and writes consequetive n tagged lines to STDOUT

### pos.test.out ###

tagged output for the test set given

## Instructions on use ##

1. create model file from POS training data


```
#!python

./postrain.py <training_file> <model_file>

```
 
2. classify text as follows


```
#!python

./postag.py <model_file>  <  test_file  >  outputfile 
```
-------------------------------------------------------------------------------------------------------------------------------------------
# NER #


## Files ##

### nelearn.py ###

learns from training to produce model

### netag.py ###

tags n lines from STDIN, writes to STDOUT

### ner.esp.test.out ###

tagged test data

## Instructions on use ##

1. learn


```
#!python

./nelearn.py <training_file> <model_file>
```

2. classify


```
#!python

./netag <model_file>  <  test_file  >  out_file
```
-----------------------------------------------------------------------------------------------------------------------------------------