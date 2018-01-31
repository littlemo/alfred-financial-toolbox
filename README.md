# alfred-instalment

提供分期付款并用于固定收益率理财的最终收益计算

## Badge

### GitHub

[![GitHub followers](https://img.shields.io/github/followers/littlemo.svg?label=github%20follow)](https://github.com/littlemo)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/littlemo/alfred-instalment.svg)](https://github.com/littlemo/alfred-instalment)
[![GitHub stars](https://img.shields.io/github/stars/littlemo/alfred-instalment.svg?label=github%20stars)](https://github.com/littlemo/alfred-instalment)
[![GitHub release](https://img.shields.io/github/release/littlemo/alfred-instalment.svg)](https://github.com/littlemo/alfred-instalment/releases)
[![Github commits (since latest release)](https://img.shields.io/github/commits-since/littlemo/alfred-instalment/latest.svg)](https://github.com/littlemo/alfred-instalment)

[![Github All Releases](https://img.shields.io/github/downloads/littlemo/alfred-instalment/total.svg)](https://github.com/littlemo/alfred-instalment/releases)
[![Github All Releases (by Asset)](https://img.shields.io/github/downloads/littlemo/alfred-instalment/alfred-instalment.alfredworkflow.svg)](https://github.com/littlemo/alfred-instalment/releases)
[![GitHub Release Date](https://img.shields.io/github/release-date/littlemo/alfred-instalment.svg)](https://github.com/littlemo/alfred-instalment/releases)

### 其他

[![Alfred3 Workflow](https://img.shields.io/badge/alfred3-workflow-brightgreen.svg)](https://www.alfredapp.com)
[![license](https://img.shields.io/github/license/littlemo/alfred-instalment.svg)](https://github.com/littlemo/alfred-instalment)
[![](https://img.shields.io/badge/bitcoin-donate-green.svg)](https://keybase.io/littlemo)

## 使用展示

![0.png](https://github.com/littlemo/alfred-instalment/blob/master/screenshot/0.png)
![1.png](https://github.com/littlemo/alfred-instalment/blob/master/screenshot/1.png)
![2.png](https://github.com/littlemo/alfred-instalment/blob/master/screenshot/2.png)
![3.png](https://github.com/littlemo/alfred-instalment/blob/master/screenshot/3.png)

```
01期 月初：￥  6,000.00  月末：￥  6,020.00  费用：￥     18.00
02期 月初：￥  5,520.00  月末：￥  5,538.40  费用：￥     18.00
03期 月初：￥  5,038.40  月末：￥  5,055.19  费用：￥     18.00
04期 月初：￥  4,555.19  月末：￥  4,570.38  费用：￥     18.00
05期 月初：￥  4,070.38  月末：￥  4,083.95  费用：￥     18.00
06期 月初：￥  3,583.95  月末：￥  3,595.89  费用：￥     18.00
07期 月初：￥  3,095.89  月末：￥  3,106.21  费用：￥     18.00
08期 月初：￥  2,606.21  月末：￥  2,614.90  费用：￥     18.00
09期 月初：￥  2,114.90  月末：￥  2,121.95  费用：￥     18.00
10期 月初：￥  1,621.95  月末：￥  1,627.36  费用：￥     18.00
11期 月初：￥  1,127.36  月末：￥  1,131.11  费用：￥     18.00
12期 月初：￥    631.11  月末：￥    633.22  费用：￥     18.00
[月缴本金]：    500.00   [月缴费用]：     18.00
[理财收益]：    133.22   [分期成本]：    216.00
[最终收益]：    -82.78
```

## 下载安装

[![Download Here](https://img.shields.io/badge/Download-Here-brightgreen.svg)](https://github.com/littlemo/alfred-instalment/releases)

选择最新的 `Release` 下载，并双击运行，即可完成安装

## 功能描述

该 workflow 将计算指定金额在指定分期数下（以及可能存在的手续费），通过理财所获得的最终收益。并将分期详情列表输出到 `放大显示` 与 `系统剪贴板` 中。

调用用例： `fq 6000 12 4 0.3` ，计算 6000 元以 0.3% 月手续费分 12 期的情况下，进行预期年化 4% 的活期理财（毕竟是要按月还钱的），所得的最终收益。

> 通过对结果条目触发 `enter` 事件，可放大显示详情信息，并同时输出到剪贴板中

## 现存问题

### Large Type 显示的对齐问题
原因在于 Alfred 在 Large Type 显示时使用的字体是非等宽字体，故造成对齐困难，还未想到好的解决办法

目前可通过输出到 __系统剪贴板__ 的方式，用户在第三方编辑器（等宽字体显示）中粘贴查看，效果会好很多

## License

本项目采用 [![license](https://img.shields.io/github/license/littlemo/alfred-instalment.svg)](https://github.com/littlemo/alfred-instalment) 协议开源发布，请您在修改后维持开源发布，并为原作者额外署名，谢谢您的尊重

## 问题

如果您在使用该应用时遇到任何问题，请在 GitHub 上查看本项目 [![alfred-instalment](https://img.shields.io/badge/Repo-alfred--instalment-brightgreen.svg)](https://github.com/littlemo/alfred-instalment) ，并在其中提交 Issues 给我，多谢您的帮助~~
