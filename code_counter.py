import os
import sys
from collections import defaultdict

def count_lines_by_extension(directory='.'):
    """
    统计指定目录下各种编程语言的代码行数
    
    Args:
        directory (str): 要统计的目录路径，默认为当前目录
    """
    # 只保留项目源代码相关的文件类型
    extension_map = {
        '.c': 'C',
        '.cpp': 'C++',
        '.h': 'C/C++ Header',
        '.py': 'Python',
        '.js': 'JavaScript',
        '.java': 'Java',
        '.css': 'CSS',
        # 微信小程序相关文件类型
        '.wxml': '微信模板',
        '.wxss': '微信样式',
        '.wxs': '微信脚本',
        
        # 添加更多编程语言
        '.cs': 'C#',
        '.go': 'Go',
        '.rs': 'Rust',
        '.rb': 'Ruby',
        '.php': 'PHP',
        '.swift': 'Swift',
        '.kt': 'Kotlin',
        '.ts': 'TypeScript',
        '.jsx': 'React JSX',
        '.tsx': 'React TSX',
        '.vue': 'Vue',
        '.scala': 'Scala',
        '.dart': 'Dart',
        '.r': 'R',
        '.m': 'Objective-C',
        '.mm': 'Objective-C++',
        '.sql': 'SQL',
        '.sh': 'Shell',
        '.ps1': 'PowerShell',
        '.lua': 'Lua',
        '.pl': 'Perl',
        '.ex': 'Elixir',
        '.exs': 'Elixir Script',
        '.elm': 'Elm',
        '.fs': 'F#',
        '.coffee': 'CoffeeScript',
        '.sass': 'Sass',
        '.scss': 'SCSS',
        '.less': 'Less',
        '.tf': 'Terraform',
        '.yaml': 'YAML',
        '.yml': 'YAML',
        '.json': 'JSON',
        '.proto': 'Protocol Buffers',
        # 添加更多文件类型
        '.asm': '汇编语言',
        '.s': '汇编语言',
        '.f90': 'Fortran',
        '.f95': 'Fortran',
        '.f': 'Fortran',
        '.for': 'Fortran',
        '.pas': 'Pascal',
        '.pp': 'Pascal',
        '.inc': 'Pascal',
        '.bas': 'Basic',
        '.vb': 'Visual Basic',
        '.vbs': 'VBScript',
        '.clj': 'Clojure',
        '.cljc': 'Clojure',
        '.cljs': 'ClojureScript',
        '.erl': 'Erlang',
        '.hrl': 'Erlang',
        '.hs': 'Haskell',
        '.lhs': 'Haskell',
        '.ml': 'OCaml',
        '.mli': 'OCaml',
        '.groovy': 'Groovy',
        '.gvy': 'Groovy',
        '.gradle': 'Gradle',
        '.tcl': 'Tcl',
        '.asp': 'ASP',
        '.aspx': 'ASP.NET',
        '.cshtml': 'Razor',
        '.vbhtml': 'Razor',
        '.jsp': 'JSP',
        '.jspx': 'JSP',
        '.php4': 'PHP',
        '.php5': 'PHP',
        '.phtml': 'PHP',
        '.nim': 'Nim',
        '.cr': 'Crystal',
        '.d': 'D',
        '.v': 'Verilog',
        '.vhd': 'VHDL',
        '.sv': 'SystemVerilog',
        '.pro': 'Prolog',
        '.pl': 'Prolog',
        '.cmake': 'CMake',
        '.dockerfile': 'Dockerfile',
        '.jenkins': 'Jenkins',
        '.bat': 'Batch',
        '.cmd': 'Batch',
        '.ino': 'Arduino',
        '.pde': 'Processing',
        '.sol': 'Solidity',
        '.nix': 'Nix',
        '.dhall': 'Dhall',
        '.graphql': 'GraphQL',
        '.gql': 'GraphQL',
        '.hcl': 'HCL',
        '.toml': 'TOML',
        '.ini': 'INI'
    }
    
    # 需要排除的目录
    exclude_dirs = {
        'node_modules',
        'venv',
        'env',
        '__pycache__',
        'dist',
        'build',
        'lib',
        'libs',
        'vendor',
        'packages',
        '.idea',           # IDE配置目录
        '.vs',            # Visual Studio配置目录
        'ipch',           # Visual Studio智能感知缓存
        'FileContentIndex', # VS文件索引
        'Debug',          # 调试输出目录
        'Release',        # 发布输出目录
        'x64',           # 64位输出目录
        'x86',           # 32位输出目录
        '.git',          # Git版本控制目录
        '.svn',          # SVN版本控制目录
        '.hg',           # Mercurial版本控制目录
        '.tox',          # Tox测试环境目录
        '.pytest_cache', # Pytest缓存目录
        '.mypy_cache',   # MyPy缓存目录
        '.coverage',     # 覆盖率报告目录
        '.vscode',       # VSCode配置目录
        '.DS_Store',     # macOS系统文件
        '__MACOSX',      # macOS压缩文件目录
        'target',         # Maven/Rust构建目录
        'out',           # 通用输出目录
        'bin',           # 二进制文件目录
        'obj',           # .NET构建目录
        'tmp',           # 临时文件目录
        'temp',          # 临时文件目录
        'cache',         # 缓存目录
        'logs',          # 日志目录
        'coverage',      # 测试覆盖率目录
        '.next',         # Next.js构建目录
        '.nuxt',         # Nuxt.js构建目录
        'public/build',  # 前端构建目录
        '.sass-cache',   # Sass缓存目录
        '.gradle',       # Gradle构建目录
        'gradle',        # Gradle包装器目录
        '.cargo',        # Rust Cargo缓存
        'migrations',    # 数据库迁移文件
        'fixtures',      # 测试数据文件
        'assets',        # 静态资源目录
        'docs',          # 文档目录
    }
    
    # 需要排除的文件类型
    exclude_extensions = {
        '.exe', '.dll', '.so', '.dylib',  # 二进制文件
        '.xml', '.txt', '.md', '.rst',    # 文档和配置文件
        '.pyc', '.pyo', '.pyd',           # Python编译文件
        '.min.js', '.min.css',            # 压缩文件
        '.test.js', '.spec.js',           # 测试文件
        '.log', '.lock', '.map',          # 其他工具文件
        '.vsidx',        # VS索引文件
        '.ipch',         # VS智能感知缓存
        '.suo',          # VS用户选项文件
        '.db',           # 数据库文件
        '.cache',        # 缓存文件
        '.gitignore',    # git配置文件
        '.iml',          # IntelliJ IDEA模块文件
        '.swp',          # Vim临时文件
        '.tmp',          # 临时文件
        '.bak',          # 备份文件
        '.old',          # 旧文件
        '.orig',         # 原始文件
        '.pdf', '.doc', '.docx',  # 文档文件
        '.xls', '.xlsx',          # Excel文件
        '.ppt', '.pptx',          # PPT文件
        '.zip', '.rar', '.7z',    # 压缩文件
        '.tar', '.gz', '.bz2',    # 压缩文件
        '.png', '.jpg', '.jpeg',  # 图片文件
        '.gif', '.svg', '.ico',   # 图片文件
        '.mp3', '.mp4', '.avi',   # 媒体文件
        '.wav', '.flac', '.ogg',  # 音频文件
        '.ttf', '.woff', '.eot',  # 字体文件
        '.woff2', '.otf',         # 字体文件
        '.env',                   # 环境配置文件
        '.config',                # 配置文件
        '.conf',                  # 配置文件
        '.properties',            # 属性文件
        '.d.ts',                  # TypeScript声明文件
        '.min.map',              # Source map文件
        '.sum',                  # Go模块校验和
        '.mod',                  # Go模块文件
        '.pb.go',               # Protocol Buffers生成文件
        '.generated.*',         # 自动生成的文件
        '.g.dart',             # Flutter生成的文件
        '.freezed.dart',       # Freezed生成的文件
        '.mock.ts',            # 测试模拟文件
        '.stub.php',           # 测试桩文件
    }
    
    # 需要排除的文件名
    exclude_filenames = {
        'package-lock.json',
        'yarn.lock',
        'pnpm-lock.yaml',
        'composer.lock',
        'Gemfile.lock',
        'poetry.lock',
        'Cargo.lock',
        'go.sum',
        '.eslintrc',
        '.prettierrc',
        '.editorconfig',
        '.browserslistrc',
        'tsconfig.json',
        'jest.config.js',
        'babel.config.js',
        'webpack.config.js',
        'rollup.config.js',
        'vite.config.js',
        'next.config.js',
        'nuxt.config.js',
        'tailwind.config.js',
        'postcss.config.js',
        'karma.conf.js',
        'Dockerfile',
        'docker-compose.yml',
        'Makefile',
        'Rakefile',
        'Jenkinsfile',
    }
    
    # 用于存储每种语言的行数
    language_counts = defaultdict(int)
    
    # 注释标记
    single_line_comment_markers = {
        '.py': '#',
        '.js': '//',
        '.java': '//',
        '.c': '//',
        '.cpp': '//',
        '.cs': '//',
        '.go': '//',
        '.rs': '//',
        '.rb': '#',
        '.php': '//',
        '.swift': '//',
        '.kt': '//',
        '.ts': '//',
        '.jsx': '//',
        '.tsx': '//',
        '.scala': '//',
        '.dart': '//',
        '.r': '#',
        '.sh': '#',
        '.ps1': '#',
        '.lua': '--',
        '.pl': '#',
        '.ex': '#',
        '.exs': '#',
        '.elm': '--',
        '.fs': '//',
        '.coffee': '#',
        '.sass': '//',
        '.scss': '//',
        '.less': '//',
        '.tf': '#',
        '.yaml': '#',
        '.yml': '#',
        '.json': '//',
        '.proto': '//',
        '.asm': ';',
        '.s': ';',
        '.f90': '!',
        '.f95': '!',
        '.f': '!',
        '.for': '!',
        '.pas': '//',
        '.pp': '//',
        '.inc': '//',
        '.bas': "'",
        '.vb': "'",
        '.vbs': "'",
        '.clj': ';',
        '.cljc': ';',
        '.cljs': ';',
        '.erl': '%',
        '.hrl': '%',
        '.hs': '--',
        '.lhs': '--',
        '.ml': '(*',
        '.mli': '(*',
        '.groovy': '//',
        '.gvy': '//',
        '.gradle': '//',
        '.tcl': '#',
        '.asp': "'",
        '.aspx': "'",
        '.cshtml': '@*',
        '.vbhtml': '@*',
        '.jsp': '<%--',
        '.jspx': '<%--',
        '.php4': '//',
        '.php5': '//',
        '.phtml': '//',
        '.nim': '#',
        '.cr': '#',
        '.d': '//',
        '.v': '//',
        '.vhd': '--',
        '.sv': '//',
        '.pro': '%',
        '.pl': '%',
        '.cmake': '#',
        '.dockerfile': '#',
        '.jenkins': '#',
        '.bat': 'REM',
        '.cmd': 'REM',
        '.ino': '//',
        '.pde': '//',
        '.sol': '//',
        '.nix': '#',
        '.dhall': '--',
        '.graphql': '#',
        '.gql': '#',
        '.hcl': '#',
        '.toml': '#',
        '.ini': ';'
    }
    
    # 遍历指定目录及其子目录
    for root, dirs, files in os.walk(directory):
        # 移除所有以点开头的目录和需要排除的目录
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in exclude_dirs]
            
        for file in files:
            # 跳过以点开头的文件
            if file.startswith('.'):
                continue
                
            # 跳过指定的文件名
            if file in exclude_filenames:
                continue
                
            # 获取文件扩展名
            ext = os.path.splitext(file)[1].lower()
            
            # 跳过需要排除的文件类型
            if ext in exclude_extensions:
                continue
                
            # 跳过测试文件
            if 'test' in file.lower() or 'spec' in file.lower():
                continue
                
            if ext in extension_map:
                try:
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = 0
                        for line in f:
                            stripped_line = line.strip()
                            if not stripped_line:
                                continue
                            if ext in single_line_comment_markers and stripped_line.startswith(single_line_comment_markers[ext]):
                                continue
                            lines += 1
                        language_counts[extension_map[ext]] += lines
                except:
                    # 如果文件无法读取，跳过该文件
                    continue

    # 打印结果
    print("\n代码统计结果:")
    print("-" * 40)
    print(f"{'语言':<15}{'行数':>10}")
    print("-" * 40)
    
    # 首先打印微信小程序相关的统计
    wx_categories = ['微信模板', '微信样式', '微信脚本']
    for category in wx_categories:
        if language_counts[category] > 0:
            print(f"{category:<15}{language_counts[category]:>10}")
            
    # 然后打印其他语言的统计
    for language, count in sorted(language_counts.items()):
        if language not in wx_categories:  # 跳过已经打印的微信相关类别
            print(f"{language:<15}{count:>10}")
    
    total_lines = sum(language_counts.values())
    print("-" * 40)
    print(f"{'总计':<15}{total_lines:>10}")

def print_usage():
    """打印使用说明"""
    print("""
代码行数统计工具

用法:
    python code_counter.py [目录路径]

参数:
    目录路径    可选，要统计的目录路径，默认为当前目录

示例:
    python code_counter.py                 # 统计当前目录
    python code_counter.py /path/to/code   # 统计指定目录
    """)

def get_directory_input():
    """获取用户输入的目录路径"""
    print("\n请输入要统计的目录路径（直接回车则统计当前目录）：")
    path = input().strip()
    return path if path else '.'

if __name__ == '__main__':
    try:
        # 获取命令行参数
        if len(sys.argv) > 2:
            print("错误：参数过多")
            print_usage()
            sys.exit(1)
        
        if len(sys.argv) == 2:
            if sys.argv[1] in ['-h', '--help']:
                print_usage()
                sys.exit(0)
            directory = sys.argv[1]
        else:
            # 如果没有命令行参数，通过交互方式获取目录
            directory = get_directory_input()
        
        # 验证目录是否有效
        if not os.path.exists(directory):
            print(f"错误：目录 '{directory}' 不存在")
            sys.exit(1)
        if not os.path.isdir(directory):
            print(f"错误：'{directory}' 不是一个目录")
            sys.exit(1)
        
        # 执行统计
        count_lines_by_extension(directory)
        
    except KeyboardInterrupt:
        print("\n统计被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n发生错误：{str(e)}")
        sys.exit(1) 