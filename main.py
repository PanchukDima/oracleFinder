from FileParser import FileParser


if __name__ == '__main__':
    FP = FileParser("C:/pkg_iemk_4.pck")
    FP.start_parse()
    print(FP.search_procedure_declare())
