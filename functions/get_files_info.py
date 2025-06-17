import os

def get_files_info(working_directory, directory=None):
    try:
        if directory is None:
            directory = working_directory

        abs_working_dir = os.path.abspath(working_directory)
        abs_target_dir = os.path.abspath(os.path.join(working_directory, directory))

        if not abs_target_dir.startswith(abs_working_dir):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(abs_target_dir):
            return f'Error: "{directory}" is not a directory'

        items = []
        for item in os.listdir(abs_target_dir):
            item_path = os.path.join(abs_target_dir, item)
            try:
                size = os.path.getsize(item_path)
                is_dir = os.path.isdir(item_path)
                items.append(f'- {item}: file_size={size} bytes, is_dir={is_dir}')
            except Exception as e:
                return f'Error: Could not access "{item}": {str(e)}'

        return '\n'.join(items)

    except Exception as e:
        return f'Error: {str(e)}'