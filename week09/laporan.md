# Web Server Sederhana Menggunakan TCP Socket Programming

# Tujuan Praktikum

Praktikum ini bertujuan untuk membuat program web server sederhana berbasis TCP socket programming. Server dibuat menggunakan bahasa Python dan digunakan untuk menerima request HTTP dari browser, membaca file HTML, lalu mengirimkan response HTTP kembali ke client.

---

# 9.1 Pengantar

Web server merupakan aplikasi jaringan yang bertugas menerima request dari client, memproses request tersebut, kemudian mengirimkan response. Pada praktikum ini, web server dibuat menggunakan socket TCP.

TCP digunakan karena komunikasi HTTP membutuhkan koneksi yang andal antara client dan server. Dengan TCP, data dapat dikirim secara berurutan dan lebih terjamin dibandingkan UDP.

Program web server pada praktikum ini bekerja dengan alur berikut:

1. Server membuat socket TCP.
2. Server melakukan bind ke port tertentu.
3. Server menunggu koneksi dari client.
4. Browser mengirim request HTTP.
5. Server membaca file yang diminta.
6. Server mengirim response HTTP.
7. Jika file tidak ditemukan, server mengirim pesan 404 Not Found.

---

# 9.2 Source Code Web Server

File program yang dibuat adalah `WebServer.py`.

```python
from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        f = open(filename[1:])
        outputdata = f.read()

        header = 'HTTP/1.1 200 OK\r\n\r\n'
        connectionSocket.send(header.encode())

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send('\r\n'.encode())
        connectionSocket.close()

    except IOError:
        errorHeader = 'HTTP/1.1 404 Not Found\r\n\r\n'
        errorBody = '<html><body><h1>404 Not Found</h1></body></html>'

        connectionSocket.send(errorHeader.encode())
        connectionSocket.send(errorBody.encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
````

---

# 9.3 File HTML

File HTML yang digunakan bernama `HelloWorld.html`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>File ini berhasil ditampilkan melalui web server sederhana berbasis TCP socket.</p>
</body>
</html>
```

---

# 9.4 Menjalankan Server

Langkah menjalankan program:

1. Buka folder `week9` di VS Code.
2. Pastikan file `WebServer.py` dan `HelloWorld.html` berada dalam folder yang sama.
3. Jalankan server menggunakan terminal:

```bash
python WebServer.py
```

4. Jika server berhasil berjalan, terminal akan menampilkan:

```bash
Ready to serve...
```

5. Buka browser lalu akses:

```text
http://localhost:6789/HelloWorld.html
```

---

# 9.5 Hasil Percobaan

## 1. Server Berjalan di Terminal

![Server Running](assets/asset1.png)

### Analisis

Pada gambar tersebut, server berhasil dijalankan dan berada dalam kondisi siap menerima request dari client. Pesan `Ready to serve...` menunjukkan bahwa server sedang menunggu koneksi dari browser.

---

## 2. Browser Menampilkan File HTML

![HTML Berhasil Ditampilkan](assets/asset2.png)

### Analisis

Ketika browser mengakses `HelloWorld.html`, server menerima request HTTP, membaca file HTML, lalu mengirim response dengan status `200 OK`. Setelah itu, browser menampilkan isi file HTML.

---

## 3. Percobaan File Tidak Ada

URL yang dicoba:

```text
http://localhost:6789/tidakada.html
```

![404 Not Found](assets/asset3.png)

### Analisis

Ketika file yang diminta tidak tersedia di folder server, program masuk ke bagian `except IOError`. Server kemudian mengirim response `404 Not Found` ke browser.

---

## 4. Struktur Folder di VS Code

![Struktur Folder](assets/asset4.png)

### Analisis

Struktur folder dibuat sederhana agar file Python, HTML, laporan, dan screenshot tersusun rapi. Folder `assets` digunakan untuk menyimpan hasil screenshot praktikum.

---

# 9.6 Pembahasan Program

## Membuat Socket TCP

```python
serverSocket = socket(AF_INET, SOCK_STREAM)
```

Baris ini digunakan untuk membuat socket TCP. `AF_INET` menunjukkan bahwa program menggunakan IPv4, sedangkan `SOCK_STREAM` menunjukkan bahwa socket menggunakan protokol TCP.

---

## Bind Port Server

```python
serverSocket.bind(('', serverPort))
```

Baris ini digunakan untuk menghubungkan socket dengan port `6789`. Dengan begitu, server dapat menerima koneksi melalui port tersebut.

---

## Server Listening

```python
serverSocket.listen(1)
```

Baris ini membuat server berada dalam kondisi menunggu koneksi dari client.

---

## Menerima Koneksi

```python
connectionSocket, addr = serverSocket.accept()
```

Ketika browser mengirim request, server menerima koneksi tersebut melalui method `accept()`.

---

## Membaca Request HTTP

```python
message = connectionSocket.recv(1024).decode()
filename = message.split()[1]
```

Server menerima request dari browser, lalu mengambil nama file yang diminta.

---

## Mengirim Response 200 OK

```python
header = 'HTTP/1.1 200 OK\r\n\r\n'
connectionSocket.send(header.encode())
```

Jika file ditemukan, server mengirim header HTTP `200 OK` sebagai tanda bahwa request berhasil diproses.

---

## Mengirim Response 404 Not Found

```python
errorHeader = 'HTTP/1.1 404 Not Found\r\n\r\n'
```

Jika file tidak ditemukan, server mengirim response `404 Not Found`.

---

# Kesimpulan

Berdasarkan praktikum yang dilakukan, dapat disimpulkan bahwa web server sederhana dapat dibuat menggunakan TCP socket programming dengan Python.

Server bekerja dengan menerima request HTTP dari browser, membaca file yang diminta, lalu mengirimkan response kembali ke client. Jika file tersedia, server mengirim response `200 OK`. Jika file tidak tersedia, server mengirim response `404 Not Found`.

Praktikum ini menunjukkan bahwa komunikasi antara browser dan web server berjalan melalui koneksi TCP. Dengan memahami program ini, konsep dasar web server, HTTP request, HTTP response, dan socket TCP dapat dipahami dengan lebih jelas.

---

# Daftar Screenshot

| File       | Keterangan                                   |
| ---------- | -------------------------------------------- |
| asset1.png | Server berjalan di terminal                  |
| asset2.png | Browser berhasil menampilkan HelloWorld.html |
| asset3.png | Browser menampilkan 404 Not Found            |
| asset4.png | Struktur folder week9 di VS Code             |

