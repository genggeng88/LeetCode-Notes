class SQL:
    def __init__(self, names: List[str], columns: List[int]):
        self.table: Dict[str, List[str]] = {}
        for name in names:
            self.table[name] = []

    def insertRow(self, name: str, row: List[str]) -> None:
        self.table[name].append(row)


    def deleteRow(self, name: str, rowId: int) -> None:
        pass

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.table[name][rowId-1][columnId-1]