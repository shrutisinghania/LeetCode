class Codec:
    
    def __init__(self):
        self.d = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.d.keys():
            return self.d[longUrl]
        v = 'http://tinyurl.com/' + str(random.randint(0, 999999))
        self.d[v] = longUrl
        return v

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.d[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))