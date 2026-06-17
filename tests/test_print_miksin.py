from src.lawn_grass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_print_mixin(capsys):
    Product("Iphone", "Iphone 15 pro max", 120000.0, 5)
    captured = capsys.readouterr()
    assert captured.out.rstrip("\n") == "Product (Iphone, Iphone 15 pro max, 120000.0, 5)"

    Smartphone("Poco", "Poco readme 9 note", 20000.0, 6, 45, "9 note", 120, "grey")
    captured = capsys.readouterr()
    assert captured.out.rstrip("\n") == "Smartphone (Poco, Poco readme 9 note, 20000.0, 6)"

    LawnGrass("Plutovka", "Трава", 200, 6, "Россия", 6, "Зеленая")
    captured = capsys.readouterr()
    assert captured.out.rstrip("\n") == "LawnGrass (Plutovka, Трава, 200, 6)"
