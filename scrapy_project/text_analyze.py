import collections, re


def most_common(text):
    cleanr = re.compile("<script[^>]*>(.*?)</script[^>]*>")
    tags = re.compile("<.*?>")
    strings = re.compile("\\r | \\n | \\t | \\xa0")
    cleantext = re.sub(cleanr, '', str(text))
    cleantext = re.sub(tags,'',cleantext)
    cleantext = re.sub(strings, '', cleantext)
    #c = collections.Counter(text).most_common(1)
    return cleantext