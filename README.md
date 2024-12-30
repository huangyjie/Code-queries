# 代码行数统计工具

这是一个用Python编写的代码行数统计工具，可以统计项目中不同编程语言的代码行数，支持多种编程语言，并能自动过滤注释和空行。

## 功能特点

- 支持超过60种编程语言和文件类型的统计
- 自动排除常见的构建目录和二进制文件
- 特别支持微信小程序相关文件的统计
- 智能过滤测试文件和编译后的文件
- 支持UTF-8编码的文件读取
- 支持通过命令行参数指定要统计的目录
- 支持详细的文件列表输出
- 支持文件大小和修改时间统计
- 支持自定义忽略规则（.codeignore）
- 自动生成统计日志文件
- 跨平台支持（Windows/Linux/macOS）

## 系统要求

- Python 3.6 或更高版本
- 不需要额外的依赖包

## 使用方法

### 基本用法

```bash
# 统计当前目录
python code_counter.py

# 统计指定目录
python code_counter.py /path/to/your/code

# 显示详细信息（包含文件列表）
python code_counter.py -d /path/to/your/code

# 显示帮助信息
python code_counter.py --help
```

### 交互式使用

```bash
python code_counter.py
> 请输入要统计的目录路径（直接回车则统计当前目录）：
> /path/to/your/code
```

### 命令行参数

- `-h, --help`: 显示帮助信息
- `-d, --detailed`: 显示详细的文件列表
- `[目录路径]`: 要统计的目录路径（可选）

## 输出示例

```
代码统计结果 - 2024-03-21 15:30:45
统计目录: /path/to/your/code

总体统计
============================================================
总代码行数:         1234
文件总数:            56
总大小:          2.34MB

语言统计
============================================================
语言                    行数      文件数         大小
------------------------------------------------------------
Python                  500          8       256.5KB
JavaScript              300          5       150.2KB
CSS                     200          4        98.6KB
HTML                    150          3        45.8KB
微信模板                 80          2        25.4KB
微信样式                 60          2        18.7KB
------------------------------------------------------------

详细文件列表
====================================================================================================
文件路径                                                    大小        修改时间
----------------------------------------------------------------------------------------------------
src/main.py                                              12.5KB    2024-03-21 15:30:45
src/utils/helper.py                                       8.2KB    2024-03-21 15:28:30
...
```

## 配置说明

### .codeignore 文件

您可以在项目根目录创建 `.codeignore` 文件来自定义要忽略的文件和目录：

```
# 忽略所有日志文件
*.log

# 忽略特定目录
temp/
build/
dist/
node_modules/
__pycache__/

# 忽略特定文件
config.json
*.min.js
*.pyc
```

支持的通配符：
- `*`: 匹配任意字符（除了路径分隔符）
- `**`: 匹配任意目录层级
- `?`: 匹配单个字符
- `[abc]`: 匹配方括号中的任意字符
- `!`: 排除模式

## 支持的文件类型

### 常见编程语言
- Python (.py)
- JavaScript (.js)
- Java (.java)
- C/C++ (.c, .cpp, .h)
- C# (.cs)
- Go (.go)
- Rust (.rs)
- Ruby (.rb)
- PHP (.php)
- Swift (.swift)
- Kotlin (.kt)
- TypeScript (.ts)

### Web开发
- HTML (.html)
- CSS (.css)
- Vue (.vue)
- React (.jsx, .tsx)
- Sass/SCSS (.sass, .scss)
- Less (.less)

### 移动开发
- Swift (.swift)
- Kotlin (.kt)
- Objective-C (.m, .mm)
- Dart (.dart)

### 微信小程序
- WXML (.wxml)
- WXSS (.wxss)
- WXS (.wxs)

### 配置和标记语言
- YAML (.yml, .yaml)
- JSON (.json)
- TOML (.toml)
- XML (.xml)
- Markdown (.md)
- Protocol Buffers (.proto)

### 其他语言
- Shell (.sh)
- PowerShell (.ps1)
- Batch (.bat, .cmd)
- SQL (.sql)
- GraphQL (.graphql, .gql)
- R (.r)
- Matlab (.m)
- Perl (.pl)
- Lua (.lua)

## 自动排除的内容

### 目录
- 构建目录：build/, dist/, target/
- 依赖目录：node_modules/, venv/, vendor/
- IDE配置：.idea/, .vscode/, .vs/
- 缓存目录：__pycache__/, .cache/
- 版本控制：.git/, .svn/

### 文件
- 编译文件：*.pyc, *.exe, *.dll
- 压缩文件：*.min.js, *.min.css
- 日志文件：*.log
- 临时文件：*.tmp, *.temp
- 备份文件：*.bak, *.backup
- 测试文件：*test.*, *spec.*

## 注意事项

- 统计时只计算非空行和非注释行
- 自动跳过二进制文件和不可读文件
- 日志文件保存在 `logs` 目录下
- 支持 UTF-8 编码的文件
- 大文件和特殊编码文件可能会被跳过
- 建议在统计大型项目时使用 .codeignore 配置

## 常见问题

1. **为什么某些文件没有被统计？**
   - 检查文件是否在排除列表中
   - 确认文件编码是否为 UTF-8
   - 查看是否被 .codeignore 规则排除

2. **如何统计指定类型的文件？**
   - 使用 .codeignore 排除不需要的文件类型
   - 查看支持的文件类型列表

3. **统计结果中出现乱码？**
   - 确保文件为 UTF-8 编码
   - 检查终端是否支持中文显示

## 许可证

MIT License

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进这个工具。

1. Fork 本仓库
2. 创建您的特性分支
3. 提交您的改动
4. 推送到您的分支
5. 创建 Pull Request