class Comment:
    def __init__(self, username, text, likes):
        self.username = username
        self.text = text
        self.likes = likes

c = Comment("davey123", "lol you're so silly", 3)
print(c.username)
print(c.text)
print(c.likes)