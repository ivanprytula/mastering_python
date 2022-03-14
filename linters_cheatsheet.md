## Use flake8
The error code of flake8 are E***, W*** used in pep8 and F*** and C9**.

E***/W***: Error and warning of pep8
F***: Detection of PyFlakes
C9**: Detection of circulate complexity by McCabe


```shell
flake8 <file_name.py>
```

```python
# flake8: noqa
```

## Use black
```shell
black <file_name.py> --check

# -S, --skip-string-normalization: Don't normalize string quotes or prefixes.
black <file_name.py> -S

#  --diff Don't write the files back, just output a
#                                  diff for each file on stdout.
# --color / --no-color            Show colored diff. Only applies when
#                                  `--diff` is given.
black --diff --color main.py
# Format all files in dir
black .
```
https://naereen.github.io/badges/
