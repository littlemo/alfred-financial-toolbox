# alfred-instalment

提供分期付款并用于固定收益率理财的最终收益计算

## Badge

### GitHub

[![GitHub followers](https://img.shields.io/github/followers/littlemo.svg?label=github%20follow)](https://github.com/littlemo)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/littlemo/alfred-instalment.svg)](https://github.com/littlemo/alfred-instalment)
[![GitHub stars](https://img.shields.io/github/stars/littlemo/alfred-instalment.svg?label=github%20stars)](https://github.com/littlemo/alfred-instalment)

### 其他

[![Alfred3 Workflow](https://img.shields.io/badge/alfred3-workflow-brightgreen.svg)](https://www.alfredapp.com)
[![license](https://img.shields.io/github/license/littlemo/alfred-instalment.svg)](https://github.com/littlemo/alfred-instalment)
[![](https://img.shields.io/badge/bitcoin-donate-green.svg)](https://keybase.io/littlemo)

## 使用截图

![0.png](https://github.com/littlemo/alfred-instalment/blob/master/screenshot/0.png)
![1.png](https://github.com/littlemo/alfred-instalment/blob/master/screenshot/1.png)
![2.png](https://github.com/littlemo/alfred-instalment/blob/master/screenshot/2.png)
![3.png](https://github.com/littlemo/alfred-instalment/blob/master/screenshot/3.png)
![4.png](https://github.com/littlemo/alfred-instalment/blob/master/screenshot/4.png)

## 功能描述

该 workflow 将计算指定金额在指定分期数下（以及可能存在的手续费），通过理财所获得的最终收益。并将分期详情列表输出到 `放大显示` 与 `系统剪贴板` 中。

调用用例： `fq 6000 12 4 0.3` ，计算 6000 元以 0.3% 月手续费分 12 期的情况下，进行预期年化 4% 的活期理财（毕竟是要按月还钱的），所得的最终收益。

> 通过对结果条目触发 `enter` 事件，可放大显示详情信息，并同时输出到剪贴板中

## License

本项目采用 [![license](https://img.shields.io/github/license/littlemo/alfred-instalment.svg)](https://github.com/littlemo/alfred-instalment) 协议开源发布，请您在修改后维持开源发布，并为原作者额外署名，谢谢您的尊重

## 问题

如果您在使用该镜像时遇到任何问题，请查看镜像源码的 [littlemo/alfred-instalment](https://github.com/littlemo/alfred-instalment) Repo，并在其中提交 Issues 给我，多谢您的帮助~~
