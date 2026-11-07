const tombol = document.getElementById("btn-contoh");
const hasil = document.getElementById("hasil");

tombol.addEventListener("click", async function () {
  const respon = await fetch("/api/materi/stack");
  const data = await respon.json();
  hasil.textContent = data.isi;
});