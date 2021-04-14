from path_save import paths_steam


def add_path_steam(name_game, path):
    paths_steam.append({name_game: path})
    f = open('path_save.py', 'w')
    f.write(f"paths_steam = {paths_steam}")

