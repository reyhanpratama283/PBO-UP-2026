
class Pegawai:
    """Kelas induk untuk data dan penghasilan pegawai."""

    def __init__(self, nip: str, nama: str, gaji_pokok: int) -> None:
        if not nip.strip():
            raise ValueError("NIP tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        if gaji_pokok <= 0:
            raise ValueError("Gaji pokok harus lebih dari 0")

        self._nip = nip
        self._nama = nama
        self._gaji_pokok = gaji_pokok

    @property
    def nip(self) -> str:
        return self._nip

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def gaji_pokok(self) -> int:
        return self._gaji_pokok

    def hitung_penghasilan(self, potongan: int = 0) -> int:
        """Menghitung penghasilan setelah dikurangi potongan."""
        if potongan < 0 or potongan > self.gaji_pokok:
            raise ValueError("Potongan tidak valid")
        return self.gaji_pokok - potongan

    def __str__(self) -> str:
        return f"{self.nip} - {self.nama}"

    def __repr__(self) -> str:
        return (
            f"Pegawai(nip={self.nip!r}, "
            f"nama={self.nama!r}, gaji_pokok={self.gaji_pokok!r})"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Pegawai):
            return NotImplemented
        return self.nip == other.nip

    def __hash__(self) -> int:
        return hash(self.nip)
