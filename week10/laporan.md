# Analisis Protokol IP Menggunakan Wireshark

# Tujuan Praktikum

Praktikum ini bertujuan untuk memahami cara kerja protokol IP menggunakan Wireshark, meliputi analisis IPv4, fragmentasi IP, serta pengenalan dasar IPv6.

---

# 10.1 Pengantar

Internet Protocol (IP) merupakan protokol utama pada layer network yang bertugas mengirimkan paket data dari sumber menuju tujuan melalui jaringan.

Pada praktikum ini dilakukan analisis paket IPv4 dan IPv6 menggunakan aplikasi Wireshark. Selain itu dilakukan pengamatan terhadap proses traceroute dan fragmentasi IP.

Traceroute bekerja dengan mengirim paket menggunakan nilai TTL berbeda-beda untuk mengetahui jalur router menuju tujuan.

---

# 10.2 Capture Paket Traceroute

Pada praktikum ini dilakukan capture paket menggunakan Wireshark bersamaan dengan menjalankan perintah traceroute menuju server:

```bash
traceroute gaia.cs.umass.edu 56
````

dan

```bash
traceroute gaia.cs.umass.edu 3000
```

Untuk Windows:

```bash
tracert gaia.cs.umass.edu
```

---

## Langkah Praktikum

1. Membuka Wireshark.
2. Memulai capture paket.
3. Menjalankan perintah traceroute ukuran 56 byte.
4. Menjalankan traceroute ukuran 3000 byte.
5. Menghentikan capture.
6. Melakukan analisis paket IPv4, ICMP, dan IPv6.

![Capture Traceroute](assets/asset1.png)

---

# 10.2.1 Bagian 1 - IPv4 Dasar

Filter yang digunakan:

```bash
udp || icmp
```

![Filter UDP dan ICMP](assets/asset2.png)

### Analisis

Filter tersebut digunakan untuk menampilkan paket UDP dan ICMP yang dihasilkan selama proses traceroute berlangsung.

Paket UDP dikirim oleh host menuju tujuan, sedangkan paket ICMP TTL Exceeded dikirim oleh router ketika nilai TTL mencapai nol.

---

## Analisis Paket UDP

Filter:

```bash
ip.src==[IP_CLIENT] && ip.dst==128.119.245.12 && udp && !icmp
```

![Paket UDP Traceroute](assets/asset3.png)

### Analisis

Paket UDP digunakan oleh traceroute untuk mengirim probe menuju server tujuan. Setiap paket dikirim dengan nilai TTL berbeda sehingga router yang dilewati dapat mengembalikan pesan ICMP.

---

## Analisis Paket ICMP

Filter:

```bash
ip.dst==[IP_CLIENT] && icmp
```

![Paket ICMP TTL Exceeded](assets/asset4.png)

### Analisis

Router yang menerima paket dengan TTL bernilai nol akan mengirim pesan ICMP TTL Exceeded kembali ke host pengirim.

Dari pesan ICMP tersebut dapat diketahui alamat router yang dilewati selama proses traceroute.

---

## Analisis TTL

### Analisis

Nilai TTL pada setiap paket traceroute meningkat secara bertahap:

* TTL 1
* TTL 2
* TTL 3
* dan seterusnya

Setiap router akan mengurangi TTL sebesar 1 sebelum meneruskan paket ke router berikutnya.

Jika TTL mencapai nol, router akan membuang paket dan mengirim ICMP TTL Exceeded.

---

# 10.2.2 Bagian 2 - Fragmentasi IP

Pada bagian ini dilakukan analisis terhadap paket traceroute berukuran besar yaitu 3000 byte.

![Fragmentasi IP](assets/asset5.png)

### Analisis

Karena ukuran paket lebih besar dari MTU jaringan, datagram IP akan dipecah menjadi beberapa fragmen.

Setiap fragmen memiliki:

* Identification yang sama
* Fragment Offset berbeda
* Flag fragment tertentu

Tujuan fragmentasi adalah agar paket dapat melewati jaringan dengan batas ukuran frame tertentu.

---

## Identification Field

### Analisis

Field Identification digunakan untuk menandai bahwa beberapa fragmen berasal dari datagram IP yang sama.

Ketika seluruh fragmen diterima, host tujuan akan melakukan proses reassembly berdasarkan nilai Identification tersebut.

---

## Fragment Offset

### Analisis

Fragment Offset digunakan untuk menunjukkan posisi fragmen pada datagram asli.

Dengan informasi offset, host tujuan dapat menyusun ulang seluruh fragmen sesuai urutannya.

---

## More Fragment Flag

### Analisis

Flag MF (More Fragment) digunakan untuk menunjukkan apakah masih terdapat fragmen lain setelah fragmen tersebut.

* MF = 1 → masih ada fragmen berikutnya
* MF = 0 → fragmen terakhir

---

# 10.2.3 Bagian 3 - IPv6

Pada bagian ini dilakukan analisis paket IPv6 menggunakan file capture yang telah disediakan.

![Paket IPv6](assets/asset6.png)

### Analisis

IPv6 merupakan pengembangan dari IPv4 dengan ukuran alamat 128 bit sehingga menyediakan jumlah alamat jauh lebih besar.

Selain itu, IPv6 memiliki struktur header yang lebih sederhana dibandingkan IPv4.

---

## Analisis DNS IPv6

Paket yang diamati merupakan DNS request tipe AAAA.

![DNS IPv6](assets/asset7.png)

### Analisis

Request DNS tipe AAAA digunakan untuk mencari alamat IPv6 dari suatu domain.

Pada praktikum ini dilakukan request terhadap domain youtube.com untuk memperoleh alamat IPv6 miliknya.

---

## Perbedaan IPv4 dan IPv6

| IPv4                   | IPv6                       |
| ---------------------- | -------------------------- |
| 32 bit                 | 128 bit                    |
| Menggunakan NAT        | Tidak membutuhkan NAT      |
| Header lebih kompleks  | Header lebih sederhana     |
| Jumlah alamat terbatas | Jumlah alamat sangat besar |

![Perbandingan IPv4 dan IPv6](assets/asset8.png)

---

# Kesimpulan

Berdasarkan hasil praktikum, dapat diketahui bahwa protokol IP berfungsi untuk mengirimkan paket data antar jaringan menggunakan alamat IP sebagai identitas host.

Pada analisis traceroute terlihat bahwa nilai TTL digunakan untuk menentukan jalur router yang dilewati paket menuju tujuan. Ketika TTL habis, router akan mengirim pesan ICMP TTL Exceeded.

Selain itu, paket IP berukuran besar dapat mengalami fragmentasi apabila ukuran paket melebihi MTU jaringan. Proses fragmentasi menggunakan field Identification, Fragment Offset, dan More Fragment.

Pada bagian IPv6 terlihat bahwa IPv6 memiliki jumlah alamat jauh lebih besar dibandingkan IPv4 serta struktur header yang lebih sederhana.

Dengan demikian, praktikum ini membantu memahami proses kerja protokol IP baik pada IPv4 maupun IPv6.

---

# Daftar Screenshot

| File       | Keterangan                 |
| ---------- | -------------------------- |
| asset1.png | Capture traceroute         |
| asset2.png | Filter UDP dan ICMP        |
| asset3.png | Paket UDP traceroute       |
| asset4.png | Paket ICMP TTL Exceeded    |
| asset5.png | Fragmentasi IP             |
| asset6.png | Paket IPv6                 |
| asset7.png | DNS request AAAA           |
| asset8.png | Perbandingan IPv4 dan IPv6 |
