# ShortURL

![](https://raw.githubusercontent.com/DavidJacobson/ShortURL/master/main.PNG)

## Setup
To use the URL shortening service, you are going to need an API key. This is easy to obtain.
Go to [this url](http://www.tiny-url.info/request_api_key.html) and request a key. Once you have it, write it down and register it.

Next you need to save the key as an environment variable:

```shell
python main.py http://google.com --apikey yourkeyhere
```

You should get a message saying your key was saved successfully. 

##Usage

To use ShortURL just type:

```shell
python main.py http://YourURLHere.TLD
http://bit.ly/2BAlDhS
```

You can choose which URL shortening service you would like to use with the --provider option.

By default ShortURL will use bit.ly. I would recommend sticking with bit.ly. 

A full list of choices is available [here](http://www.tiny-url.info/open_api.html#provider_list)

```shell
python main.py http://google.com --provider tiny_cc
```

If you get an error, your API key has likely expired.

```shell
python main.py http://google.com
An error occured
```
Return to http://www.tiny-url.info/request_api_key.html, request a new key, and run:
```shell
python main.py LastUrl --apikey NewKey
```

To confirm that the API key has updated, check the environment:
```shell
Windows:
SET short_apikey
*Nix:
printenv
``` 

To manually replace the API key, use:

```shell
Windows:
SETX short_apikey YourNewKey

*Nix
export short_apikey=YourNewKey
```


