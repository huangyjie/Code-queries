# 代码行数统计工具

这是一个用Python编写的代码行数统计工具，可以统计项目中不同编程语言的代码行数。

## 功能特点

- 支持超过60种编程语言和文件类型的统计
- 自动排除常见的构建目录和二进制文件
- 特别支持微信小程序相关文件的统计
- 智能过滤测试文件和编译后的文件
- 支持UTF-8编码的文件读取
- 支持通过命令行参数指定要统计的目录

## 使用方法

1. 确保您的系统已安装Python 3.x

2. 安装依赖包：
   
   ```bash
   pip install -r requirements.txt
   ```

3. 运行脚本：
   
   ```bash
   # 方式1：命令行参数指定目录
   python code_counter.py /path/to/your/code
   
   # 方式2：交互式输入
   python code_counter.py
   > 请输入要统计的目录路径（直接回车则统计当前目录）：
   > /path/to/your/code
   
   # 显示帮助信息
   python code_counter.py --help
   ```

## 支持的文件类型

包括但不限于：

- 常见编程语言：Python, Java, C/C++, JavaScript等
- 微信小程序：WXML, WXSS, WXS
- Web开发：HTML, CSS, Vue, React等
- 移动开发：Swift, Kotlin, Objective-C等
- 配置文件：YAML, JSON, TOML等

## 排除规则

自动排除以下内容：

- 构建目录：node_modules, venv, dist等
- IDE配置目录：.idea, .vs等
- 编译文件：.pyc, .exe, .dll等
- 测试文件：包含test或spec的文件
- 压缩文件：.min.js, .min.css等

## 输出格式

代码统计结果:
----------------------------------------

语言         行数
----------------------------------------

----------------------------------------

Python                100
JavaScript           200
CSS                      150

----------------------------------------

总计 450

## 注意事项

- 统计时只计算非空行
- 如果文件无法读取会自动跳过
- 默认使用UTF-8编码读取文件

## 许可证

MIT License