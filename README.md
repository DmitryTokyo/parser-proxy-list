# Parser [spy.one](http://spys.one/proxies/)

Parse proxies from the `free-proxy-list` by country, and get list of proxies in the json file.

## Environment and installation

Script on `Python 3.8.1`

For install requirements by using follow command:

```bash
pip install -r requirements.txt
```

Before run the script need to download Selenuim webdriver. In curent script was choosing the [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads) webdriver. The others driver available on the official [Selenuim](https://selenium-python.readthedocs.io/installation.html) page.
If will choose an another driver then need to change the script (activate downloaded driver instead Chrome):

```python
driver = webdriver.Chrome(executable_path = env('PATH_TO_DRIVER'))
```

The project has 2 environments variable:

`PATH_TO_DRIVER` - full path to driver.
`PROXY_FILE` - name of output json file.

## Usage

Parser can run following command:

```bash
pip proxies_scrappy.py
```

## Data output

All free proxies save to the json file in the folowing form:

```json
{
    "Germany": [
        "1.1.2.3:1080",
        "4.4.5.5:3128",
        "6.6.7.7:3129",
        ...,
    ]
}
```

## Contact

if you have any questions about this repo, please send email (from the my profile)