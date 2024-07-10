CSEL-BGC: A bioinformatics framework integrating machine learning define the biosynthetic evolutionary landscape of uncharacterized antibacterial natural products
=

The sluggish pace of new antibacterial drug development reflects a vulnerability in the face of the current severe threat posed by bacterial resistance. Microbial natural products (NPs), as a reservoir of immense chemical potential, have emerged as the most promising avenue for the discovery of next generation antibacterial agent. Directly accessing the antibacterial activity of potential products derived from biosynthetic gene clusters (BGCs) would significantly expedite the process. To tackle this issue, we propose a CSEL-BGC framework that integrates machine learning (ML) techniques. This framework involves the development of a novel cascade-stacking ensemble learning (CSEL) model and the establishment of a groundbreaking model evaluation system. Based on this framework, we predict 6,666 BGCs with antibacterial activity from 3,468 complete bacterial genomes and elucidate a biosynthetic evolutionary landscape to reveal their antibacterial potential. This provides crucial insights for interpretating the synthesis and secretion mechanisms of unknown NPs.

![image](https://github.com/Du-Minghui/CSEL/blob/main/Graphic%20Abstract.jpg)


Attention!
=

***Our project is currently in progress and will be further refined in the near future***

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


## Reference

* [DeepBGC](https://github.com/Merck/bgc-pipeline) - DeepBGC development & evaluation code
* [SRD](https://github.com/davidbajusz/srdpy) - Python implementation of Sum of Ranking Differences (SRD)
* [DF](https://github.com/LAMDA-NJU/Deep-Forest) - Deep Forest model

