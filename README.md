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

```
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage PuriDivER --robust_type PuriDivER --rnd_seed 1 --exp_name blurry10_asymN40
```

```
$ python run_experiment.py --dataset_path ../../../../datasets/cifar10_png --mem_manage NTD --robust_type none --rnd_seed 1 --exp_name blurry10_asymN40
```
