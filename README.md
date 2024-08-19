CSEL-BGC: A bioinformatics framework integrating machine learning define the biosynthetic evolutionary landscape of uncharacterized antibacterial natural products
=

The sluggish pace of new antibacterial drug development reflects a vulnerability in the face of the current severe threat posed by bacterial resistance. Microbial natural products (NPs), as a reservoir of immense chemical potential, have emerged as the most promising avenue for the discovery of next generation antibacterial agent. Directly accessing the antibacterial activity of potential products derived from biosynthetic gene clusters (BGCs) would significantly expedite the process. To tackle this issue, we propose a CSEL-BGC framework that integrates machine learning (ML) techniques. This framework involves the development of a novel cascade-stacking ensemble learning (CSEL) model and the establishment of a groundbreaking model evaluation system. Based on this framework, we predict 6,666 BGCs with antibacterial activity from 3,468 complete bacterial genomes and elucidate a biosynthetic evolutionary landscape to reveal their antibacterial potential. This provides crucial insights for interpretating the synthesis and secretion mechanisms of unknown NPs.

![image]()


Experimental details
=

## Hardware environment
Our project was completed in the following hardware environment:

- `CPU`: Intel(R) Core(TM) i7-12700 CPU @ 2.10GHz
- `RAM`: 64GB
- `System`: Ubuntu 22.04

## Training duration

The table below displays the time taken by the CSEL model over 10 replicates of 5-fold cross-validation.

| HPO     | CPU times    | Wall time    |
| :------------- | :-------------: | -------------: |
| Yes      | 10h 25min 47s      | 5h 27min 20s      |
| No      | 8h 37min 53s     | 5h 45min 3s      |

## Random seed settings
We did not set a random seed in the base module of the CSEL model, as we rely on the average performance metrics of 10 replicates of 5-fold cross-validation to mitigate randomness.


# Data Preprocessing

## 1. MIBiG Dataset

### 1.1 Downloading from the Database

Download all entries in both GBK and JSON formats for:
- Version 1.3 from [MIBiG Database v1.3](https://mibig.secondarymetabolites.org/download)
- Version 3.1 from [MIBiG Database v3.1](https://mibig.secondarymetabolites.org/download)

### 1.2 Installing HMMER and Downloading PFAM Database

- Install HMMER version 3.1b2
- Download PFAM 34.0 database

### 1.3 Annotating BGC Entries Using HMMER

Run HMMER to scan BGC entries for Pfam domains :
```bash
hmmscan --domtblout mibig_domtbl.tbl /pfam/Pfam-A.hmm mibig_proteins.fa
```

### 1.4 Extracting BGC Features Using DeepBGC Pipeline

Use Python scripts from the DeepBGC pipeline:
```bash
python domtbl2csv.py -i mibig_domtbl.tbl -f proteins2fasta -o mibig_domains.csv
python positive_mibig.py -i mibig_domains.csv -g genome -o mibig_bgcs_all -md 1 -mp 1 -e 0.01
```

### 1.5 Building the Feature Matrix

Use `bgc_counts.ipynb` to build the feature matrix.

### 1.6 Extracting BGC Chemical Activity

Due to differences in encoding methods between JSON files of versions 3.1 and 1.3, we modified the script `mibig_compounds.py` to `mibig_compounds_.py`. Extract BGC chemical activity using:
```bash
python mibig_compounds_.py -g mibig_gbk_3.1 -j mibig_json_3.1 -o mibig_compounds.csv
```

### 1.7 Building the Chemical Activity Matrix

Use `activity_counts.ipynb` to build the chemical activity matrix.

### 1.8 Filtering Antibacterial Activity BGCs

Filter out BGCs with antibacterial activity from the dataset.

## 2. NCBI RefSeq Dataset

### 2.1 Installing antiSMASH and BIG-SCAPE

- Install antiSMASH version 6.1
- Install BIG-SCAPE version 1.1.5

### 2.2 Identifying BGCs Using antiSMASH

Run antiSMASH with the following parameters:
```bash
--cb-general --cb-knownclusters --cb-subclusters --genefinding-tool prodigal --allow-long-headers
```

### 2.3 Extracting antiSMASH Results

Use the provided script to convert HTML results to CSV:
```bash
python html2csv.py -i [input HTML format] -o [output CSV format]
```

### 2.4 Partition the dataset based on the similarity of BGCs

BGCs with similarity >75% are used as the external test set, while BGCs with similarity = 0 are utilized for the discovery of potential antimicrobial natural products.


### 2.5 Identifying Pfam Domains Using BIG-SCAPE

Run BIG-SCAPE with the following parameters:
```bash
--pfam_dir /pfam/34.0 --mibig
```

### 2.6 Consolidating BGC Pfam IDs

Combine and organize Pfam IDs from BGCs:
```bash
paste -s *.pfs > pfs.txt
```

### 2.7 Building the Feature Matrix

Use `onehot.ipynb` to build the feature matrix.


# Hyperparameter Settings

Refer to the supplementary materials for hyperparameter settings.

# Other Relevant Configurations

Refer to the code section for other relevant configurations.


# Reference

* [DeepBGC](https://github.com/Merck/bgc-pipeline) - DeepBGC development & evaluation code
* [SRD](https://github.com/davidbajusz/srdpy) - Python implementation of Sum of Ranking Differences (SRD)
* [DF](https://github.com/LAMDA-NJU/Deep-Forest) - Deep Forest model



**Jul 10, 2024 :**

1. Establish a repository

2. Upload the core code of the model

3. Upload the code for generating drawings

**Jul 14, 2024 :**

1. Supplement data

2. Upload data preprocessing scripts

3. Upload Shell scripts

4. Upload the model evaluation system

**Jul 17, 2024 :**

1. Upload AgglomerativeHC

2. Upload Bigscape

3. Upload NaPDoS2

4. Document the data preprocessing steps

5. Rectify errors
