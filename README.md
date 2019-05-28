[![version](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg)](https://img.shields.io/badge/python-3.6%20%7C%203.7-blue.svg)
[![travis build status](https://travis-ci.org/duckling-python-wrapper/fb_duckling.svg?branch=master)](https://travis-ci.org/duckling-python-wrapper/fb_duckling)
[![Coverage Status](https://coveralls.io/repos/github/duckling-python-wrapper/fb_duckling/badge.svg?branch=master)](https://coveralls.io/github/duckling-python-wrapper/fb_duckling?branch=master)

# fb_duckling

A python wrapper for **[facebook's duckling](https://github.com/facebook/duckling)**.

## Installation:

1. Installation of Duckling.
Set the environment properly to reach your duckling server.
Facebook's Duckling is a library used for feature extraction in text, and it is coded in haskell.
To make it work, you need to
   - Install [haskell](https://www.haskell.org/platform/) to your platform.
   - Clone [facebook's duckling](https://github.com/facebook/duckling).
   - Install the project using ```stack build``` from duckling's project root.
 
2. Start Duckling.
   - Launch the duckling-server with the command ```stack exec duckling-example-exe```.
 
3. Install the library on python3
   - On **python3.6** or **python3.7** use the command ```pip install fb-duckling```.
   
## Using the Library

```python
from fb_duckling import Duckling
duckling = Duckling(locale="en_US")
duckling("All work and no play makes jack@gmail.com a dull boy 0102030405")

```
```bash
{
    'body': 'jack@gmail.com',
    'start': 6,
    'value': {'value': 'jack@gmail.com'},
    'end': 20,
    'dim': 'email',
    'latent': False
}
 ```
