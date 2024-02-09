# NTD

5th CLVISION CVPR Workshop

<details><summary>Conda Setup</summary>

```bash
$ conda create -n ntd python=3.10 -y
$ conda activate ntd
```

</details>


<details><summary>Clone and Install</summary>

```bash
$ cd ntd/
$ pip install -r requirements.txt
```

</details>


<details><summary>Trial (rnd_seed 1)</summary>

```bash
# PuriDivER
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage PuriDivER --robust_type PuriDivER --rnd_seed 1 --exp_name blurry10_asymN40

# NTD
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --rnd_seed 1 --exp_name blurry10_asymN40
```

</details>


<details><summary>Execute Command</summary>

```bash
$ python run_experiment.py --dataset_path <dataset path> \
                           --mem_manage <memory construction type> \
                           --robust_type <memory usage type> \
                           --exp_name <noisy level and type>

# example
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_symN20
```

</details>


<details><summary>Reproduce Command</summary>

```bash
# CIFAR10
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_symN20

$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_symN40

$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_symN60

$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_asymN20

$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --exp_name blurry10_asymN40

# CIFAR100
$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_symN20

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_symN40

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_symN60

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_asymN20

$ python run_experiment.py --dataset cifar100 --dataset_path ../../../../datasets/cifar100_png --mem_manage NTD --robust_type none --exp_name blurry10_asymN40
```

</details>
