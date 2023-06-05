import openpyxl


class CheckoutPageData:     ## class name has to be pascle type

    def load_test_data_from_excel(self, file_name, sheet_name):
        data = []
        book = openpyxl.load_workbook(file_name)
        sheet = book[sheet_name]
        header = [cell.value for cell in sheet[1]]
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(dict(zip(header, row)))
        return data

