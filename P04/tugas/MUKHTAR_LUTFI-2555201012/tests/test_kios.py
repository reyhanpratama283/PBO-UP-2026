
import pytest

from src.kios import Kios


def test_membuat_produk_valid() -> None:
    produk = Kios("B001", "Beras", 10000, 12000, 20)

    assert produk.kode == "B001"
    assert produk.nama_produk == "Beras"


def test_konstanta_nama_kios() -> None:
    assert Kios.NAMA_KIOS == "Kios UMKM Bangkinang"


def test_harga_wajar() -> None:
    assert Kios.harga_wajar(10000, 12000) is True


def test_harga_jual_terlalu_rendah() -> None:
    assert Kios.harga_wajar(10000, 9000) is False


def test_harga_modal_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("B002", "Gula", 0, 12000, 10)

def test_stok_boleh_nol() -> None:
    produk = Kios("B003", "Minyak", 10000, 12000, 0)

    assert produk.stok == 0


def test_stok_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("B004", "Telur", 10000, 12000, -1)


def test_kode_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("", "Beras", 10000, 12000, 10)


def test_nama_produk_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("B005", "", 10000, 12000, 10)


def test_harga_jual_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("B006", "Gula", 10000, 0, 10)

def test_margin_minimum_diterima() -> None:
    assert Kios.harga_wajar(10000, 11000) is True


def test_margin_maksimum_diterima() -> None:
    assert Kios.harga_wajar(10000, 20000) is True


def test_margin_melebihi_batas_ditolak() -> None:
    assert Kios.harga_wajar(10000, 21000) is False


def test_harga_modal_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("B007", "Garam", -1000, 12000, 10)


def test_kode_hanya_spasi_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("   ", "Beras", 10000, 12000, 10)


def test_nama_hanya_spasi_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios("B008", "   ", 10000, 12000, 10)


def test_stok_produk_valid() -> None:
    produk = Kios("B009", "Tepung", 10000, 12000, 15)
    assert produk.stok == 15


def test_classmethod_dari_baris_valid() -> None:
    produk = Kios.dari_baris_csv("B010|Beras|10000|12000|20")
    assert produk.kode == "B010"
    assert produk.nama_produk == "Beras"
    assert produk.stok == 20


def test_classmethod_format_salah_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("B011|Gula|10000")


def test_classmethod_harga_bukan_angka_ditolak() -> None:
    with pytest.raises(ValueError):
        Kios.dari_baris_csv("B012|Gula|abc|12000|10")


def test_pencacah_naik_satu_produk() -> None:
    awal = Kios.jumlah_terdaftar()
    Kios("B013", "Garam", 5000, 6000, 10)
    akhir = Kios.jumlah_terdaftar()
    assert akhir - awal == 1
