# n-door 问题

背景介绍：飞书文档 (https://genecast.feishu.cn/docx/Tcx4dr9VJo9vPpx2rNSc4GjBnMe) 或 [n-door problem.pdf](https://git.genecast.com.cn/chen.minjun/n-door/-/blob/main/n-door%20problem.pdf)

## 代码使用说明

```shell
> python3 .\ndoor.py -h

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





