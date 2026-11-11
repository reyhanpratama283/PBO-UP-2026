
import pytest

from src.kepegawaian.pegawai import Pegawai
from src.kepegawaian.pegawai_tetap import PegawaiTetap
from src.kepegawaian.pegawai_harian import PegawaiHarian
from src.kepegawaian.pegawai_kontrak import PegawaiKontrak


def test_membuat_pegawai() -> None:
    pegawai = Pegawai("001", "Andi", 3_000_000)
    assert pegawai.nama == "Andi"


def test_penghasilan_dasar() -> None:
    pegawai = Pegawai("001", "Andi", 3_000_000)
    assert pegawai.hitung_penghasilan() == 3_000_000


def test_str_pegawai() -> None:
    pegawai = Pegawai("001", "Andi", 3_000_000)
    assert str(pegawai) == "001 - Andi"


def test_repr_pegawai() -> None:
    pegawai = Pegawai("001", "Andi", 3_000_000)
    assert "Pegawai" in repr(pegawai)


def test_pegawai_sama_berdasarkan_nip() -> None:
    pertama = Pegawai("001", "Andi", 3_000_000)
    kedua = Pegawai("001", "Budi", 4_000_000)
    assert pertama == kedua


def test_pegawai_bisa_menjadi_kunci_dictionary() -> None:
    pegawai = Pegawai("001", "Andi", 3_000_000)
    data = {pegawai: "Pegawai aktif"}
    assert data[pegawai] == "Pegawai aktif"


def test_nip_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("", "Andi", 3_000_000)


def test_nama_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("001", "", 3_000_000)


def test_gaji_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Pegawai("001", "Andi", 0)


def test_pegawai_tetap_mendapat_tunjangan() -> None:
    pegawai = PegawaiTetap("002", "Budi", 3_000_000, 500_000)
    assert pegawai.hitung_penghasilan() == 3_500_000


def test_tunjangan_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiTetap("002", "Budi", 3_000_000, -100_000)


def test_pegawai_harian_menghitung_hari_kerja() -> None:
    pegawai = PegawaiHarian("003", "Citra", 100_000, 20)
    assert pegawai.hitung_penghasilan() == 2_000_000


def test_jumlah_hari_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiHarian("003", "Citra", 100_000, 0)


def test_pegawai_kontrak_menghitung_kehadiran() -> None:
    pegawai = PegawaiKontrak("004", "Dedi", 3_000_000, 80)
    assert pegawai.hitung_penghasilan() == 2_400_000


def test_persentase_kehadiran_di_luar_batas_ditolak() -> None:
    with pytest.raises(ValueError):
        PegawaiKontrak("004", "Dedi", 3_000_000, 120)
