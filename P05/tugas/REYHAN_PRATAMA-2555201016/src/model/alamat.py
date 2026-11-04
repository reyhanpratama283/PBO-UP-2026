
from dataclasses import dataclass


@dataclass(frozen=True)
class Alamat:
    """Menyimpan informasi alamat secara tetap dan tervalidasi."""

    jalan: str
    kota: str
    provinsi: str
    kode_pos: str

    def __post_init__(self) -> None:
        if not self.jalan.strip():
            raise ValueError("Jalan tidak boleh kosong")
        if not self.kota.strip():
            raise ValueError("Kota tidak boleh kosong")
        if not self.provinsi.strip():
            raise ValueError("Provinsi tidak boleh kosong")
        if not self.kode_pos.strip():
            raise ValueError("Kode pos tidak boleh kosong")
