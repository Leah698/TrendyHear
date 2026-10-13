# 原生行为验证

`decisions-0.9.1.splash` 在正式脚本上只替换启动回调，使用手工构造的活动、用户背景和模型返回值。它调用正式校验/存储函数，不调用真实模型，不证明真实生成质量。

执行：`python3 tests/run_native_checks.py --octo /path/to/tools/octo`。使用隔离临时目录和参考card-host，只移除测试清单的agent/requires以运行本地检查；不改变正式包或用户数据。退出本次启动的窗口后打印结果。需要已经构建的官方工具。
