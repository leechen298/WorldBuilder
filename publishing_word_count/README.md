# Publishing Word Count

规则（常见中文出版统计口径）：

- 全角字符（中文、全角标点等）每个算 1 字。
- 半角字符（英文、数字、半角符号等）每 2 个算 1 字（向上取整）。
- 空白字符（空格、换行、制表符）不计入。

## Usage

```python
from publishing_word_count import count_publishing_words

count = count_publishing_words("你好abc123")
print(count)  # 5
```

运行测试：

```bash
python -m unittest discover -s publishing_word_count/tests
```
