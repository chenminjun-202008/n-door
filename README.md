# n-door 问题

[TOC]

## 背景介绍：[飞书文档](https://genecast.feishu.cn/docx/Tcx4dr9VJo9vPpx2rNSc4GjBnMe) 或 [n-door problem.pdf](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/n-door%20problem.pdf)

n (i.e. n=3) 扇门中有一扇门后面有财宝，每扇门后面有财宝的概率是多少？ 主持人让你选择一扇但不打开。 接着， 他打开任意一扇没有财宝的门后问你， 你愿不愿意更换你的第一选择（=选择另一扇门）？ 
从概率的角度来看：
- 概率1：不换门获得财宝的概率。
- 概率2：选择换门后的获得财宝的概率。



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
  -o OUTFILE   gates(3,5,10,30) and trials(10^(3,4,5,6)), hdf5 files are generated with changing/no-changing probality

author: chen.minjun
email:   chen.minjun@genecast.com.cn
```


## 结果展示

### n个门-t次重复试验,获得财宝的概率

```shell
> python3 ndoor.py -n 3 -t 1000
```

### n个门-不同t次试验的运行时间 ![figure1](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/result/runtime.png)

尝试 t=1000次、10K次，100K次，1M次 , 程序的运⾏时间(以n=5为例）

```shell
> python3 ndoor.py -n 5 -t 1000 -fa runtime.png
```

### 不同重复t次,模拟概率与理论值的差距 ![figure2](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/result/divergence.png)

尝试 t=1000次、10K次，100K次，1M次 ,divergence = |模拟答案-理论|

```shell
> python3 ndoor.py -n 5 -t 1000 -fa runtime.png
```

### HDF5文件 [HDF5](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/result/ndoor-ntrial-probablity.h5)
```
> python3 ndoor.py -n 5 -t 1000 -o result.h5
```
