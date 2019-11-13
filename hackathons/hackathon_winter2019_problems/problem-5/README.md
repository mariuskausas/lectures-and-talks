# Automated submission of analyses to online servers 

## Reference

Taken from [UCLA Github](https://github.com/QCB-Collaboratory/Python-Hackathon-Fall2017/blob/master/Materials_Resources/Problem-4/Readme.md)

## Introduction

Predicting the presence and location of cleavage sites of signal peptides is a complex and interesting problem. For instance, the presence of a signal peptide in a given protein of interest indicates that it is destined towards the secretory pathway. Also, in genome sequencing and proteomics studies, one can estimate the diversity of secreted proteins by targeting the structure of the signal peptide. SignalP 4.1 Server uses a neural network to find cleavage sites of signal peptides for Gram-positive prokaryotes, Gram-negative prokaryotes, and eukaryotes. To use it, you can use a web interface by the Center for Biological Sequence Analysis at the Technical University of Denmark (DTU):

http://www.cbs.dtu.dk/services/SignalP/

<img src="./figures/scheme_signalPclient.png" width="600" />

### Primary goal

During the Hackathon, we will develop a Python script or module that automates the detection of cleavage sites of signal peptide in sequences of aminoacid. This module should control for how often the requests are made, and how the output files are saved.


### Technical challenges

* Automating genomics analyses based on online applications

* Dealing with a bottleneck when analyzing a large dataset

* Learning how to construct web crawlers


### Guideline

1. Read about web crawlers and look for which Python libraries you can use. The library should be able to fill forms.

2. Go to [SignalP 4.1 Server](http://www.cbs.dtu.dk/services/SignalP/). Try submitting one sequence and learn how the options in the form work.

3. Make a scheme with each of the steps of your web crawler needs to perform. 

4. Write your script and test it with small examples before. When using a dataset with more than 200 sequences, set a generous delay between each of the batches - so you would not overwhelm the server!

### Inputs

#### Single peptide singal sequence

An example of a single protein sequence containing a singal peptide:

https://www.uniprot.org/uniprot/P01165#ptm_processing

#### Dataset

Chlamydomonas reinhardtii's proteome, available on the Genome Portal hosted by the Joint Genome Institute:

https://genome.jgi.doe.gov/chlamy/chlamy.download.ftp.html

Please follow to the repository's resources folder to download [Chlamydomonas reinhardtii's proteome](./resources/Chlre4_best_proteins.fasta) in a .fasta format.

### Resources

* Read a little bit about [web crawlers](https://en.wikipedia.org/wiki/Web_crawler). They are extremely useful in many areas, including the automation of the use of online applications that do not offer APIs.

* There are many Python libraries to construct web crawlers. Start reading [mechanize](https://github.com/python-mechanize/mechanize).

* Example of [filling forms with mechanize](https://stackoverflow.com/questions/3516655/python-auto-fill-with-mechanize.

https://stackoverflow.com/questions/38718891/python3-nothing-happens-when-submitting-a-form-via-mechanicalsoup
