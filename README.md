# PSICalc Algorithm Package

This is a package for clustering Multiple Sequence Alignments (MSAs) utilizing normalized mutual information to examine protein subdomains. A complete data visualization tool for psicalc is available on the releases page. 

As an example:

```
import psicalc as pc

file = "<your_fasta_file>" # e.g "PF02517_seed.txt"

data = pc.read_txt_file_format(file) # read Fasta file

data = pc.durston_schema(data, 1) # Label column index starting at 1

result = pc.find_clusters(1, data) # will sample every column against msa

# Optionally write dictionary to csv
pc.write_output_data(1, result)
```

The program will run and return a csv file with the strongest clusters found in the MSA provided.

Our initial publication can be found here: https://academic.oup.com/bioinformaticsadvances/article/2/1/vbac058/6671262

Following our initial publication, the program was found to associate invariant columns with variable columns in some cases. It was determined that the invariant columns were causing and issue and due to their low entropy offered little information in the way of clustering. Therefore, in the latest version (0.5.1 Roadside Picnic), a we have added the ability to filter out low entropy columns using a sliding scale from 0-0.25 (25%) entropy where entropy is the number of different amino acids found in a column along with the number of occurrences of each amino acid. Invariant columns (i.e., those with only one amino acid) have an entropy of 0. 
As a result of these changes, data run using this latest version will not match what was found in our initial paper, but should represent clusters based upon meaningful relationships. In all cases, researchers are advised to inspect the outputs to confirm the associations are meaningful. 
