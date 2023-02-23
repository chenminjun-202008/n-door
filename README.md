# n-door 问题

背景介绍：[飞书文档] (https://genecast.feishu.cn/docx/Tcx4dr9VJo9vPpx2rNSc4GjBnMe) 或 [n-door problem.pdf](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/n-door%20problem.pdf)

## 代码使用说明

```shell
> python3 ndoor.py -h

usage: ndoor.py [-h] -n NDOOR -t NTRIAL [-fa FIGUREA] [-fb FIGUREB] [-o OUTFILE]

n-door problem

options:
  -h, --help   show this help message and exit
  -n NDOOR     number of doors
  -t NTRIAL    number of trials.
  -fa FIGUREA  Plot:Y=runtime, X=the number of trials
  -fb FIGUREB  Plot:the divergence = |模拟答案-理论值| and the number of trials
  -o OUTFILE   gates(3,5,10,30) and trials(10^(3,4,5,6,7)), hdf5 files are generated with changing/no-changing probality

author: chen.minjun
mail:   chen.minjun@genecast.com.cn
```

## 结果展示

### n个门-重复t次后,获得财宝概率计算

```shell
> python3 ndoor.py -n 3 -t 1000
Ndoor:3 and trials:1000
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 501171.47it/s]
The frequency of changing/no-changing the first choice is 0.6490/0.3510 and use time 0.04s.
```

### n个门-重复t次的运行时间 ![figure](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/result/runtime.png)

尝试 t=1000次、10K次，100K次，1M次 , 程序的运⾏时间(以n=5为例）

```shell
> python3 ndoor.py -n 5 -t 1000 -fa runtime.png

Ndoor:5 and trials:1000
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 334367.35it/s] 
The frequency of changing/no-changing the first choice is 0.2720/0.2050 and use time 0.02s.

100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1000/1000 [00:00<00:00, 334314.04it/s] 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 10000/10000 [00:00<00:00, 358071.30it/s] 
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100000/100000 [00:00<00:00, 392733.18it/s] 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████| 1000000/1000000 [00:02<00:00, 340993.42it/s] 
100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4/4 [00:03<00:00,  1.24it/s]
```

### 不同重复次数模拟概率与理论值的差距 ![figure](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/result/divergence.png)

尝试 t=1000次、10K次，100K次，1M次 ,divergence = |模拟答案-理论|

```shell
> python3 .\ndoor.py -n 5 -t 1000 -fa runtime.png
```

### HDF5文件
```
> python3 .\ndoor.py -n 5 -t 1000 -o result.h5
```

