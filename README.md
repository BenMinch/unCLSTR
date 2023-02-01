# unCLSTR
unCLSTR is a tool for parsing Cd-hit clstr files into csv format in a way that is easier to work with and perform downstream analysis.

## Use cases

The standard output of a cd-hit run is a .clstr file showing all the clusters and their members as well as a file with all the representative sequences for each cluster. This is usually good enough but sometimes you want to be able to parse out which sequences got placed in which clusters during your analysis. This is where unCLSTR comes into play as it can change the .clstr file into a .csv that can be used in python or R for further analysis. Some potential uses include..

1) Finding only clusters with a particular taxa or identifier.
2) Looking at cluster trends and membership.
3) Assessing average length in each cluster and what type of sequences are clustering together. 

I am no where near an expert in clustering algorithms so I'm sure there are a lot of applications I am missing.

## How to use
1) Download unCLSTR.py and put it into your working directory with your .clstr file
2) On an open terminal run `python unCLSTR.py input.clstr outname`
- Input.clstr: This is your raw clusterfile from the cd-hit run
- outname: this is what you want to name the output files

## Outputs
1) outname_total_members.csv: This is basically just a parsed version of your .clstr file. This is what you will want most of the time
2) outname_rep_members.csv: This just has the representative sequence for each cluster (this information can also just be gathered from the FASTA file it spits out but it requires a few more steps).
