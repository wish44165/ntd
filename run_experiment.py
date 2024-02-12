"""
PuriDivER
Copyright 2022-present NAVER Corp.
GPLv3
"""
import os

import argparse

from configuration.config import Args, build_command_line_args

def parse_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument('--mem_manage', type=str, choices=["none", "RSV", "GBS", "RM", "PuriDivER", "NTD"], default='none', help='memory management')
    parser.add_argument('--robust_type', type=str, choices=["none", "const_reg", "SELFIE", "soft_relabel", "PuriDivER", "contrast"], default='none', help='Robust Learning Type when training')
    parser.add_argument('--dataset', type=str, choices=["cifar10", "cifar100", "WebVision-V1-2", "Food-101N"], default='cifar10', help='Dataset name')
    parser.add_argument('--dataset_path', type=str, default='./dataset/cifar10/', help='dataset path')
    parser.add_argument('--n_tasks', type=int, default=5, help='The number of tasks')
    parser.add_argument('--n_cls_a_task', type=int, default=2, help='The number of class of each task')
    parser.add_argument('--n_init_cls', type=int, default=2, help='The number of classes of initial task')
    parser.add_argument('--warmup', type=int, default=1, help='Warm-up Epochs')
    parser.add_argument('--rnd_seed', nargs="+", type=int, default=[1, 2, 3], help='Random seed number')
    parser.add_argument('--memory_size', type=int, default=500, help='Episodic memory size')
    parser.add_argument('--log_path', type=str, default='./results/', help='The path logs are saved. Only for local-machine')
    parser.add_argument('--model_name', type=str, choices=["resnet18", "resnet32", "resnet34"], default='resnet18', help='Backbone model name')
    parser.add_argument('--batchsize', type=int, default=512, help='Batch size')
    parser.add_argument('--n_epoch', type=int, default=255, help='Epochs')
    parser.add_argument('--n_worker', type=int, default=0, help='Number of workers')
    parser.add_argument('--lr', type=float, default=0.1, help='Learning rate')
    parser.add_argument('--init_model', nargs='?', const=True, default=True, help='Initialize model parameters for every iterations')
    parser.add_argument('--init_opt', nargs='?', const=True, default=True, help='Initialize optimizer states for every iterations')
    parser.add_argument('--topk', type=int, default=1, help='Set k when we want to set topk accuracy')
    #parser.add_argument('--transforms', type=str, default=List[Literal["cutmix", "cutout", "randaug", "autoaug"]], help='Additional train transforms')
    parser.add_argument('--exp_name', type=str, choices=["blurry10", "blurry10_symN20", "blurry10_symN40", "blurry10_symN60", "blurry10_asymN20", "blurry10_asymN40"], default='blurry10_symN20', help='Experiment name')
    parser.add_argument('--debug', nargs='?', const=True, default=False, help='Turn on Debug mode')
    parser.add_argument('--coeff', type=float, default=1.0, help='Coefficiency')
    parser.add_argument('--noise_rate', type=float, default=0.0, help='only for CoTeaching.')
    return parser.parse_known_args()[0] if known else parser.parse_args()

opt = parse_opt()

# Default args
args = Args()

args.robust_type = "PuriDivER" # none, SELFIE, CoTeaching, DivideMix, PuriDivER
args.mem_manage = "PuriDivER" # RSV, GBS, RM, PuriDivER
args.dataset = "cifar10" # cifar10, cifar100, WebVision-V1-2, Food-101N
args.exp_name = "blurry10" # WebVision-V1-2, Food-101N: blurry10, others: blurry10_symN20, blurry10_symN40, blurry10_symN60, blurry10_asymN20, blurry10_asymN40
args.dataset_path = f"dataset/{args.dataset}"

args.dataset = opt.dataset

if args.dataset == "cifar10":
    args.n_cls_a_task = 2
    args.n_init_cls = 10
    args.memory_size = 500
    args.n_tasks = 5
    args.model_name = "resnet18"
    args.warmup = 10 # change to 10 (1 for test)
    args.n_epoch = 255 # The epoch is 256 because of online learning (one-pass).

elif args.dataset == "cifar100":
    args.n_cls_a_task = 20
    args.n_init_cls = 100
    args.memory_size = 2000
    args.n_tasks = 5
    args.model_name = "resnet32"
    args.warmup = 30
    args.n_epoch = 255 # The epoch is 256 because of online learning (one-pass).

elif args.dataset == "WebVision-V1-2":
    args.n_cls_a_task = 5
    args.n_init_cls = 50
    args.memory_size = 1000
    args.n_tasks = 10
    args.model_name = "resnet34"
    args.warmup = 10
    args.n_epoch = 127 # The epoch is 128 because of online learning (one-pass).

elif args.dataset == "Food-101N":
    args.n_cls_a_task = 20
    args.n_init_cls = 101
    args.memory_size = 2000
    args.n_tasks = 5
    args.model_name = "resnet34"
    args.warmup = 10
    args.n_epoch = 127 # The epoch is 128 because of online learning (one-pass).

else:
    raise NotImplementedError()

args.batchsize = 16
args.lr = 0.05

args.rnd_seed = [1, 2, 3] # 1 2 3
args.log_path = "results"

args.transforms = ["autoaug", "cutmix"]
args.n_worker = 2

args.init_model = False
args.init_opt = True
args.topk = 1

args.debug = False

args.coeff = 0.5

# custom
args.exp_name = opt.exp_name
args.dataset_path = opt.dataset_path
args.debug = opt.debug

args.mem_manage = opt.mem_manage
args.robust_type = opt.robust_type
args.rnd_seed = opt.rnd_seed

args_text = build_command_line_args(args)
command = f'python main.py {args_text}'

print(f"[Execute] {command}")
os.system(command)