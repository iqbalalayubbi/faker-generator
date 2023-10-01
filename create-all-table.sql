CREATE TABLE `kategori` (
  `kode` varchar(20) PRIMARY KEY,
  `jenis` varchar(100)
);

CREATE TABLE `role` (
  `id` integer PRIMARY KEY,
  `nama` varchar(100)
);

CREATE TABLE `pelanggan` (
  `id` integer PRIMARY KEY,
  `nama` varchar(100),
  `jenis_kelamin` char(1),
  `nomor_telepon` varchar(20),
  `alamat` text
);

CREATE TABLE `metode_pembayaran` (
  `kode` varchar(20) PRIMARY KEY,
  `nama` varchar(50),
  `jenis` varchar(50)
);

CREATE TABLE `akun` (
  `username` varchar(50) PRIMARY KEY,
  `password` varchar(50),
  `email` varchar(50),
  `jenis_kelamin` char(1),
  `nomor_telepon` varchar(20),
  `alamat` text,
  `id_role` integer
);

CREATE TABLE `barang` (
  `kode` varchar(20) PRIMARY KEY,
  `barcode` varchar(20),
  `nama` varchar(50),
  `harga_beli` decimal(10,3),
  `harga_jual` decimal(10,3),
  `berat` decimal(10,3),
  `stok` integer,
  `kode_kategori` varchar(20)
);

CREATE TABLE `supplier` (
  `id` integer PRIMARY KEY,
  `nama` varchar(50),
  `alamat` text,
  `nomor_telepon` varchar(20),
  `perusahaan` varchar(100)
);

CREATE TABLE `pembelian` (
  `kode` varchar(20) PRIMARY KEY,
  `waktu` datetime,
  `biaya_kirim` decimal(10,3),
  `id_supplier` integer,
  `username_akun` varchar(50)
);

CREATE TABLE `detail_pembelian` (
  `kode` varchar(20) PRIMARY KEY,
  `harga` decimal(10,3),
  `jumlah` decimal(5,3),
  `kode_pembelian` varchar(20),
  `kode_barang` varchar(20)
);

CREATE TABLE `transaksi` (
  `kode` varchar(20) PRIMARY KEY,
  `waktu` datetime,
  `username_akun` varchar(50),
  `kode_metode_pembayaran` varchar(20),
  `id_pelanggan` integer
);

CREATE TABLE `detail_transaksi` (
  `kode` varchar(20) PRIMARY KEY,
  `harga` decimal(10,3),
  `jumlah` decimal(5,3),
  `kode_transaksi` varchar(20),
  `kode_barang` varchar(20)
);

ALTER TABLE `akun` ADD FOREIGN KEY (`id_role`) REFERENCES `role` (`id`);

ALTER TABLE `barang` ADD FOREIGN KEY (`kode_kategori`) REFERENCES `kategori` (`kode`);

ALTER TABLE `pembelian` ADD FOREIGN KEY (`id_supplier`) REFERENCES `supplier` (`id`);

ALTER TABLE `pembelian` ADD FOREIGN KEY (`username_akun`) REFERENCES `akun` (`username`);

ALTER TABLE `detail_pembelian` ADD FOREIGN KEY (`kode_pembelian`) REFERENCES `pembelian` (`kode`);

ALTER TABLE `detail_pembelian` ADD FOREIGN KEY (`kode_barang`) REFERENCES `barang` (`kode`);

ALTER TABLE `transaksi` ADD FOREIGN KEY (`username_akun`) REFERENCES `akun` (`username`);

ALTER TABLE `transaksi` ADD FOREIGN KEY (`kode_metode_pembayaran`) REFERENCES `metode_pembayaran` (`kode`);

ALTER TABLE `transaksi` ADD FOREIGN KEY (`id_pelanggan`) REFERENCES `pelanggan` (`id`);

ALTER TABLE `detail_transaksi` ADD FOREIGN KEY (`kode_transaksi`) REFERENCES `transaksi` (`kode`);

ALTER TABLE `detail_transaksi` ADD FOREIGN KEY (`kode_barang`) REFERENCES `barang` (`kode`);
