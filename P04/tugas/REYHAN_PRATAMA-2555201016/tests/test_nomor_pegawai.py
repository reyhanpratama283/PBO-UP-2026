import pytest
from dataclasses import FrozenInstanceError

from src.model.nomor_pegawai import NomorPegawai


def test_nomor_pegawai_valid() -> None:
    nomor = NomorPegawai("PG-001")
    assert nomor.nilai == "PG-001"


def test_nomor_pegawai_kosong_ditolak() -> None:
    with pytest.raises(ValueError):
        NomorPegawai("")


def test_nomor_pegawai_spasi_ditolak() -> None:
    with pytest.raises(ValueError):
        NomorPegawai("   ")


def test_nomor_pegawai_beku() -> None:
    nomor = NomorPegawai("PG-001")
    with pytest.raises(FrozenInstanceError):
        nomor.nilai = "PG-002"  # type: ignore[misc]
