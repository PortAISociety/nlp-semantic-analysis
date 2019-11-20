import urllib.request
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
import nltk
import operator


# Get HTML document from URL
# returns HTML file string
def getPage(url: str):
    response = urllib.request.urlopen(url)
    return response.read()


# Cleanup HTML to just get the text
# pip install beautifulsoup4
# pip install html5lib
def toSoup(html):
    soup = BeautifulSoup(html, 'html5lib')
    return soup.get_text(strip=True)


# Count the frequency of tokens within the page
# Returns first X most frequent tokens
# pip install nltk
def countWords(tokens, num_to_get):
    # Remove 'stopwords' from the page - words such as 'and', 'the', etc;
    sr = stopwords.words('english')
    clean_tokens = tokens[:]
    for token in tokens:
        if token in sr:
            clean_tokens.remove(token)

    # Use the NLTK to return a dictionary of the token and the number of occurrences
    freq = nltk.FreqDist(clean_tokens)
    items = freq.items()

    # Sort the dictionary by the number of occurrences, in descending order
    sorted_items = sorted(items, key=operator.itemgetter(1))
    sorted_items.reverse()

    # Add the X most common words to a list
    ret = []
    sorted_list = list(sorted_items)
    for i in range(num_to_get):
        ret.append(sorted_list[i])

    # Return that list
    return ret


if __name__ == '__main__':
    # Print out HTML page, with HTML included
    html = getPage('https://en.wikipedia.org/wiki/Tesla,_Inc.')

    # Cleanup HTML to just get the text
    text = toSoup(html)

    # Convert text into tokens
    tokens = [t for t in text.split()]

    # Count the frequency of words
    words = countWords(tokens, 10)
    for key, val in words:
        print(str(key) + ': ' + str(val))

    # Print statement about what the page is about
    print("\nI'm thinking that this page is about " + str(words[0][0]) + ".")
