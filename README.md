------------------------------------------------------------------------------------------------------------------------------------------
# PART 1  - PERCEPTRON  IMPLEMENTATION #

## THIS IMPLEMENTATION IS NOT AVERAGED PERCEPTRON BUT MULTICLASS PERCEPTRON ##

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
# PART II - POS tagging #

## Files ##

### postrain.py ###

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
# PART III - NER #


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

# PART IV #

## (1) Accuracy of POS tagger on dev set ##

1. **=  .94** after 20 iterations of training

2. **=  .96** after 40 iteraions of training

Note: this is a multiclass perceptron


## (2) Precision, Recall, F Scores for NER for all entities  ##

```
#!python

CLASS: B-LOC

precision: 0.717479674796748
recall: 0.7853170189098999
f_score: 0.7498672331386087

```


```
#!python

CLASS: O

precision: 0.9889540523855719
recall: 0.9810804899387576
f_score: 0.9850015371777416
```


```
#!python

CLASS: B-ORG

precision: 0.8252941176470588
recall: 0.8156976744186046
f_score: 0.82046783625731

```



```
#!python

CLASS: B-PER

precision: 0.8126022913256956
recall: 0.8240663900414937
f_score: 0.8182941903584673
```



```
#!python

CLASS: I-PER
precision: 0.7590221187427241
recall: 0.9731343283582089
f_score: 0.8528449967298888

```


```
#!python

CLASS: B-MISC

precision: 0.5305810397553516
recall: 0.7728285077951003
f_score: 0.629193109700816

```


```
#!python

CLASS: I_ORG
precision: 0.7715959004392386
recall: 0.6214622641509434
f_score: 0.6884389288047028

```



```
#!python

CLASS: I-LOC

precision: 0.486646884272997
recall: 0.7772511848341233
f_score: 0.5985401459854015

```



```
#!python

CLASS: I-MISC

precision: 0.5305810397553516
recall: 0.7728285077951003
f_score: 0.629193109700816
```

## Overall statistic for NER ##


```
#!python

**Overall F score:  .76**
**Accuracy: .95**
```

## (3) Using Naive Bayes Classifier instead of perceptron ##

When Naive Bayes classifies was used for POS tagging instead of perceptron. Following were the observations.

### Accuracy of tagging DEV set: ###

* Accuracy of tagging POS for dev set was **reduced to .63 from .94**
* If you calculate f-score for any class, that is quite low as well -> **f_score for 'NN' from perceptron comes out to .95 and from naive bayes it comes out to be .67**

* The reason for such a low score on accuracy level for Naive Bayes classification is arguably due to the independence assumption of Naive Bayes. Naive Bayes does not take into consideration the context a word (PREVIOUS, CURRENT, NEXT) as good as perceptron, and hence gives less accuracy on tagging.

* Also  perceptron is trained by many more iterations as compared to Naive Bayes, so it is also a contributing factor, more training = better classification.

-------------------------------------------------------------------------------------------------------------------------------

Naive bayes implementation for POS tagging is at - 
```
#!python

/postagging/nb_test/
```