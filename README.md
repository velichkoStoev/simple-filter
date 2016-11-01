# simple-filter

Simple filter is a small Python script that applies basic filters to your image.  

Available filters:
- grayscale
- luminance
- desaturation
- min_decomposition
- max_decomposition

![](http://i.imgur.com/En6iQGq.jpg)

## Install
1. *(optional)* Consider using  [virtualenv](https://virtualenv.pypa.io/en/stable/) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).
2. Install [Pillow](https://python-pillow.org/) by running `pip install Pillow`.

## Execute
```python simple_filter.py -p ~/path/to/img -f the-name-of-the-filter```

or 

```python simple_filter.py --path=~/path/to/img --filter=the-name-of-the-filter```

#### See the help output
`python simple_filter.py -h` or `python simple_filter.py --help`

