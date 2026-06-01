from src.utils import records_class_category


# Проверка records_class на положительный результат
def test_records_class_is_positive(list_to_records_class):
    result = records_class_category(list_to_records_class)
    assert isinstance(result, list)
    assert result[0].name == "Смартфоны"
    assert result[0].description == "Смартфоны, как средство"


# Проверка records_class что при, передачи пустого списка возвращает пустой список
def test_records_class_empty_list():
    result = records_class_category([])
    assert result == []
