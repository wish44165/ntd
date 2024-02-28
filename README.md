## Data Stream Sampling with Fuzzy Task Boundaries and Noisy Labels


5th CLVISION CVPR Workshop


### 1. Environmental Setup

<details>

<summary>Hardware Information</summary>

- CPU: Intel® Core™ i7-12650H
- GPU: NVIDIA GeForce RTX 4050 Laptop GPU (6G)
  
</details>

<details><summary>Create Conda Environment</summary>

```bash
$ conda create -n ntd python=3.10 -y
$ conda activate ntd
$ git clone https://github.com/wish44165/ntd.git
$ cd ntd/
$ pip install -r requirements.txt
```

</details>

<details><summary>Datasets Preparation</summary>

- [CIFAR10](https://github.com/hwany-j/cifar10_png)
- [CIFAR100](https://github.com/hwany-j/cifar100_png)
- [WebVision](https://data.vision.ee.ethz.ch/cvl/webvision/download.html) ([Google Images Resized (16 GB)](https://data.vision.ee.ethz.ch/cvl/webvision/google_resized_256.tar) / [Validation Images Resized (834 MB)](https://data.vision.ee.ethz.ch/cvl/webvision/test_images_256.tar))
- [Food-101N](https://kuanghuei.github.io/Food-101N/)

| Datasets    | CIFAR10  | CIFAR100 | WebVision | Food-101N |
| ----------- | -------- | -------- | --------- | --------- |
| # train     | 50000    | 50000    | 65944     | 52867     |
| # test      | 10000    | 10000    | 2500      | 4741      |
| # class     | 10       | 100      | 50        | 101       |
| # tasks     | 5        | 5        | 10        | 5         |
| Memory size | 500      | 2000     | 1000      | 2000      |
| Models      | ResNet18 | ResNet32 | ResNet34  | ResNet34  |
| Batch size  | 16       | 16       | 16        | 16        |
| Epochs      | 256      | 256      | 128       | 128       |

</details>


### 2. Reproducing Details

<details><summary>Execute Commands</summary>

```bash
$ python run_experiment.py --dataset_path <dataset path> \
                           --mem_manage <memory construction type> \
                           --robust_type <memory usage type> \
                           --exp_name <noisy level and type>
```

</details>

<details><summary>Reproduce Commands</summary>

```bash
# CIFAR10
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_symN20
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10_symN20

$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_symN40
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10_symN40

$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_symN60
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10_symN60

$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_asymN20
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10_asymN20

$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_asymN40
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10_asymN40

# CIFAR100
$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_symN20
$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10_symN20

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_symN40
$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10_symN40

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_symN60
$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10_symN60

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_asymN20
$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10_asymN20

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_asymN40
$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10_asymN40

# WebVision
$ python run_experiment.py --dataset WebVision-V1-2 --dataset_path ../../../../datasets/WebVision-V1-2 --mem_manage NTD --robust_type none --exp_name blurry10
$ python run_experiment.py --dataset WebVision-V1-2 --dataset_path ../../../../datasets/WebVision-V1-2 --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10

# Food-101N
$ python run_experiment.py --dataset Food-101N --dataset_path ../../../../datasets/Food-101N/images --mem_manage NTD --robust_type none --exp_name blurry10
$ python run_experiment.py --dataset Food-101N --dataset_path ../../../../datasets/Food-101N/images --mem_manage PuriDivER --robust_type PuriDivER --exp_name blurry10
```

</details>


### 3. Experimental Results

- [logs](https://github.com/wish44165/ntd/tree/main/logs)

<details><summary>Tables</summary>

**Table: Last test accuracy evaluated on CIFAR10 and CIFAR100 datasets with noisy types Sym.-{20%, 40%, 60%} and Asym.-{20%, 40%}.**

| Methods                  | CIFAR10           |                   |                   | CIFAR100          |                   |                   |
|--------------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
|                          | Sym.              |                   |                   | Sym.              |                   |                   |
|                          | 20                | 40                | 60                | 20                | 40                |                   |
| PuriDivER~[1]            | **60.6** ± 1.8    | 57.8 ± 2.2        | **52.0** ± 2.8    | **61.2** ± 2.9    | 49.4 ± 5.7        | 36.3 ± 0.3        |
| NTD (ours)               | 59.8 ± 0.6        | **59.7** ± 1.5    | 50.9 ± 0.3        | 60.1 ± 0.3        | **53.7** ± 3.9    | **38.3** ± 1.0    |


**Table: Last memory clean ratio on CIFAR10 and CIFAR100 datasets with noisy types Sym.-{20%, 40%, 60%} and Asym.-{20%, 40%}.**

| Methods                  | CIFAR10           |                   |                   | CIFAR100          |                   |                   |
|--------------------------|-------------------|-------------------|-------------------|-------------------|-------------------|-------------------|
|                          | Sym.              |                   |                   | Sym.              |                   |                   |
|                          | 20                | 40                | 60                | 20                | 40                |                   |
| PuriDivER~[1]            | 98.6 ± 0.7        | 96.1 ± 0.6        | 86.6 ± 4.0        | 98.7 ± 0.4        | 79.7 ± 7.7        | **99.2** ± 0.1    |
| NTD (ours)               | **99.2** ± 0.5    | **97.1** ± 0.9    | **86.8** ± 0.7    | **98.7** ± 1.0    | **87.9** ± 4.6    | 99.0 ± 0.3        |

**Table: Last test accuracy evaluated on WebVision and Food-101N.**

| Methods                  | WebVision          | Food-101N          |
|--------------------------|--------------------|--------------------|
| PuriDivER~[1]            | $25.1$ ± $0.8$     | $13.8$ ± $0.6$     |
| NTD (ours)               | **26.1** ± $1.6$   | **17.0** ± $0.9$   |

**Table: Last memory clean ratio on WebVision and Food-101N.**

| Methods                  | WebVision          | Food-101N          |
|--------------------------|--------------------|--------------------|
| PuriDivER~[1]            | $100$ ± $0$        | $100$ ± $0$        |
| NTD (ours)               | **100** ± $0$      | **100** ± $0$      |

**References:**

[1] bang2022online


</details>




### 4. Acknowledgments and References

- [Online Continual Learning on a Contaminated Data Stream with Blurry Task Boundaries](https://arxiv.org/abs/2203.15355) ([GitHub](https://github.com/clovaai/puridiver))


### Citation
```
@inproceedings{chen2023one,
  title={One-Epoch Training for Object Detection in Fisheye Images},
  author={Chen, Yu-Hsi},
  booktitle={Proceedings of the 5th ACM International Conference on Multimedia in Asia},
  pages={1--5},
  year={2023}
}
```
