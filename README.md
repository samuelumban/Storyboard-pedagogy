# 📄 Skill: Storyboard Bimas Kristen

**Generator template storyboard pembelajaran linear resmi**  
Kementerian Agama RI – Direktorat Jenderal Bimbingan Masyarakat Kristen

---

## Tentang Skill Ini

Skill ini memungkinkan Claude menghasilkan file PDF template storyboard yang **identik secara visual** dengan dokumen resmi `Template_Storyboard_Linear.pdf` dari Ditjen Bimas Kristen Kemenag RI.

Output mencakup:
- ✅ Kop surat resmi (nama institusi, alamat, website)
- ✅ Tabel meta pembelajaran (Judul, Fase, Tujuan, Capaian, dsb.)
- ✅ Tabel tanda tangan (Dibuat / Diperiksa / Disetujui)
- ✅ Bar hitam "S T O R Y B O A R D"
- ✅ 9 blok scene lengkap: Tahap Pembuka → Inti → Penutup
- ✅ Setiap blok berisi kolom No, Scene, Durasi, Narasi, Visual, Interaksi, Keterangan/Catatan
- ✅ Siap cetak (A4, margin standar)

---

## Struktur Folder

```
storyboard-skill/
├── SKILL.md                    ← Panduan lengkap untuk Claude
├── README.md                   ← File ini
└── scripts/
    └── generate_storyboard.py  ← Script Python generator utama
```

---

## Cara Instalasi

1. Salin folder `storyboard-skill/` ke direktori skill aktif.
2. Pastikan `reportlab` tersedia di environment Python:
   ```bash
   pip install reportlab --break-system-packages
   ```
3. Skill akan otomatis terpicu saat pengguna meminta storyboard, template video pembelajaran, atau dokumen perencanaan media berbasis 9 tahap Gagne.

---

## Cara Pakai (Manual)

```bash
# Template kosong
python scripts/generate_storyboard.py output.pdf

# Atau dengan Python API
python3 - << 'EOF'
import sys
sys.path.insert(0, "./scripts")
from generate_storyboard import generate

generate(
    output_path="storyboard_hukum_kasih.pdf",
    meta={
        "judul":         "Hukum Kasih",
        "fase":          "Fase E – Pendidikan Agama Kristen",
        "tujuan":        "Peserta memahami makna hukum kasih",
        "capaian":       "CP.1.2 – Mengasihi sesama",
        "no_dokumen":    "SB-2025-001",
        "tanggal_rilis": "Juni 2025",
        "total_durasi":  "15 menit",
        "ahli_materi":   "Dr. Sinta Wulandari",
    },
    dibuat    = {"nama": "Budi Santoso, S.Pd", "nip": "NIP. 198501012010011001"},
    diperiksa = {"nama": "Dewi Rahayu, M.Pd",  "nip": "NIP. 197803042005022003"},
    disetujui = {"nama": "Prof. Yusuf Manalu",  "nip": "NIP. 196712101990031002"},
)
EOF
```

---

## Parameter

| Parameter     | Wajib | Keterangan |
|---------------|-------|-----------|
| `output_path` | ✅    | Path file PDF output |
| `meta`        | ❌    | Dict: `judul`, `fase`, `tujuan`, `capaian`, `no_dokumen`, `tanggal_rilis`, `total_durasi`, `ahli_materi` |
| `dibuat`      | ❌    | Dict: `nama`, `nip` |
| `diperiksa`   | ❌    | Dict: `nama`, `nip` |
| `disetujui`   | ❌    | Dict: `nama`, `nip` |
| `logo_path`   | ❌    | Path ke file gambar logo (PNG/JPG) |

---

## Contoh Output

Template menghasilkan 3 halaman A4 dengan layout persis seperti di bawah:

```
Halaman 1 : Kop surat + Meta + Tanda tangan + STORYBOARD bar
            + Tahap 1 (Menarik Perhatian) + Tahap 2 (Tujuan)
Halaman 2 : Tahap 3 (Pengetahuan Awal)
            + [TAHAP INTI]
            + Tahap 4, 5, 6
Halaman 3 : [TAHAP PENUTUP]
            + Tahap 7 (Feedback), 8 (Refleksi), 9 (Penguatan)
```

---

## Dependensi

| Library      | Versi Minimum | Keterangan |
|--------------|---------------|------------|
| `reportlab`  | 4.0           | Generator PDF utama (wajib) |
| `Pillow`     | 9.0           | Opsional – hanya dibutuhkan jika menyertakan logo |

---

## Catatan Desain

- Bagian **"Keterangan" event 1–9** yang ada di halaman terakhir template asli **tidak dimasukkan** sesuai permintaan.
- Font yang digunakan: **Helvetica** (built-in ReportLab – tidak perlu install font eksternal).
- Seluruh warna, ukuran kolom, dan struktur tabel direplikasi dari template PDF asli Ditjen Bimas Kristen.

---

## Lisensi

Template ini mereproduksi format dokumen resmi instansi pemerintah untuk keperluan internal.  
Gunakan sesuai ketentuan penggunaan dokumen Kementerian Agama RI.
