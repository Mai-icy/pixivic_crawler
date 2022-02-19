# Pixivic Crawler
一个带有图形界面的pixivic网站爬虫

## 简介 Introduction
这是基于Python3以及Pyqt5的图形界面爬虫，是我在github上的第一个项目。

This is a web crawler for the Pixivic website based on Python3 and Pyqt5,  It was my first project on GitHub.   

## 特性 Features
- 拥有方便操作的用户图形界面 With an easly-operated GUI
- 支持多线程 Support for multithreading
- 可以获取日排行图片和搜索词图片 You can get daily ranking images and search keyword of images

### Version 1.0
- 第一个较为稳定的版本 The first stable version

### Version1.2
- 调整下载图片上限从200至1000 Adjusted the upper limit of downloaded images from 200 to 1000
- 添加针对画师id以及画作id进行图片下载的模式 Add a mode to download images for artist ID and painting ID
- 将符合关键词的图片优先下载 The images that match the keywords will be downloaded first
- 为线程分配内存，防止在运行时候出现未响应 Allocate memory for threads to prevent unresponsiveness at run time(fix bug)

### Version1.3

- 调整部分代码整洁性 Adjust some code neatness
- 搜索图片的时候不再卡顿未响应 The interface is not unresponsive when searching for images
- 自动排除被网站屏蔽的图片 Automatically exclude images which blocked by the site
- 将conf.ini配置文件放到main.pyw同级目录 Modified the configuration file directory
- 优化了部分提示文本 Optimized some hint text

### Version1.5
- 代码重构，真的变的更好了

## 运行环境与依赖 Running environment and requirements
- Windows
- Python 3
- Pyqt5 module

## 联系方式 Contact
邮箱 Email：Maiicy@foxmail.com

## 使用许可 Use license
[MIT](LICENSE) © Lost

