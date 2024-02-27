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

#### 3.1. Last test accuracy

- [epoch_000.pt](https://drive.google.com/file/d/1_8tjqhdgy8UVrWlXnJcFTR4i7erNk0ym/view?usp=sharing)

| Leaderboards     | Filename               | Upload time         | Evaluation result | Ranking |
| ---------------- | ---------------------- | ------------------- | ----------------- | ------- |
| Public & Private | fp-1-0.01-0.5-2172.csv | 2023-08-04 00:51:42 | 0.5700583         | 1/24    |

#### 3.2. Last clean ratio

#### 3.3. Training time spent

#### 3.4. GPU resource requirement


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
