
from src.model.alamat import Alamat

NIK_LENGTH: int = 16


class Penyewa:
    """Mewakili penyewa alat pertanian beserta identitas dan alamatnya."""

    def __init__(
        self,
        nama: str,
        nik: str,
        telepon: str,
        alamat: Alamat,
    ) -> None:
        if not nama.strip():
            raise ValueError("Nama tidak boleh kosong")
        if len(nik) != NIK_LENGTH or not nik.isdigit():
            raise ValueError("NIK harus terdiri dari 16 digit")
        if not telepon.strip():
            raise ValueError("Telepon tidak boleh kosong")

        self._nama = nama
        self._nik = nik
        self.telepon = telepon
        self._alamat = alamat

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def nik(self) -> str:
        return self._nik

    @property
    def telepon(self) -> str:
        return self._telepon

    @telepon.setter
    def telepon(self, nilai: str) -> None:
        if not nilai.strip():
            raise ValueError("Telepon tidak boleh kosong")
        self._telepon = nilai

    @property
    def alamat(self) -> Alamat:
        return self._alamat
