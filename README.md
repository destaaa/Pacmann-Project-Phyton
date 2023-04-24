# _Self-service Cashier System_
## Background Project
Andi merupakan pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana perbaikan proses bisnis yaitu membuat sistem kasir _self-service_ yang daat memberikan kemudahan kepada para customer termasuk dalam melakukan transaksi jarak jauh. Dengan adanya sistem kasir ini, diharapkan customer dapat dengan mudah memanambahkan produk dalam daftar belanja, melakukan perubahan terhadap daftar belanja dan aktivitas transaksi lainnya melalui sistem kasir yang dibuat

## Objective & Requirements
Sistem kasir pada supermarket Andi dibuat dengan sistem _self-service_, dimana customer dapat melakukan transaksi secara mandiri dengan fitur-fitur sebagai berikut: 
1. Customer dapat membuat ID transaksi.
2. Customer dapat memasukkan atau menambahkan barang yang dibeli, jumlah dan harga barang.
3. Customer dapat melakukan perubahan pada nama produk/item yang telah dimasukkan ke daftar belanja.
4. Customer dapat melakukan perubahan pada jumlah produk/item yang telah dimasukkan ke daftar belanja.
5. Customer dapat melakukan perubahan pada harga produk/item yang telah dimasukkan ke daftar belanja.
6. Customer dapat menghapus nama produk/item yang telah dimasukkan ke daftar belanja.
7. Customer dapat melihat daftar belanja yang dibuat.
8. Customer dapat mereset daftar belanja.
9. Customer dapat melakukan pembayaran atas pembelian.

## Flowchart
![alt text](https://github.com/destaaa/PacmannProject/blob/main/images/Flowchart.png?raw=true)
### Penjelasan Kode Program
* `Transaction` : Class untuk menyimpan seluruh method untuk menjalankan proses transaksi.
* `add_item()` : Method dari 'class Transaction' untuk melakukan penambahan nama item, jumlah dan harga ke dalam daftar belanja.
* `update_item_name()` : Method dari 'class Transaction' untuk melakukan update/perubahan pada nama item yang telah dimasukkan ke dalam daftar belanja.
* `update_item_qty()` : Method dari 'class Transaction' untuk melakukan update/perubahan pada jumlah item yang telah dimasukkan ke dalam daftar belanja.
* `update_item_price()` : Method dari 'class Transaction' untuk melakukan update/perubahan pada harga item yang telah dimasukkan ke dalam daftar belanja.
* `delete_item()` : Method dari 'class Transaksi' untuk menghapus salah satu item besert jumlah dan harganya.
* `reset_transaction()` : Method dari 'class Transaction' untuk mereset/mengosongkan daftar belanja.
* `check_order()` : Method dari 'class Transaction' untuk menampilkan daftar belanja.
* `total_purchase()` : Method dari 'class Transaction' untuk menampilkan total pembelian daftar belanja.
* `pay_checkout()` : Method dari 'class Transaction' untuk melakukan pembayaran daftar belanja.

## Test Case
### Test Case 1
Customer ingin menambahkan 2 item baru menggunakan method `add_item()`. Item yang ditambahkan adalah sebagai berikut:
* Nama item: Ayam goreng, Qty: 2, Harga: 20000
* Nama item: Pasta gigi, Qty: 3, Harga: 15000

Daftar belanja setelah ditambahkan:

### Test Case 2
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menggunakan method `delete_item()` untuk menghapus item. Item yang ingin dihapus adalah Pasta gigi.

Daftar belanja setelah diperbarui:

### Test Case 3
Ternyata setelah dipikir-pikir Customer salah memasukkan item yang ingin dibelanjakan. Daripada menghapusnya satu-satu, maka Customer cukup menggunakan method `reset_transaction()` untuk menghapus semua item yang sudah ditambahkan.

Daftar belanja setelah diperbarui:

### Test Case 4
setelah Customer selesai berbelanja, maka akan menghitung total belanja yang harus dibayarkan menggunakan method `total_purchase'. Sebelum mengeluarkan output total akan menampilkan daftar belanja.

Daftar belanja setelah diperbarui:

