# keywordtool-scraper
Exposes a basic API to search using keywordtool.io. That search uses autosuggest from various search engines to complete a base phrase.

# Usage
```python
import keywordtool

keywords = keywordtool.get_keywords('my search term', source='google', timeout=5)
```

The `source` kwarg **silently defaults** to `'google'` if the provided argument is invalid. Available options for the `source` kwarg are
* `'amazon'`
* `'app-store'`
* `'bing'`
* `'ebay'`
* `'google'`
* `'youtube'`
