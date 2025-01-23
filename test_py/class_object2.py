column_container = {
    "file_download": {
        "column_name": "file_download",
        "data_type": "timestamp",
        "default": "now()"
    },
    "type_code": {
        "column_name": "type_code",
        "data_type": "text",
        "default": None
    }
}

class column_object:
    def __init__(self, name):
        self.name = name
        self.default = None
        
        if name == 'file_download':
            self.data_type = "timestamp"
            self.default = "now()"
        
        elif name == "type_code":
            self.data_type = "text"
        else:
            print(f"Couldnt find any properties for column name: {name}")

col1 = column_object('file_download')
col2 = column_object('type_code')
col3 = column_object('dog')

print(f'\ncol1: {col1.name}, data_type: {col1.data_type}, default: {col1.default}')
print(f'col2: {col2.name}, data_type: {col2.data_type}, default: {col2.default}\n')

