import os


class PathView:
    """
    Проверка путей
    """

    def __init__(self, path, search_dir):
        self.path = path
        self.search_dir = search_dir

    def go_search(self):
        """
        Работа по поиску
        """
        os.chdir(self.path)
        list_dir = os.listdir()
        path = os.getcwd()
        for main_dir in list_dir:
            self.path = f"{path}/{main_dir}"
            if main_dir == self.search_dir:
                print(self.path)
            self.go_search()


search = PathView(path="./tree", search_dir="python")
search.go_search()
