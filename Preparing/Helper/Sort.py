def sortByColumns(data, columns):
        if(columns):
                data.sort_values(by=columns)
                return data