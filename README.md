
# AnimalSounds

a python library to speak like snakes and bees.

## Install:

```
pip install animalsounds
```

## Example:

```
python snake.py 4
```

## Building Hints

```
conda create -n animalsounds -y python=3.12
conda activate animalsounds
pip install hatch
hatch clean
hatch build
hatch test
pip install dist/animalsounds-0.0.1-py3-none-any.whl
```

recompile, reinstall with same version
```
pip install dist/animalsounds-0.0.1-py3-none-any.whl --force-reinstall --no-deps
```

## Useful links:
https://git-scm.com/
https://pypi.org/
https://packaging.python.org/en/latest/tutorials/packaging-projects/
https://hatch.pypa.io
https://docs.python.org/3/library/__main__.html
https://docs.python.org/3/library/typing.html
https://docs.pytest.org
https://docs.python.org/3/library/argparse.html#module-argparse
https://docs.python.org/3/howto/argparse.html#argparse-tutorial
