import re

class MarkdownEngine:
    def parse(self, text):
        text = re.sub(r'^# (.*)$', r'<h1>\1</h1>', text, flags=re.M)
        text = re.sub(r'^## (.*)$', r'<h2>\1</h2>', text, flags=re.M)
        text = re.sub(r'\*\*(.*)\*\*', r'<b>\1</b>', text)
        text = re.sub(r'\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', text)
        return text

if __name__ == "__main__":
    engine = MarkdownEngine()
    sample = "# Hello Buddy\nThis is **bold** and here is a [link](https://python.org)"
    
    print("📝 Markdown Input:")
    print(sample)
    print("\n🌐 HTML Output:")
    print(engine.parse(sample))
