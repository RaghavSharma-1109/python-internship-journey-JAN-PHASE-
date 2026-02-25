class DatasetError(Exception):
    pass
class Dataset:
    def __init__(self,data) -> None:
        self.data = data
    @property
    def data(self):
        return self._data
    @data.setter
    def data(self,value):
        if not isinstance(value,list):
            raise DatasetError('Invalid Data Type')
        if len(value)==0:
            raise DatasetError('Data Can not be empty.')
        if not all(isinstance(x,(int,float)) for x in value):
            raise DatasetError('All elements must be numeric')
        self._data = value