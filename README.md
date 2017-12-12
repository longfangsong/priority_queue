**该项目已经有beta版本发布！**

**This Project now has beta release!**
# 优先队列

这是一个任务管理App。

作者开发这个App的原因是因为有选择障碍症，在手头有多个任务时往往不知道要先做什么好。

希望能帮到和我有同样毛病的人……

也希望有大佬来提意见&帮着开发。

## 技术选型
前端使用[quasar框架](http://quasar-framework.org)，这是一个用于构建网页和Hybrid App的框架。

支持Vue全家桶和将前端页面用[Cordova](http://cordova.apache.org)封装成App。

（曾经有一个未发布的版本使用的是Weex，然而Weex的文档太烂，对web标准的支持又太差，说是说用web技术构建原生App其实几乎完全是另外一套东西，限制特别大，于是只好弃了）。

后端……暂时没有必要有后端。

## 构建开发环境

``` bash
# 安装依赖
$ npm install

# 运行服务器（有hot reload） ，默认地址localhost:8080
$ quasar dev

# 构建production版本
$ quasar build

# lint code
$ quasar lint

# 在ios上运行
$ ./runios.sh

# 在Android上运行
$ ./runandroid.sh

# 运行功能测试（兼具Demo效果）
$ python3 functional_test.py
```
---
# Priority Queue

This is a task management App.

The reason the author developed this App is because of his disorder of choice, often having no idea what to do first when there are multiple tasks in hand.

Hoping to help people who have the same problems as me.

Also want to have some great guys to give some advice & help me in developing this.

## Techs.
The frontend uses [quasar-framework](http://quasar-framework.org),which is a framework to build Hybrid and Web Apps。

Support Vue and its env. system, and [Cordova](http://cordova.apache.org) wrap it as an App。

（I used to use Weex,but its document is terrible，and its terrible support on web standard is driving me mad, there're to many limits!）

There's temporary no need to have a backend.

## Build a dev env

``` bash
# install dependencys
$ npm install

# run a dev server with hot reload on localhost:8080
$ quasar dev

# build for production
$ quasar build

# lint code
$ quasar lint

# run on ios
$ ./runios.sh

# run on Android
$ ./runandroid.sh

# functional test(can also be regarded as a demo)
$ python3 functional_test.py
```
