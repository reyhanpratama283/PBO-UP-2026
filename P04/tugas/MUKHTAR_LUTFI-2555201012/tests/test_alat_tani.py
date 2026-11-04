"""Pengujian untuk model AlatTani."""

from typing import cast

import pytest
from src.model.alat_tani import AlatTani


@pytest.fixture
def alat() -> AlatTani:
    return AlatTani("TR-01", "Traktor", 100_000)


def test_konstruktor_menyimpan_kode(alat: AlatTani) -> None:
    assert alat.kode == "TR-01"


def test_konstruktor_menyimpan_nama(alat: AlatTani) -> None:
    assert alat.nama == "Traktor"


def test_konstruktor_menyimpan_tarif(alat: AlatTani) -> None:
    assert alat.tarif_harian == 100_000


def test_tarif_minimum_diterima() -> None:
    alat = AlatTani("A1", "Alat", 10_000)
    assert alat.tarif_harian == 10_000


def test_tarif_maksimum_diterima() -> None:
    alat = AlatTani("A1", "Alat", 5_000_000)
    assert alat.tarif_harian == 5_000_000


def test_tarif_di_bawah_minimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("A1", "Alat", 9_999)


def test_tarif_di_atas_maksimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("A1", "Alat", 5_000_001)


def test_tarif_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("A1", "Alat", 0)


def test_tarif_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("A1", "Alat", -10_000)


def test_tarif_float_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("A1", "Alat", cast(int, 100_000.5))


def test_tarif_boolean_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("A1", "Alat", True)


def test_tarif_wajar_menerima_nilai_valid() -> None:
    assert AlatTani.tarif_wajar(100_000) is True


def test_tarif_wajar_menolak_nilai_tidak_valid() -> None:
    assert AlatTani.tarif_wajar(5_000) is False


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(1_500_000) == "Rp1.500.000"


def test_format_rupiah_nilai_kecil() -> None:
    assert AlatTani.format_rupiah(10_000) == "Rp10.000"


def test_biaya_sewa_satu_hari(alat: AlatTani) -> None:
    assert alat.biaya_sewa(1) == 100_000


def test_biaya_sewa_beberapa_hari(alat: AlatTani) -> None:
    assert alat.biaya_sewa(3) == 300_000


def test_biaya_sewa_nol_hari(alat: AlatTani) -> None:
    assert alat.biaya_sewa(0) == 0


def test_biaya_sewa_hari_negatif_ditolak(alat: AlatTani) -> None:
    with pytest.raises(ValueError):
        alat.biaya_sewa(-1)


def test_denda_keterlambatan() -> None:
    alat = AlatTani("A1", "Alat", 100_000)
    assert alat.denda_keterlambatan(2) == 20_000


def test_denda_nol_hari(alat: AlatTani) -> None:
    assert alat.denda_keterlambatan(0) == 0


def test_denda_hari_negatif_ditolak(alat: AlatTani) -> None:
    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)


def test_dari_baris_csv() -> None:
    alat = AlatTani.dari_baris_csv("TR-02;Traktor Besar;200000")
    assert alat.kode == "TR-02"
    assert alat.nama == "Traktor Besar"
    assert alat.tarif_harian == 200_000


def test_dari_baris_csv_dengan_jumlah_kolom_salah() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-02;Traktor")


def test_dari_baris_csv_tarif_bukan_angka() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-02;Traktor;mahal")


def test_jumlah_terdaftar_bertambah() -> None:
    awal = AlatTani.jumlah_terdaftar()
    AlatTani("A1", "Alat Pertama", 100_000)
    AlatTani("A2", "Alat Kedua", 200_000)
    akhir = AlatTani.jumlah_terdaftar()

    assert akhir - awal == 2
