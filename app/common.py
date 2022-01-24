import datetime
import json


def timeit(func):
    date_time = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S:%f")
    print('Endpoint handler function {} request at \033[92m{}\033[0m\n'.format(func.__name__.upper(), date_time))


class DbHandler(object):

    def __init__(self, path: str):
        self._path = path
        assert path.endswith('json'), f'Expected json file path, got instead {path}'
        self._content = None

    def _read_content(self):
        with open(self._path, 'r') as _fp:
            self._content = json.load(_fp)

    def _write_content(self, new_item):
        self._content.append(new_item)
        with open(self._path, 'w') as _fp:
            json.dump(self._content, _fp, indent=4)
            self._content = None

    @property
    def content(self) -> list[dict]:
        """Return the file content as a parsed native python object"""
        self._read_content()
        # if self._content is None: self._read_content()
        return self._content

    @property
    def _last_id(self) -> int:
        """Return current number of records in the file"""
        return len(self.content)

    def retrieve_data(self) -> list:
        """
    Read the file data, parse into python object and return it
        """
        return self.content

    def send_data(self, dict_ob: dict) -> dict:
        """
    Write new company items to the file
        """
        assert type(dict_ob) is dict, f'Expected dict object, got instead {type(dict_ob)}'
        new_item_id = dict(id=self._last_id + 1)
        dict_ob.update(new_item_id)  # set the record id field
        self._write_content(dict_ob)
        return new_item_id


if __name__ == '__main__':
    print('Hi, This is Python')
