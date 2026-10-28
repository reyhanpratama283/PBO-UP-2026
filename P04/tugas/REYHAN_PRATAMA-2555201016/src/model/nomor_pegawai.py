"""Model nilai beku untuk nomor pegawai."""

from dataclasses import dataclass


@dataclass(frozen=True)
class NomorPegawai:
    """Mewakili nomor identitas unik seorang petugas."""

    nilai: str

    def __post_init__(self) -> None:
        """Memastikan nomor pegawai tidak kosong."""
        if not self.nilai.strip():
            raise ValueError("Nomor pegawai tidak boleh kosong")
