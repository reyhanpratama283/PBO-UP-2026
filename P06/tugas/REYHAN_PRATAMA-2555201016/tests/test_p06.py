import pytest
from src.model.alat_tani import AlatTani
from src.model.perontok import Perontok
from src.model.pompa_air import PompaAir
from src.model.traktor import Traktor


def test_traktor_mewarisi_alat_tani() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150_000, 8)
    assert isinstance(alat, AlatTani)


def test_pompa_air_mewarisi_alat_tani() -> None:
    alat = PompaAir("PA-01", "Pompa Air", 75_000, 600)
    assert isinstance(alat, AlatTani)


def test_perontok_mewarisi_alat_tani() -> None:
    alat = Perontok("PR-01", "Mesin Perontok", 200_000, 900)
    assert isinstance(alat, AlatTani)


def test_biaya_traktor_satu_hari() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150_000, 8)
    assert alat.biaya_sewa(1) == 250_000


def test_biaya_traktor_tiga_hari() -> None:
    alat = Traktor("TR-01", "Traktor Kubota", 150_000, 8)
    assert alat.biaya_sewa(3) == 750_000


def test_tenaga_kuda_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        Traktor("TR-01", "Traktor Kubota", 150_000, 0)


def test_konsumsi_solar_pompa_air() -> None:
    alat = PompaAir("PA-01", "Pompa Air", 75_000, 600)
    assert alat.konsumsi_solar_harian() == 18


def test_biaya_pompa_air_satu_hari() -> None:
    alat = PompaAir("PA-01", "Pompa Air", 75_000, 600)
    assert alat.biaya_sewa(1) == 201_000


def test_biaya_pompa_air_tiga_hari() -> None:
    alat = PompaAir("PA-01", "Pompa Air", 75_000, 600)
    assert alat.biaya_sewa(3) == 603_000


def test_debit_nol_ditolak() -> None:
    with pytest.raises(ValueError):
        PompaAir("PA-01", "Pompa Air", 75_000, 0)


def test_perontok_satu_hari_ditagih_dua_hari() -> None:
    alat = Perontok("PR-01", "Mesin Perontok", 200_000, 900)
    assert alat.biaya_sewa(1) == 400_000


def test_perontok_tiga_hari() -> None:
    alat = Perontok("PR-01", "Mesin Perontok", 200_000, 900)
    assert alat.biaya_sewa(3) == 600_000


def test_hari_tagihan_minimum_perontok() -> None:
    assert Perontok.hari_ditagih(1) == 2


def test_hari_tagihan_normal_perontok() -> None:
    assert Perontok.hari_ditagih(3) == 3


def test_str_alat_tani() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    assert "[TR-01]" in str(alat)
    assert "Rp150.000/hari" in str(alat)


def test_repr_alat_tani() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    assert "AlatTani" in repr(alat)
    assert "TR-01" in repr(alat)


def test_alat_dengan_kode_sama_dianggap_sama() -> None:
    alat1 = AlatTani("TR-01", "Traktor", 150_000)
    alat2 = Traktor("TR-01", "Traktor Kubota", 200_000, 8)
    assert alat1 == alat2


def test_alat_dengan_kode_berbeda_tidak_sama() -> None:
    alat1 = AlatTani("TR-01", "Traktor", 150_000)
    alat2 = AlatTani("TR-02", "Traktor", 150_000)
    assert alat1 != alat2


def test_alat_dibandingkan_dengan_objek_lain() -> None:
    alat = AlatTani("TR-01", "Traktor", 150_000)
    assert alat != "Traktor"


def test_hash_alat_dapat_digunakan_dalam_set() -> None:
    alat1 = AlatTani("TR-01", "Traktor", 150_000)
    alat2 = AlatTani("TR-01", "Traktor Kubota", 200_000)

    kumpulan = {alat1, alat2}

    assert len(kumpulan) == 1
