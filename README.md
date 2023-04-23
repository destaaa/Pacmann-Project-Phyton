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
* `Transaksi` : Class untuk menyimpan seluruh method untuk menjalankan proses transaksi.
* `add_item()` : Method dari 'class Transaksi' untuk melakukan penambahan nama item, jumlah dan harga ke dalam daftar belanja.
* `update_item_name()` : Function dari 'class Transaksi' untuk melakukan update/perubahan pada nama item yang telah dimasukkan ke dalam daftar belanja.
* `update_item_qty()` : Function dari 'class Transaksi' untuk melakukan update/perubahan pada jumlah item yang telah dimasukkan ke dalam daftar belanja.
* `update_item_price()` : Function dari 'class Transaksi' untuk melakukan update/perubahan pada harga item yang telah dimasukkan ke dalam daftar belanja.
* `delete_item()` : Function dari 'class Transaksi' untuk menghapus salah satu item besert jumlah dan harganya.
* `reset_transaction()` : Function dari 'class Transaksi' untuk mereset/mengosongkan daftar belanja.
* `check_order()` : Function dari 'class Transaksi' untuk menampilkan daftar belanja.
* `total_purchase()` : Function dari 'class Transaksi' untuk menampilkan total pembelian daftar belanja.
* `pay_checkout()` : Function dari 'class Transaksi' untuk melakukan pembayaran daftar belanja.

## Test Case
