
import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.penyewa import Penyewa


def test_alamat_valid() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    assert alamat.kota == "Bangkinang"


def test_alamat_jalan_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat(
            jalan="",
            kota="Bangkinang",
            provinsi="Riau",
            kode_pos="28411",
        )


def test_alamat_beku_tidak_bisa_diubah() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )


    with pytest.raises(AttributeError):
        alamat.kota = "Pekanbaru"  # type: ignore[misc]
def test_alamat_kota_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat(
            jalan="Jalan Merdeka No. 10",
            kota="",
            provinsi="Riau",
            kode_pos="28411",
        )


def test_alamat_provinsi_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat(
            jalan="Jalan Merdeka No. 10",
            kota="Bangkinang",
            provinsi="",
            kode_pos="28411",
        )


def test_alamat_kode_pos_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Alamat(
            jalan="Jalan Merdeka No. 10",
            kota="Bangkinang",
            provinsi="Riau",
            kode_pos="",
        )



def test_penyewa_valid() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    penyewa = Penyewa(
        nama="Budi Santoso",
        nik="1234567890123456",
        telepon="08123456789",
        alamat=alamat,
    )

    assert penyewa.nama == "Budi Santoso"
    assert penyewa.nik == "1234567890123456"
    assert penyewa.telepon == "08123456789"
    assert penyewa.alamat == alamat



def test_penyewa_nama_kosong_ditolak() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    with pytest.raises(ValueError, match="Nama tidak boleh kosong"):
        Penyewa(
            nama="",
            nik="1234567890123456",
            telepon="08123456789",
            alamat=alamat,
        )


def test_penyewa_nik_tidak_cukup_16_digit_ditolak() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    with pytest.raises(ValueError, match="NIK harus terdiri dari 16 digit"):
        Penyewa(
            nama="Budi Santoso",
            nik="12345",
            telepon="08123456789",
            alamat=alamat,
        )


def test_penyewa_nik_mengandung_huruf_ditolak() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    with pytest.raises(ValueError, match="NIK harus terdiri dari 16 digit"):
        Penyewa(
            nama="Budi Santoso",
            nik="123456789012345A",
            telepon="08123456789",
            alamat=alamat,
        )


def test_penyewa_telepon_kosong_ditolak() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    with pytest.raises(ValueError, match="Telepon tidak boleh kosong"):
        Penyewa(
            nama="Budi Santoso",
            nik="1234567890123456",
            telepon="",
            alamat=alamat,
        )


def test_penyewa_telepon_bisa_diubah() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    penyewa = Penyewa(
        nama="Budi Santoso",
        nik="1234567890123456",
        telepon="08123456789",
        alamat=alamat,
    )

    penyewa.telepon = "08987654321"

    assert penyewa.telepon == "08987654321"


def test_penyewa_telepon_spasi_ditolak() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    with pytest.raises(ValueError, match="Telepon tidak boleh kosong"):
        Penyewa(
            nama="Budi Santoso",
            nik="1234567890123456",
            telepon="   ",
            alamat=alamat,
        )


def test_penyewa_alamat_bisa_dibaca() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    penyewa = Penyewa(
        nama="Budi Santoso",
        nik="1234567890123456",
        telepon="08123456789",
        alamat=alamat,
    )

    assert penyewa.alamat.jalan == "Jalan Merdeka No. 10"


def test_penyewa_nama_tidak_bisa_diubah() -> None:
    alamat = Alamat(
        jalan="Jalan Merdeka No. 10",
        kota="Bangkinang",
        provinsi="Riau",
        kode_pos="28411",
    )
    penyewa = Penyewa(
        nama="Budi Santoso",
        nik="1234567890123456",
        telepon="08123456789",
        alamat=alamat,
    )

    with pytest.raises(AttributeError):
        penyewa.nama = "Siti Aminah"  # type: ignore[misc]


def test_alat_tani_tarif_valid() -> None:
    alat = AlatTani("TR-01", "Traktor", 150000)
    assert alat.tarif_harian == 150000


def test_alat_tani_tarif_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", 0)


def test_alat_tani_tarif_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        AlatTani("TR-01", "Traktor", -1000)
