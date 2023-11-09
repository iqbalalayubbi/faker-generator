/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     11/2/2023 11:36:23 AM                        */
/*==============================================================*/


drop table if exists AKUN;

drop table if exists BARANG;

drop table if exists KATEGORI;

drop table if exists MEMBER;

drop table if exists METODE_PEMBAYARAN;

drop table if exists RESTOCK;

drop table if exists SUPPLIER;

drop table if exists TRANSAKSI;

/*==============================================================*/
/* Table: AKUN                                                  */
/*==============================================================*/
create table AKUN
(
   USERNAME_AKUN        varchar(50) not null,
   PASSWORD_AKUN        varchar(50),
   EMAIL_AKUN           varchar(50),
   JENIS_KELAMIN_AKUN   varchar(1),
   NOMOR_TELEPON_AKUN   varchar(20),
   ALAMAT_AKUN          longtext,
   ROLE                 varchar(50),
   primary key (USERNAME_AKUN)
);

/*==============================================================*/
/* Table: BARANG                                                */
/*==============================================================*/
create table BARANG
(
   KODE_BARANG          varchar(20) not null,
   KODE_KATEGORI        varchar(20),
   BARCODE_BARANG       varchar(20),
   NAMA_BARANG          varchar(50),
   HARGA_BELI_BARANG    decimal(10,3),
   HARGA_JUAL_BARANG    decimal(10,3),
   BERAT_BARANG         decimal(10,3),
   STOK_BARANG          int,
   primary key (KODE_BARANG)
);

/*==============================================================*/
/* Table: KATEGORI                                              */
/*==============================================================*/
create table KATEGORI
(
   KODE_KATEGORI        varchar(20) not null,
   JENIS_KATEGORI       varchar(100),
   primary key (KODE_KATEGORI)
);

/*==============================================================*/
/* Table: MEMBER                                                */
/*==============================================================*/
create table MEMBER
(
   ID_MEMBER            int not null,
   NAMA_MEMBER          varchar(100),
   JENIS_KELAMIN_MEMBER char(1),
   NOMOR_TELEPON_MEMBER varchar(20),
   ALAMAT_MEMBER        longtext,
   primary key (ID_MEMBER)
);

/*==============================================================*/
/* Table: METODE_PEMBAYARAN                                     */
/*==============================================================*/
create table METODE_PEMBAYARAN
(
   KODE_METODE_PEMBAYARAN varchar(20) not null,
   NAMA_METODE_PEMBAYARAN varchar(50),
   JENIS_METODE_PEMBAYARAN varchar(50),
   primary key (KODE_METODE_PEMBAYARAN)
);

/*==============================================================*/
/* Table: RESTOCK                                               */
/*==============================================================*/
create table RESTOCK
(
   KODE_RESTOCK         varchar(20) not null,
   ID_SUPPLIER          int,
   KODE_BARANG          varchar(20),
   USERNAME_AKUN        varchar(50),
   WAKTU_RESTOCK        timestamp,
   BIAYA_KIRIM_RESTOCK  decimal(10,3),
   HARGA_RESTOCK        decimal(10,3),
   TOTAL_BARANG_RESTOCK int,
   primary key (KODE_RESTOCK)
);

/*==============================================================*/
/* Table: SUPPLIER                                              */
/*==============================================================*/
create table SUPPLIER
(
   ID_SUPPLIER          int not null,
   NAMA_SUPPLIER        varchar(50),
   ALAMAT_SUPPLIER      longtext,
   NOMOR_TELEPON_SUPPLIER varchar(20),
   PERUSAHAAN_SUPPLIER  varchar(100),
   primary key (ID_SUPPLIER)
);

/*==============================================================*/
/* Table: TRANSAKSI                                             */
/*==============================================================*/
create table TRANSAKSI
(
   KODE_TRANSAKSI       varchar(20) not null,
   KODE_BARANG          varchar(20),
   ID_MEMBER            int,
   USERNAME_AKUN        varchar(50),
   KODE_METODE_PEMBAYARAN varchar(20),
   WAKTU_TRANSAKSI      timestamp,
   HARGA_TRANSAKSI      decimal(10,3),
   TOTAL_TRANSAKSI      decimal(10,3),
   primary key (KODE_TRANSAKSI)
);

alter table BARANG add constraint FK_BARANG_TERMASUK_KATEGORI foreign key (KODE_KATEGORI)
      references KATEGORI (KODE_KATEGORI) on delete restrict on update restrict;

alter table RESTOCK add constraint FK_AKUN_MENERIMA_RESTOCK foreign key (USERNAME_AKUN)
      references AKUN (USERNAME_AKUN) on delete restrict on update restrict;

alter table RESTOCK add constraint FK_BARANG_TERMASUK_RESTOCK foreign key (KODE_BARANG)
      references BARANG (KODE_BARANG) on delete restrict on update restrict;

alter table RESTOCK add constraint FK_SUPPLIER_MEMBUAT_RESTOCK foreign key (ID_SUPPLIER)
      references SUPPLIER (ID_SUPPLIER) on delete restrict on update restrict;

alter table TRANSAKSI add constraint FK_AKUN_MEMBUAT_TRANSAKSI foreign key (USERNAME_AKUN)
      references AKUN (USERNAME_AKUN) on delete restrict on update restrict;

alter table TRANSAKSI add constraint FK_BARANG_TERMASUK_TRANSAKSI foreign key (KODE_BARANG)
      references BARANG (KODE_BARANG) on delete restrict on update restrict;

alter table TRANSAKSI add constraint FK_MEMBER_MELAKUKAN_TRANSAKSI foreign key (ID_MEMBER)
      references MEMBER (ID_MEMBER) on delete restrict on update restrict;

alter table TRANSAKSI add constraint FK_TRANSAKSI_MEMILIH_METODE_PEMBAYARAN foreign key (KODE_METODE_PEMBAYARAN)
      references METODE_PEMBAYARAN (KODE_METODE_PEMBAYARAN) on delete restrict on update restrict;

