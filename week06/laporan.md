# Analisis Protokol TCP Menggunakan Wireshark

# Tujuan Praktikum

Praktikum ini bertujuan untuk memahami cara kerja protokol TCP menggunakan Wireshark. Selain itu, praktikum dilakukan untuk menganalisis proses komunikasi TCP seperti three-way handshake, sequence number, acknowledgement, retransmission, flow control, congestion control, throughput, dan round trip time.

---

# 6.1 Pengantar

TCP atau Transmission Control Protocol merupakan protokol layer transport yang bersifat connection-oriented dan reliable. TCP digunakan untuk memastikan data dapat dikirim dengan urut, lengkap, dan tanpa error.

Berbeda dengan UDP, TCP memiliki mekanisme seperti:

- Three-way handshake
- Acknowledgement
- Retransmission
- Flow control
- Congestion control

Pada praktikum ini dilakukan analisis transfer file menggunakan metode HTTP POST untuk melihat bagaimana TCP bekerja dalam proses pengiriman data berukuran besar.

---

# 6.2 Capture Transfer TCP

Pada praktikum ini dilakukan upload file `alice.txt` ke server:

```text
http://gaia.cs.umass.edu
````

Capture dilakukan menggunakan Wireshark selama proses upload berlangsung.

Langkah praktikum:

1. Mengunduh file `alice.txt`.
2. Membuka halaman upload file.
3. Menjalankan Wireshark.
4. Memulai capture paket.
5. Mengunggah file menggunakan HTTP POST.
6. Menghentikan capture.

![Capture TCP](assets/asset1.png)

---

# 6.3 Analisis Awal Trace TCP

Filter yang digunakan pada Wireshark:

```bash
tcp
```

Setelah filter diterapkan, terlihat komunikasi TCP antara client dan server gaia.cs.umass.edu.

![Filter TCP](assets/asset2.png)

---

## Pertanyaan 6.3

### 1. IP Address dan Port TCP Client

IP Address client:

```text
[Isi IP client]
```

Port TCP client:

```text
[Isi port TCP client]
```

### Analisis

Port yang digunakan client biasanya berupa ephemeral port atau port acak yang dipilih sistem operasi untuk komunikasi sementara.

---

### 2. IP Address dan Port Server

IP Address server gaia.cs.umass.edu:

```text
[Isi IP server]
```

Port TCP server:

```text
80
```

### Analisis

Server menggunakan port 80 karena proses upload dilakukan menggunakan protokol HTTP.

---

### 3. IP dan Port TCP Client Sendiri

IP client:

```text
[Isi IP client]
```

Port TCP:

```text
[Isi port TCP]
```

---

# 6.4 Dasar TCP

## 1. Sequence Number Segmen SYN

Sequence Number SYN:

```text
[Isi sequence number]
```

Segmen dapat dikenali sebagai SYN karena memiliki flag:

```text
SYN = 1
```

![Segmen SYN](assets/asset3.png)

### Analisis

Segmen SYN digunakan untuk memulai koneksi TCP antara client dan server dalam proses three-way handshake.

---

## 2. Sequence Number Segmen SYNACK

Sequence Number SYNACK:

```text
[Isi sequence number]
```

Acknowledgement Number:

```text
[Isi acknowledgement]
```

Flag yang aktif:

```text
SYN = 1
ACK = 1
```

![Segmen SYNACK](assets/asset4.png)

### Analisis

Server menentukan acknowledgement number dengan menambahkan 1 pada sequence number milik client sebelumnya.

---

## 3. Sequence Number HTTP POST

Sequence Number segmen HTTP POST:

```text
[Isi sequence number]
```

![HTTP POST](assets/asset5.png)

### Analisis

Segmen ini membawa data HTTP POST yang digunakan untuk mengunggah file ke server.

---

## 4. Sequence Number dan RTT

| Segmen | Sequence Number | Waktu Kirim | Waktu ACK | RTT   |
| ------ | --------------- | ----------- | --------- | ----- |
| 1      | [Isi]           | [Isi]       | [Isi]     | [Isi] |
| 2      | [Isi]           | [Isi]       | [Isi]     | [Isi] |
| 3      | [Isi]           | [Isi]       | [Isi]     | [Isi] |
| 4      | [Isi]           | [Isi]       | [Isi]     | [Isi] |
| 5      | [Isi]           | [Isi]       | [Isi]     | [Isi] |
| 6      | [Isi]           | [Isi]       | [Isi]     | [Isi] |

![RTT TCP](assets/asset6.png)

### Analisis

RTT atau Round Trip Time menunjukkan waktu yang dibutuhkan paket untuk dikirim hingga acknowledgement diterima kembali.

Nilai RTT dipengaruhi oleh delay jaringan, jarak server, dan kondisi lalu lintas jaringan.

---

## 5. Panjang Enam Segmen TCP Pertama

| Segmen | Panjang |
| ------ | ------- |
| 1      | [Isi]   |
| 2      | [Isi]   |
| 3      | [Isi]   |
| 4      | [Isi]   |
| 5      | [Isi]   |
| 6      | [Isi]   |

### Analisis

Ukuran segmen TCP dapat berbeda tergantung jumlah data yang dibawa pada payload.

---

## 6. Buffer Penerima TCP

Ukuran minimum buffer penerima:

```text
[Isi ukuran buffer]
```

### Analisis

Buffer digunakan untuk menyimpan data sementara sebelum diproses oleh receiver. Jika buffer penuh, receiver dapat memperlambat pengiriman data menggunakan flow control.

---

## 7. Retransmission TCP

Apakah terdapat retransmission?

```text
[Ya / Tidak]
```

### Analisis

Retransmission dapat dikenali melalui:

* Sequence number yang sama
* Label retransmission pada Wireshark
* ACK yang terlambat atau duplicate ACK

![Retransmission](assets/asset7.png)

---

## 8. ACK pada TCP

Jumlah data yang di-ACK:

```text
[Isi jumlah byte]
```

### Analisis

Receiver biasanya melakukan cumulative ACK terhadap beberapa segmen sekaligus untuk meningkatkan efisiensi komunikasi.

---

## 9. Throughput TCP

Throughput:

```text
[Isi hasil throughput]
```

### Cara Perhitungan

```text
Throughput = Total Data / Total Waktu Transfer
```

### Analisis

Semakin besar throughput, semakin cepat proses transfer data berlangsung.

---

# 6.5 Congestion Control TCP

Pada bagian ini digunakan fitur:

```text
Statistics -> TCP Stream Graph -> Time-Sequence-Graph (Stevens)
```

![Time Sequence Graph](assets/asset8.png)

---

## 1. Analisis Slow Start dan Congestion Avoidance

### Slow Start

Fase slow start terlihat ketika jumlah data yang dikirim meningkat secara cepat pada awal koneksi.

### Congestion Avoidance

Setelah mencapai batas tertentu, pertumbuhan pengiriman data menjadi lebih stabil dan linear.

### Analisis

Mekanisme congestion control digunakan TCP untuk menghindari kemacetan jaringan dengan mengatur jumlah data yang dikirim.

---

## 2. Analisis Berdasarkan Trace Sendiri

Berdasarkan hasil trace yang diperoleh, fase slow start dan congestion avoidance dapat diamati dari perubahan pola grafik sequence number terhadap waktu.

![Grafik TCP](assets/asset9.png)

### Analisis

Pada awal komunikasi, TCP meningkatkan congestion window secara bertahap. Setelah mendekati kapasitas jaringan, pertumbuhan window menjadi lebih lambat untuk mengurangi kemungkinan congestion.

---

# Kesimpulan

Berdasarkan hasil praktikum, dapat diketahui bahwa TCP merupakan protokol transport yang menyediakan komunikasi andal melalui mekanisme acknowledgement, retransmission, flow control, dan congestion control.

Proses komunikasi TCP dimulai dengan three-way handshake menggunakan segmen SYN, SYNACK, dan ACK. Selanjutnya data dikirim menggunakan sequence number dan dikontrol menggunakan acknowledgement.

Dari hasil analisis Wireshark juga terlihat bahwa TCP memiliki mekanisme congestion control seperti slow start dan congestion avoidance untuk menjaga stabilitas jaringan selama transfer data berlangsung.

Dengan demikian, TCP sangat cocok digunakan pada layanan yang membutuhkan reliabilitas tinggi seperti HTTP, FTP, dan email.

---

# Daftar Screenshot

| File       | Keterangan                |
| ---------- | ------------------------- |
| asset1.png | Capture upload TCP        |
| asset2.png | Filter TCP                |
| asset3.png | Segmen SYN                |
| asset4.png | Segmen SYNACK             |
| asset5.png | HTTP POST                 |
| asset6.png | RTT TCP                   |
| asset7.png | Retransmission TCP        |
| asset8.png | Time Sequence Graph       |
| asset9.png | Grafik congestion control |