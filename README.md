# Fair and Robust Continual Learning: Mitigating Noisy Labels in Data Streams

5th CLVISION CVPR Workshop

<details><summary>Create Conda Environment</summary>

```bash
$ conda create -n ntd python=3.10 -y
$ conda activate ntd
```

</details>


<details><summary>Install Required Packages</summary>

```bash
$ git clone https://github.com/wish44165/ntd.git
$ cd ntd/
$ pip install -r requirements.txt
```

</details>


<details><summary>Datasets Preparation</summary>

- [CIFAR10](https://github.com/hwany-j/cifar10_png)
- [CIFAR100](https://github.com/hwany-j/cifar100_png)
- [WebVision](https://data.vision.ee.ethz.ch/cvl/webvision/download.html)
- [Food-101N](https://kuanghuei.github.io/Food-101N/)

</details>


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

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_symN60

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_asymN20

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_asymN40
```

</details>
