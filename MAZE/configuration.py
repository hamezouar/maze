import sys
from typing import Any, Dict


def open_file_read(file_path: str) -> Dict[str, Any]:
    """
    Read a config file, validate required keys
    convert values to correct types, and return the configuration dictionary.
    """
    try:

        mandatory_keys = {
            'WIDTH', "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"
        }
        config: Dict[str, Any] = {}

        with open(file_path, "r") as file:
            for line in file.readlines():
                if line.startswith('#') or line.startswith('\n'):
                    continue
                key, value = line.split('=')
                key_strip = key.strip().upper()
                value_strip = value.strip()
                config[key_strip] = value_strip
            missing = mandatory_keys.difference(config)
            if missing:
                raise KeyError("you are missing keys : "
                               f"[{(', '.join(missing))}] "
                               "\n      📝  You should enter them")

            for key, value in config.items():
                if key in ('WIDTH', 'HEIGHT'):
                    int_value = int(value)
                    if int_value <= 0:
                        raise ValueError(
                            f"this value {value} must be a positive "
                            "integer or Greater than Zero")
                    elif int_value <= 8:
                        raise ValueError("this maze is "
                                         "small i can't raw 24 please "
                                         "change ('WIDTH', 'HEIGHT')")
                    config[key] = int_value
                elif key in ('ENTRY', 'EXIT'):
                    coord_x, coord_y = value.split(',')
                    coord_x = int(coord_x)
                    coord_y = int(coord_y)
                    if coord_x < 0 or coord_y < 0:
                        raise ValueError(
                            "ENTRY coordinates cannot be negative "
                            "Use values ≥ 0 for all entries")
                    config[key] = (coord_x, coord_y)

                elif key == 'PERFECT':
                    if value.lower() == 'true':
                        config[key] = True
                    elif value.lower() == 'false':
                        config[key] = False
                    else:
                        raise ValueError("PERFECT must be True or False")
                elif key == 'OUTPUT_FILE':
                    if not value:
                        raise ValueError("OUTPUT_FILE cannot be empty. "
                                         "You must provide a filename.")
            w, h = config['WIDTH'], config['HEIGHT']
            ex, ey = config['ENTRY']
            ox, oy = config['EXIT']
            if ex >= w or ey >= h:
                raise ValueError("ENTRY is outside maze bounds")
            if ox >= w or oy >= h:
                raise ValueError("EXIT is outside maze bounds")
            if config['ENTRY'] == config['EXIT']:
                raise ValueError("ENTRY and EXIT cannot be the same cell")
            if 'SEED' in config:
                int_value = int(value)
                config[key] = int_value
            else:
                config['SEED'] = None
            return config
    except Exception as e:
        print(f" ⚠️  Error: {e.args[0]}")
        print("      🛠️   Please fix your configuration file")
        sys.exit(1)
