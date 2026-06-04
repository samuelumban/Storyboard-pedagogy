---
name: storyboard-bimas-kristen
description: >
  Buat template storyboard pembelajaran linear resmi Kementerian Agama RI –
  Direktorat Jenderal Bimbingan Masyarakat Kristen dalam format PDF.
  Gunakan skill ini setiap kali pengguna meminta storyboard, template video
  pembelajaran, atau dokumen perencanaan media pembelajaran berbasis 9 tahap
  (Pembuka → Inti → Penutup). Skill ini menghasilkan file PDF yang persis sama
  dengan template resmi bimaskristen.kemenag.go.id, termasuk kop surat, tabel
  meta, kolom tanda tangan, dan 9 blok scene ber-tahap dengan kolom No/Scene/
  Durasi/Narasi/Visual/Interaksi/Keterangan. Output selalu berupa file PDF siap
  cetak dan siap unduh.
---

# Storyboard Template Generator – Bimas Kristen Kemenag RI

## Gambaran Umum

Skill ini menghasilkan template storyboard pembelajaran linear resmi sesuai
format Direktorat Jenderal Bimbingan Masyarakat Kristen, Kementerian Agama RI.
Output berupa PDF 3–4 halaman A4 yang identik dengan `Template_Storyboard_Linear.pdf`.

Struktur dokumen:
1. **Halaman 1** – Kop surat, tabel meta (Judul/Fase/Tujuan/Capaian + No Dok/Tanggal/Durasi/Ahli), tabel tanda tangan (Dibuat/Diperiksa/Disetujui), judul STORYBOARD, serta dua blok scene pertama (Tahap 1 & 2).
2. **Halaman 2–3** – Sisa 7 blok scene, dibagi tiga fase: TAHAP PEMBUKA (3 scene) → TAHAP INTI (3 scene) → TAHAP PENUTUP (3 scene).

---

## Cara Menggunakan

### 1. Jalankan script Python

```python
# Pastikan reportlab tersedia:
# pip install reportlab --break-system-packages

import sys
sys.path.insert(0, "/path/to/storyboard-skill/scripts")
from generate_storyboard import generate

generate(
    output_path="/mnt/user-data/outputs/storyboard.pdf",

    # Data meta (semua opsional – kosong jika tidak diisi)
    meta={
        "judul":          "Hukum Kasih",
        "fase":           "Fase E – Pendidikan Agama Kristen",
        "tujuan":         "Peserta memahami makna hukum kasih dalam kehidupan",
        "capaian":        "CP.1.2 – Mengasihi sesama seperti diri sendiri",
        "no_dokumen":     "SB-2025-001",
        "tanggal_rilis":  "Juni 2025",
        "total_durasi":   "15 menit",
        "ahli_materi":    "Dr. Sinta Wulandari",
    },

    # Tanda tangan (opsional)
    dibuat    = {"nama": "Budi Santoso, S.Pd", "nip": "NIP. 198501012010011001"},
    diperiksa = {"nama": "Dewi Rahayu, M.Pd",  "nip": "NIP. 197803042005022003"},
    disetujui = {"nama": "Prof. Yusuf Manalu",  "nip": "NIP. 196712101990031002"},

    # Logo (opsional) – path ke file gambar PNG/JPG lambang Kemenag
    logo_path = None,
)
```

### 2. Sebagai skrip mandiri (tanpa parameter)

```bash
python scripts/generate_storyboard.py /mnt/user-data/outputs/storyboard.pdf
```

Akan menghasilkan template kosong (semua kolom meta kosong, tanda tangan
menggunakan placeholder NAMA / NIP.).

---

## Alur Kerja Claude

Ketika pengguna meminta template storyboard:

1. **Kumpulkan data** – tanyakan satu per satu (atau parsing dari teks user):
   - Judul Materi, Fase & Mata Pelajaran, Tujuan Pembelajaran, Capaian Pembelajaran
   - No Dokumen, Tanggal Rilis, Total Durasi, Ahli Materi
   - Nama + NIP untuk kolom Dibuat/Diperiksa/Disetujui
   - Apakah memiliki logo (file path)?

2. **Buat PDF** – jalankan `generate_storyboard.py` melalui `bash_tool` dengan
   parameter sesuai data yang terkumpul.

3. **Simpan ke output** – selalu simpan ke `/mnt/user-data/outputs/`.

4. **Presentasikan** – panggil `present_files` agar pengguna dapat mengunduh.

### Contoh Perintah Bash

```bash
python3 - << 'EOF'
import sys
sys.path.insert(0, "/home/claude/storyboard-skill/scripts")
from generate_storyboard import generate

generate(
    output_path="/mnt/user-data/outputs/storyboard.pdf",
    meta={
        "judul": "...",
        # dst.
    }
)
EOF
```

---

## Parameter `generate()`

| Parameter     | Tipe   | Keterangan |
|---------------|--------|------------|
| `output_path` | `str`  | **Wajib.** Path lengkap file PDF output. |
| `meta`        | `dict` | Opsional. Kunci: `judul`, `fase`, `tujuan`, `capaian`, `no_dokumen`, `tanggal_rilis`, `total_durasi`, `ahli_materi`. |
| `dibuat`      | `dict` | Opsional. Kunci: `nama`, `nip`. Default: `NAMA / NIP.` |
| `diperiksa`   | `dict` | Opsional. Kunci: `nama`, `nip`. Default: `NAMA / NIP.` |
| `disetujui`   | `dict` | Opsional. Kunci: `nama`, `nip`. Default: `NAMA / NIP.` |
| `logo_path`   | `str`  | Opsional. Path ke file gambar logo (PNG/JPG). Jika `None`, kolom logo dikosongkan. |

---

## Struktur Dokumen yang Dihasilkan

```
Halaman 1
├── Kop Surat (logo + nama institusi)
├── Garis pemisah
├── Tabel Meta (4 baris × 4 kolom)
├── Tabel Tanda Tangan (Dibuat | Diperiksa | Disetujui)
├── Bar hitam: S T O R Y B O A R D
├── [TAHAP PEMBUKA]
│   ├── Tahap 1: Menarik Perhatian Peserta
│   └── Tahap 2: Menyampaikan Tujuan Pembelajaran
Halaman 2
│   └── Tahap 3: Menggali Pengetahuan Awal Peserta
├── [TAHAP INTI]
│   ├── Tahap 4: Menyajikan Konten Pembelajaran
│   ├── Tahap 5: Latihan Interaktif
│   └── Tahap 6: Pembelajaran Mandiri
Halaman 3
├── [TAHAP PENUTUP]
│   ├── Tahap 7: Feedback
│   ├── Tahap 8: Refleksi
│   └── Tahap 9: Penguatan dan Aplikasi
```

Setiap blok scene terdiri dari:
- Sub-judul miring (label tahap)
- Tabel: No | Scene | Durasi | Narasi | Visual
- Baris bawah: Interaksi | Keterangan/Catatan

---

## Dependensi

```
reportlab >= 4.0   # pip install reportlab --break-system-packages
Pillow             # (opsional, untuk logo) pip install Pillow --break-system-packages
```

---

## Catatan Penting

- **Bagian "Keterangan" di halaman terakhir template asli tidak dimasukkan** —
  sesuai permintaan desain. Dokumen berakhir setelah Tahap 9.
- Ukuran halaman: **A4 portrait** (210 × 297 mm).
- Margin: 20 mm kiri/kanan, 15 mm atas/bawah.
- Font: Helvetica (built-in ReportLab, tidak memerlukan font eksternal).
- Jika logo tidak disediakan, kolom logo di kop surat dikosongkan (tidak mempengaruhi layout).
