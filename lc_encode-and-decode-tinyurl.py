class Codec:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        coded = ''
        for ch in longUrl:
            coded += str(ord(ch)) + '_'
        return coded
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        decoded = ''
        shortUrl = shortUrl.split('_')
        for i in shortUrl:
            if i.isdigit():
                decoded += chr(int(i))
        return decoded

