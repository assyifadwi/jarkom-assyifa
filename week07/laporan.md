# Socket Programming Menggunakan UDP dan TCP

# Tujuan Praktikum

1. Mahasiswa dapat membuat program berbasis socket UDP.
2. Mahasiswa dapat membuat program berbasis socket TCP.

---

# 7.1 Pengantar

Socket programming digunakan untuk membangun komunikasi antara client dan server pada jaringan komputer. Pada praktikum ini digunakan bahasa Python untuk membuat aplikasi jaringan sederhana berbasis UDP dan TCP.

UDP bersifat connectionless sehingga proses komunikasi berlangsung tanpa membuat koneksi terlebih dahulu. Sedangkan TCP bersifat connection-oriented karena menggunakan proses handshake sebelum data dikirim.

Pada praktikum ini dibuat aplikasi sederhana dengan mekanisme berikut:

1. Client mengirim kalimat ke server.
2. Server menerima data dari client.
3. Server mengubah huruf menjadi uppercase.
4. Server mengirim kembali hasil ke client.
5. Client menampilkan hasil dari server.

---

# 7.2 Socket Programming Menggunakan UDP

## Source Code UDP Client

```python
from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input('Input lowercase sentence: ')

clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print('From Server:', modifiedMessage.decode())

clientSocket.close()
````

---

## Source Code UDP Server

```python
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print('UDP Server Ready')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)

    modifiedMessage = message.decode().upper()

    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
```

---

## Hasil Running UDP

![Running UDP](assets/asset1.png)

### Analisis

Pada komunikasi UDP, client langsung mengirim data ke server tanpa membuat koneksi terlebih dahulu. Data dikirim menggunakan method `sendto()` dan diterima menggunakan `recvfrom()`.

Server menerima data dari client, kemudian mengubah seluruh huruf menjadi uppercase menggunakan fungsi `upper()` sebelum dikirim kembali ke client.

Karena UDP bersifat connectionless, proses komunikasi berlangsung lebih sederhana dan cepat.

---

# 7.3 Socket Programming Menggunakan TCP

## Source Code TCP Client

```python
from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))

sentence = input('Input lowercase sentence: ')

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(2048)

print('From Server:', modifiedSentence.decode())

clientSocket.close()
```

---

## Source Code TCP Server

```python
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))

serverSocket.listen(1)

print('TCP Server Ready')

while True:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(2048).decode()

    modifiedSentence = sentence.upper()

    connectionSocket.send(modifiedSentence.encode())

    connectionSocket.close()
```

---

## Hasil Running TCP

![Running TCP](assets/asset2.png)

### Analisis

Berbeda dengan UDP, TCP menggunakan koneksi antara client dan server sebelum data dikirim. Koneksi dibuat menggunakan method `connect()` pada client dan `accept()` pada server.

TCP menjamin data diterima secara urut dan lengkap sehingga lebih andal dibanding UDP.

Pada program ini server menerima data dari client, mengubah huruf menjadi uppercase, kemudian mengirim hasil kembali melalui koneksi TCP yang sudah terbentuk.

---

# Perbedaan UDP dan TCP

| UDP                          | TCP                    |
| ---------------------------- | ---------------------- |
| Connectionless               | Connection-oriented    |
| Tidak ada handshake          | Menggunakan handshake  |
| Lebih cepat                  | Lebih andal            |
| Tidak menjamin data diterima | Menjamin data diterima |
| Menggunakan sendto()         | Menggunakan send()     |

---

# Kesimpulan

Berdasarkan hasil praktikum, dapat diketahui bahwa socket programming memungkinkan komunikasi antara client dan server pada jaringan komputer.

UDP menggunakan komunikasi tanpa koneksi sehingga proses pengiriman data lebih cepat dan sederhana. Sedangkan TCP menggunakan koneksi yang membuat proses komunikasi lebih andal karena data dijamin diterima dengan benar.

Melalui praktikum ini dapat dipahami cara membuat aplikasi jaringan sederhana menggunakan Python dengan protokol UDP maupun TCP.

---

# Daftar Screenshot

| File       | Keterangan             |
| ---------- | ---------------------- |
| asset1.png | Running program UDP    |
| asset2.png | Running program TCP    |
| asset3.png | Source code UDP Client |
| asset4.png | Source code UDP Server |
| asset5.png | Source code TCP Client |
| asset6.png | Source code TCP Server |