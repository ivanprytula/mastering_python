import inspect

from snake_path.assets.exercises.get_zen import get_zen

source_code_string = inspect.getsource(get_zen)

print(source_code_string)
