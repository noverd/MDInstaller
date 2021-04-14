from path_save import paths_steam


def add_path_steam(steam_path,name_game, path):
    paths_steam.append({name_game: steam_path+path})
    f = open('path_save.py', 'w')
    f.write(f"paths_steam = {paths_steam}")

