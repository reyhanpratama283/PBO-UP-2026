import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def buat_alamat() -> Alamat:
    return Alamat("Jl. Merdeka", "Bangkinang", "Riau", "28412")


def buat_penyewa() -> Penyewa:
    return Penyewa("Reyhan", "1234567890123456", "08123456789", buat_alamat())


def test_alamat_berhasil_dibuat() -> None:
    assert buat_alamat().kota == "Bangkinang"


def test_alamat_jalan_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("", "Bangkinang", "Riau", "28412")


def test_alamat_kota_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Jl. Merdeka", "", "Riau", "28412")


def test_alamat_provinsi_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Jl. Merdeka", "Bangkinang", "", "28412")


def test_alamat_kode_pos_kosong() -> None:
    with pytest.raises(ValueError):
        Alamat("Jl. Merdeka", "Bangkinang", "Riau", "")


def test_alamat_tidak_bisa_diubah() -> None:
    alamat = buat_alamat()
    with pytest.raises(AttributeError):
        alamat.kota = "Pekanbaru"  # type: ignore[misc]


def test_penyewa_berhasil_dibuat() -> None:
    assert buat_penyewa().nama == "Reyhan"


def test_penyewa_nik_benar() -> None:
    assert buat_penyewa().nik == "1234567890123456"


def test_penyewa_nik_tidak_valid() -> None:
    with pytest.raises(ValueError):
        Penyewa("Reyhan", "12345", "08123456789", buat_alamat())


def test_penyewa_nik_harus_angka() -> None:
    with pytest.raises(ValueError):
        Penyewa("Reyhan", "123456789012345A", "08123456789", buat_alamat())


def test_penyewa_nama_kosong() -> None:
    with pytest.raises(ValueError):
        Penyewa("", "1234567890123456", "08123456789", buat_alamat())


def test_penyewa_telepon_kosong() -> None:
    with pytest.raises(ValueError):
        Penyewa("Reyhan", "1234567890123456", "", buat_alamat())


def test_penyewa_telepon_dapat_diubah() -> None:
    penyewa = buat_penyewa()
    penyewa.telepon = "082222222222"
    assert penyewa.telepon == "082222222222"


def test_penyewa_telepon_baru_kosong_ditolak() -> None:
    penyewa = buat_penyewa()
    with pytest.raises(ValueError):
        penyewa.telepon = ""


def test_penyewa_menyimpan_alamat() -> None:
    alamat = buat_alamat()
    penyewa = Penyewa("Reyhan", "1234567890123456", "08123456789", alamat)
    assert penyewa.alamat is alamat


def test_identitas_penyewa() -> None:
    assert "Reyhan" in buat_penyewa().identitas()
    assert "Bangkinang" in buat_penyewa().identitas()


def test_alat_tani_berhasil_dibuat() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    assert alat.kode == "TR-01"


def test_alat_tani_kode_kosong() -> None:
    with pytest.raises(ValueError):
        AlatTani("", "Traktor", 150_000)


def test_alat_tani_nama_kosong() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "", 150_000)


def test_tarif_minimum_diterima() -> None:
    alat = AlatTani("TR-02", "Traktor", 10_000)
    assert alat.tarif_harian == 10_000


def test_tarif_maksimum_diterima() -> None:
    alat = AlatTani("TR-03", "Traktor", 5_000_000)
    assert alat.tarif_harian == 5_000_000


def test_tarif_di_bawah_minimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-04", "Traktor", 9_000)


def test_tarif_di_atas_maksimum_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-05", "Traktor", 6_000_000)


def test_tarif_wajar() -> None:
    assert AlatTani.tarif_wajar(150_000)


def test_tarif_tidak_wajar() -> None:
    assert not AlatTani.tarif_wajar(5_000)


def test_format_rupiah() -> None:
    assert AlatTani.format_rupiah(150_000) == "Rp150.000"


def test_denda_keterlambatan() -> None:
    alat = AlatTani("TR-06", "Traktor", 150_000)
    assert alat.denda_keterlambatan(2) == 30_000


def test_hari_terlambat_negatif_ditolak() -> None:
    alat = AlatTani("TR-07", "Traktor", 150_000)
    with pytest.raises(ValueError):
        alat.denda_keterlambatan(-1)


def test_baca_data_csv() -> None:
    alat = AlatTani.dari_baris_csv("TR-08;Traktor;150000")
    assert alat.nama == "Traktor"
    assert alat.tarif_harian == 150_000


def test_csv_dengan_jumlah_kolom_salah() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-09;Traktor")


def test_csv_tarif_bukan_angka() -> None:
    with pytest.raises(ValueError):
        AlatTani.dari_baris_csv("TR-10;Traktor;mahal")
