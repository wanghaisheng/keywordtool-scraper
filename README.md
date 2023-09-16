# keywordtool-scraper
Exposes a basic API to search using keywordtool.io. That search uses autosuggest from various search engines to complete a base phrase.



based on flybirds 



# Installation
Navigate to any directory using your root/system conda and run the following commands:
```bash
git clone https://github.com/quantum-programmer/keywordtool-scraper.git
conda build keywordtool-scraper -c conda-forge -c r
```

**(OPTIONAL)** Remove unnecessary build files with
```bash
conda build purge
```

**(OPTIONAL)** Activate the environment in which you wish to install `keywordtool-scraper`:
```bash
source activate my_environment
```

To actually install the package, run
```bash
conda install keywordtool-scraper -c conda-forge -c r --use-local
```

Note: If I ever add support for a modern alternative to PhantomJS (like Headless Chrome), I'll add this to the Anaconda Cloud. Feel free to contribute/fork as desired.


# Basic Usage
The interface is a `KeywordTool` object with several helper methods/properties.
```python
import keywordtool

kt = keywordtool.KeywordTool(source='google', timeout=5)  # kwargs are optional
keywords = kt.get_keywords('florida man arrested')
```

# Example Usage
The usage doesn't get too crazy. What follows is a more-or-less comprehensive demonstration of the capabilities. Feel free to run and experiment with the code to get a feel for how it works.
```python
import keywordtool

kt = keywordtool.KeywordTool(source='google', timeout=5)  # kwargs are optional

print 'Current URL: %s\n' % kt.current_url
print 'There are %d search engines to choose from:' % len(kt.sources)
for s in kt.sources:
    print '   %s' % s

kt.timeout = 10
kt.source = 'bing'
arrested_keywords = kt.get_keywords('florida man arrested')
print '\nHeadlines from Florida include "%s"' % arrested_keywords[0].upper()

book_keywords = kt.get_keywords('good books', source='amazon')
print '\nPeople on Amazon are searching for "%s"' % book_keywords[0]
```

**(IMPORTANT)** The `source` kwarg **silently defaults** to `'google'` if the provided argument is invalid. Available options for the `source` kwarg are
* `'amazon'`
* `'app-store'`
* `'bing'`
* `'ebay'`
* `'google'`
* `'youtube'`
