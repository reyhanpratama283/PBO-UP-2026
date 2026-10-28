
import pytest

from src.model.petugas import Petugas


def test_petugas_valid() -> None:
    petugas = Petugas("PT-01", "Budi Santoso", "Operator")
    assert petugas.nama == "Budi Santoso"
    assert petugas.jabatan == "Operator"
    assert petugas.telepon == "-"


def test_dua_petugas_memiliki_data_masing_masing() -> None:
    petugas1 = Petugas("PT-01", "Budi Santoso", "Operator")
    petugas2 = Petugas("PT-02", "Siti Aminah", "Admin")

    assert petugas1.nama == "Budi Santoso"
    assert petugas2.nama == "Siti Aminah"


def test_identitas_petugas() -> None:
    petugas = Petugas("PT-01", "Budi Santoso", "Operator")
    assert petugas.identitas() == "Budi Santoso (PT-01)"


def test_id_petugas_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("", "Budi Santoso", "Operator")


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "", "Operator")


def test_jabatan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "Budi Santoso", "")


def test_telepon_tidak_valid_ditolak() -> None:
    with pytest.raises(ValueError):
        Petugas("PT-01", "Budi Santoso", "Operator", "123")


def test_setter_telepon() -> None:
    petugas = Petugas("PT-01", "Budi Santoso", "Operator")
    petugas.telepon = "081234567890"
    assert petugas.telepon == "081234567890"
