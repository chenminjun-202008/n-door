# n-door 问题

背景介绍：[飞书文档](https://genecast.feishu.cn/docx/Tcx4dr9VJo9vPpx2rNSc4GjBnMe) 或 [n-door problem.pdf](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/n-door%20problem.pdf)


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
email:   chen.minjun@genecast.com.cn
```


## 结果展示

### n个门-重复t次后,获得财宝概率计算

```shell
> python3 ndoor.py -n 3 -t 1000
```

### n个门-重复t次的运行时间 ![figure1](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/result/runtime.png)

尝试 t=1000次、10K次，100K次，1M次 , 程序的运⾏时间(以n=5为例）

```shell
> python3 ndoor.py -n 5 -t 1000 -fa runtime.png
```

### 不同重复次数模拟概率与理论值的差距 ![figure2](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/result/divergence.png)

尝试 t=1000次、10K次，100K次，1M次 ,divergence = |模拟答案-理论|

```shell
> python3 ndoor.py -n 5 -t 1000 -fa runtime.png
```

### HDF5文件 ![file](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/result/ndoor-ntrial-probablity.h5)
```
> python3 .\ndoor.py -n 5 -t 1000 -o result.h5
```
