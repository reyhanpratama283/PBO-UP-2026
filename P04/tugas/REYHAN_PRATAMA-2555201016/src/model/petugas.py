
"""Model petugas yang melayani penyewaan alat pertanian."""


class Petugas:
    """Mewakili petugas UPJA yang melayani penyewaan."""

    def __init__(
        self,
        id_petugas: str,
        nama: str,
        jabatan: str,
        telepon: str = "-",
    ) -> None:
        if not id_petugas.strip():
            raise ValueError("ID petugas tidak boleh kosong")
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        if not jabatan.strip():
            raise ValueError("Jabatan tidak boleh kosong")

        self._id_petugas = id_petugas
        self._nama = nama
        self._jabatan = jabatan
        self.telepon = telepon

    # Hanya-baca agar ID petugas tidak berubah setelah objek dibuat.
    @property
    def id_petugas(self) -> str:
        """Mengembalikan ID petugas."""
        return self._id_petugas

    # Hanya-baca agar perubahan nama dikendalikan melalui objek.
    @property
    def nama(self) -> str:
        """Mengembalikan nama petugas."""
        return self._nama

    # Hanya-baca agar jabatan tidak diubah sembarangan.
    @property
    def jabatan(self) -> str:
        """Mengembalikan jabatan petugas."""
        return self._jabatan

    # Bisa dibaca dan diubah, tetapi setter memvalidasi nomor telepon.
    @property
    def telepon(self) -> str:
        """Mengembalikan nomor telepon petugas."""
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        """Memastikan nomor telepon valid sebelum disimpan."""
        nomor = nilai.strip().replace(" ", "").replace("-", "")
        if nilai.strip() != "-" and (
            not nomor.isdigit() or len(nomor) < 10
        ):
            raise ValueError("Telepon harus berupa minimal 10 digit")
        self._telepon = nilai.strip()

    def identitas(self) -> str:
        """Mengembalikan identitas petugas."""
        return f"{self.nama} ({self.id_petugas})"

    def keterangan(self) -> str:
        """Mengembalikan jabatan dan nomor telepon petugas."""
        return f"{self.jabatan} — Telepon: {self.telepon}"
