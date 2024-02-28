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

#### 3.1. Last test accuracy

\begin{table*}
\centering
\footnotesize
  \caption{Last test accuracy evaluated on CIFAR10 and CIFAR100 datasets with noisy types Sym.-{20\%, 40\%, 60\%} and Asym.-{20\%, 40\%}.}
  \label{tab:last_test_accuracy_cifar}
  \begin{tabular}{@{}lcccccccccc@{}}
    \toprule
    \multirow{4}{*}{Methods} & \multicolumn{5}{c}{CIFAR10} & \multicolumn{5}{c}{CIFAR100}\\
    \cmidrule(lr){2-6} \cmidrule(lr){7-11}
    %\midrule
    & \multicolumn{3}{c}{Sym.} & \multicolumn{2}{c}{Asym.} & \multicolumn{3}{c}{Sym.} & \multicolumn{2}{c}{Asym.}\\
    & 20 & 40 & 60 & 20 & 40 & 20 & 40 & 60 & 20 & 40\\ 
    %\cline{2-3} \cline{5-6}
    \cmidrule(r){1-1} \cmidrule(lr){2-4} \cmidrule(lr){5-6} \cmidrule(lr){7-9} \cmidrule(lr){10-11}
    PuriDivER~\cite{bang2022online} & $\boldsymbol{60.6}_{\pm 1.8}$ & $57.8_{\pm 2.2}$ & $\boldsymbol{52.0}_{\pm 2.8}$ & $\boldsymbol{61.2}_{\pm 2.9}$ & $49.4_{\pm 5.7}$ & $36.3_{\pm 0.3}$ & $33.6_{\pm 0.7}$ & $\boldsymbol{28.6}_{\pm 1.7}$ & $34.3_{\pm 1.0}$ & $24.9_{\pm 1.4}$ \\
    \textbf{NTD} (ours) & $59.8_{\pm 0.6}$ & $\boldsymbol{59.7}_{\pm 1.5}$ & $50.9_{\pm 0.3}$ & $60.1_{\pm 0.3}$ & $\boldsymbol{53.7}_{\pm 3.9}$ & $\boldsymbol{38.3}_{\pm 1.0}$ & $\boldsymbol{35.2}_{\pm 1.5}$ & $28.0_{\pm 1.1}$ & $\boldsymbol{37.6}_{\pm 0.3}$ & $\boldsymbol{25.8}_{\pm 1.0}$ \\
    \bottomrule
  \end{tabular}
\end{table*}

|     | CIFAR10  | CIFAR100 | WebVision | Food-101N |
| ----------- | -------- | -------- | --------- | --------- |
| Methods | 20 | 40 | 60 | 20 | 40 | 20 | 40 | 60 | 20 | 40 |
|  |  <td colspan=3> Sym. | <td colspan=2> Asym. | <td colspan=3> Sym. | <td colspan=2> Asym. |
| PuriDivER    | 60.6 | 57.8 | 52.0 | 61.2 | 49.4 | 36.3 | 33.6 | 28.6 | 34.3 | 24.9 |
| **NTD**      | 59.8 | 59.7 | 50.9 | 60.1 | 53.7 | 38.3 | 35.2 | 28.0 | 37.6 | 25.8 |
| # class     | 10       | 100      | 50        | 101       |
| # tasks     | 5        | 5        | 10        | 5         |
| Memory size | 500      | 2000     | 1000      | 2000      |
| Models      | ResNet18 | ResNet32 | ResNet34  | ResNet34  |
| Batch size  | 16       | 16       | 16        | 16        |
| Epochs      | 256      | 256      | 128       | 128       |

#### 3.2. Last memory clean ratio

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
