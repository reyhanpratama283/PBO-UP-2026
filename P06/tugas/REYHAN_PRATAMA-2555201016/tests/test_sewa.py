import pytest
from src.model.alamat import Alamat
from src.model.alat_tani import AlatTani
from src.model.baris_sewa import BarisSewa
from src.model.penyewa import Penyewa
from src.model.sewa import Sewa


def buat_penyewa() -> Penyewa:
    alamat = Alamat("Jl. Merdeka", "Bangkinang", "Riau", "28412")
    return Penyewa("Reyhan", "1234567890123456", "08123456789", alamat)


def buat_alat(kode: str = "TR-01") -> AlatTani:
    return AlatTani(kode, "Traktor", 150_000)


def test_baris_sewa_menyimpan_alat() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)
    assert baris.alat is alat


def test_baris_sewa_menyimpan_jumlah_hari() -> None:
    baris = BarisSewa(buat_alat(), 3)
    assert baris.jumlah_hari == 3


def test_baris_sewa_menyimpan_kode_alat() -> None:
    baris = BarisSewa(buat_alat(), 2)
    assert baris.kode_alat == "TR-01"


def test_baris_sewa_menyimpan_nama_alat() -> None:
    baris = BarisSewa(buat_alat(), 2)
    assert baris.nama_alat == "Traktor"


def test_baris_sewa_menyimpan_tarif() -> None:
    baris = BarisSewa(buat_alat(), 2)
    assert baris.tarif_saat_sewa == 150_000


def test_subtotal_baris_sewa() -> None:
    baris = BarisSewa(buat_alat(), 3)
    assert baris.subtotal() == 450_000


def test_baris_nota() -> None:
    baris = BarisSewa(buat_alat(), 2)
    assert "Traktor" in baris.baris_nota()
    assert "Rp300.000" in baris.baris_nota()


def test_jumlah_hari_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), 0)


def test_jumlah_hari_negatif_ditolak() -> None:
    with pytest.raises(ValueError):
        BarisSewa(buat_alat(), -1)


def test_tarif_lama_tidak_berubah() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)
    alat.tarif_harian = 175_000
    assert baris.subtotal() == 450_000


def test_tarif_nota_lama_tidak_berubah() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 3)
    nota_lama = baris.baris_nota()
    alat.tarif_harian = 175_000
    assert baris.baris_nota() == nota_lama


def test_nomor_sewa() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    assert sewa.nomor == "SW-001"


def test_penyewa_sewa() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW-001", penyewa)
    assert sewa.penyewa is penyewa


def test_baris_awalnya_kosong() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    assert sewa.baris == ()


def test_tambah_satu_alat() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    assert len(sewa.baris) == 1


def test_baris_sewa_dibuat_di_dalam_sewa() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    assert isinstance(sewa.baris[0], BarisSewa)


def test_total_sewa() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 3)
    assert sewa.total() == 450_000


def test_total_beberapa_alat() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat("TR-01"), 2)
    sewa.tambah_alat(
        AlatTani("PA-01", "Pompa Air", 75_000), 3
    )
    assert sewa.total() == 525_000


def test_nomor_sewa_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        Sewa(" ", buat_penyewa())


def test_alat_duplikat_ditolak() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    with pytest.raises(ValueError):
        sewa.tambah_alat(buat_alat(), 3)


def test_maksimal_sepuluh_alat() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    for nomor in range(10):
        sewa.tambah_alat(
            AlatTani(f"AL-{nomor}", f"Alat {nomor}", 50_000), 1
        )
    assert len(sewa.baris) == 10


def test_alat_ke_sebelas_ditolak() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    for nomor in range(10):
        sewa.tambah_alat(
            AlatTani(f"AL-{nomor}", f"Alat {nomor}", 50_000), 1
        )
    with pytest.raises(ValueError):
        sewa.tambah_alat(AlatTani("AL-10", "Alat 10", 50_000), 1)


def test_baris_tidak_bisa_diubah_langsung() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    assert isinstance(sewa.baris, tuple)


def test_mengubah_salinin_baris_tidak_mengubah_sewa() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    salinan = sewa.baris
    salinan_lama = len(salinan)
    salinan_baru = (*salinan, BarisSewa(buat_alat("TR-02"), 1))
    assert len(sewa.baris) == salinan_lama
    assert len(salinan_baru) == 2


def test_penyewa_tetap_sama_setelah_sewa_dibuat() -> None:
    penyewa = buat_penyewa()
    sewa = Sewa("SW-001", penyewa)
    assert sewa.penyewa is penyewa


def test_alat_tetap_ada_setelah_baris_dibuat() -> None:
    alat = buat_alat()
    baris = BarisSewa(alat, 2)
    del baris
    assert alat.kode == "TR-01"


def test_nota_memuat_nomor_sewa() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    assert "SW-001" in sewa.nota()


def test_nota_memuat_identitas_penyewa() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    assert "Reyhan" in sewa.nota()


def test_nota_memuat_rincian_alat() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    assert "Traktor" in sewa.nota()


def test_nota_memuat_total() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)
    assert "Rp300.000" in sewa.nota()


def test_total_sewa_tetap_setelah_tarif_naik() -> None:
    alat = buat_alat()
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(alat, 3)
    alat.tarif_harian = 175_000
    assert sewa.total() == 450_000


def test_nota_lama_tetap_setelah_tarif_naik() -> None:
    alat = buat_alat()
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(alat, 3)
    nota_lama = sewa.nota()
    alat.tarif_harian = 175_000
    assert sewa.nota() == nota_lama


def test_komposisi_tidak_dapat_dibongkar_dari_luar() -> None:
    sewa = Sewa("SW-001", buat_penyewa())
    sewa.tambah_alat(buat_alat(), 2)

    with pytest.raises(AttributeError):
        sewa.baris.append(None)  # type: ignore[attr-defined]

    assert len(sewa.baris) == 1
