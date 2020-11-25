class Data:
    data: str

    def __init__(self, data):
        self.data = data

    @classmethod
    def split_data(cls, data):
        data_lst = data.split('-')
        day = int(data_lst[0])
        month = int(data_lst[1])
        year = int(data_lst[2])
        return day, month, year

    @staticmethod
    def data_validation(content):
        day, month, year = Data.split_data(content)
        assert 1 <= month <= 12
        assert year >= 0
        assert day >= 1
        if month == 2:
            if year % 4 == 0:
                assert day <= 29
            else:
                assert day <= 28
        elif month in (1, 3, 5, 7, 8, 10, 12):
            assert day <= 31
        else:
            assert day <= 30
        return print('Validation passed')


data1 = '12-03-2020'
print(Data.split_data(data1))
Data.data_validation(data1)
