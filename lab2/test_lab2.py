from lab2 import load_from_csv, save_to_csv

def test_load_from_csv(tmp_path):
    csv_file = tmp_path / "data.csv"
    csv_file.write_text("name,phone,surname,email\nAnna,123,White,anna@mail.com\n")

    load_from_csv(str(csv_file))
    import lab2
    assert len(lab2.students) == 1
    assert lab2.students[0]["surname"] == "White"

def test_save_to_csv(tmp_path):
    csv_file = tmp_path / "output.csv"
    import lab2
    lab2.students = [{"name": "Tom", "phone": "111", "surname": "Black", "email": "t@mail.com"}]

    save_to_csv(str(csv_file))
    text = csv_file.read_text()
    assert "Tom" in text
    assert "Black" in text