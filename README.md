# Latent Semantic Analysis for Topic Modelling

## Table of contents

* [Introduction](#Introduction)

* [Brief explanation of Topic Modelling and Topic Classification](#Brief-expenation-of-Topic-Modelling-and-Topic-Classification)

* [Input and Output data](#Input-and-Output-Data)

* [Algorithm analysis](#Algorithm-analysis)

* [Program structure and content](#Program-structure-and-content)

* [Installation](#Installation)

* [Usage examples](#Usage-examples)

* [Contributors](#Contributors)


## Introduction

Reading all the data, analyzing and sorting it is very important but really tough work. Especially when referring to enormous data. Doing this manually takes a lot of time and energy, that person could instead use for other more important things. Therefore it really makes sense to delegate this work to computers, that will perform this task not worse and not less accurately than a human. In this way, a person will have more opportunities to spend time for other duties while the computer processes data and groups it by related topics. That is where Topic Modelling comes into play.

Our main goal was to make a program that would analyze context of documents and group them by topics. We also wanted to provide users with key words from each topic to give him better understanding what exactly those topics are about.

## Brief expenation of Topic Modelling and Topic Classification

Topic modeling is a machine learning technique that is able to scan a set of documents, determining some word and phrase patterns within them, and thus with their help grouping words and similar expressions that describe a set of documents into clusters. In simpler words, topic modeling together with topic classification detects topic for a certain document.

What is the difference between Topic Modeling and Topic Classification? Topic modeling algorithms give us collections of words and phrases that are related somehow, leaving us the task of figuring out what the relation is, while topic classification provides us with groups that are already labeled, eliminating any guesswork. In addition, topic modeling is an ‘unsupervised’ technique (doesn’t need a predefined list of tags or training data that’s been previously prepared by us). And topic classification is known as ‘supervised’ machine learning techniques.

Why do we need Topic Analysis? Simple example: Let’s say you are a director of some company and you want to know what customers' feedback is about particular features of your product. You can simply analyze them with a topic modeling algorithm. By defining word frequency and distance between words, a topic model groups feedback that is similar, and words and phrases that appear most often. And with this information, you can easily define what each set of texts are about. You can also apply topic classification to see already defined labels.


## Input and Output data

* Input data

Our data we used to test the program:

[Testing data](https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups)

The data is organized into 20 different newsgroups, each corresponding to a different topic. Some of the newsgroups are very closely related to each other (e.g. comp.sys.ibm.pc.hardware / comp.sys.mac.hardware), while others are highly unrelated (e.g misc.forsale / soc.religion.christian).

* Output data

The output is in the form of a table, that shows topics, grouped documents and keywords that correspond to certain topic. There is also a plot that shows quantity of grouped documents in each topic.

## Algorithm analysis

To perform Latent Semantic Analysis we are using SVD. Before applying this algorithm we are creating a term-document matrix that is modified with TF-IDF that gives us additional information about the uniqueness of the certain words. 

* TF-IDF - term frequency - inverse document frequency - is a numerical statistic that can be used to determine how important a word is to the document in a collection or corpus of different documents. 

* SVD - singular value decomposition - is the factorisation of the matrix A that generalizes the eigendecomposition of a square matrix to the m x n matrix via an extension of the polar decomposition. Every m x n matrix can be represented as A = USVT. In general, SVD is useful as it finds a reduced dimensional representation of our document-term matrix that emphasizes the strongest relationships and throws away not needed information. We reconstruct the matrices in such a way to have only the most important information for us.

## Program structure and content

Main module where the program can be run:

[main.py](https://github.com/Sofia-Kyba/Semester_Homework_Ucu/blob/master/modules/main.py)

Module with functions for reading files from the archive and cleaning data from stop words and words shorter than 2 symbols:

[process_data.py](https://github.com/muliarska/LSA_topic_modeling/blob/main/modules/process_data.py)

Module with function form_tdm() that forms term-document matrix and tf_idf_modification() that performs TF-IDF algorithm on constructed term-document matrix:

[tdm.py](https://github.com/muliarska/LSA_topic_modeling/blob/main/modules/tdm.py)

Module with function apply_svd_basic() where built-in function for SVD algorithm is uded and function classify_into_topics() that groupes documents by related topics using results of SVD algorithm:

[svd.py](https://github.com/muliarska/LSA_topic_modeling/blob/main/modules/svd.py)

Module for extracting keywords for each topic using results of SVD algorithm:

[topic_classification.py](https://github.com/muliarska/LSA_topic_modeling/blob/main/modules/topic_classification.py)

Module for web application and visualisation of results:
 
[app.py](https://github.com/muliarska/LSA_topic_modeling/blob/main/modules/app.py)


## Installation

First of all write in the command prompt:

`$git clone https://github.com/muliarska/LSA_topic_modeling.git`

Then to run the program you need:

`$pip install -r requirements.txt`

To run the program you need:
`$python3 app.py`

## Usage examples

After running the app.py and following the link you will see:



After that you need to upload archive with documents in ZIP or TAR.GZ formats.
Then after uploading you can get such a result:

 

## Contributors

- [Yana Muliarska](https://github.com/muliarska)
- [Sofia Kyba](https://github.com/Sofia-Kyba)
- [Khrystyna Kokolus](https://github.com/khristinakokolus)

