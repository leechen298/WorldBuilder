import unittest

from publishing_word_count.counter import count_publishing_words


class PublishingWordCountTests(unittest.TestCase):
    def test_chinese_and_full_width_punctuation(self):
        text = "你好，世界。"
        self.assertEqual(count_publishing_words(text), 6)

    def test_ascii_letters_and_digits(self):
        text = "hello1234"
        self.assertEqual(count_publishing_words(text), 5)

    def test_mixed_content(self):
        text = "你好abc123"
        self.assertEqual(count_publishing_words(text), 5)

    def test_ignores_whitespace(self):
        text = "你 好\n\tabc"
        self.assertEqual(count_publishing_words(text), 4)

    def test_half_width_punctuation(self):
        text = "a,b.c!"
        self.assertEqual(count_publishing_words(text), 3)


if __name__ == "__main__":
    unittest.main()
