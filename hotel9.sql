PGDMP  :                     |            hotel9    16.1    16.0 0               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    32893    hotel9    DATABASE     �   CREATE DATABASE hotel9 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Chinese (Traditional)_Taiwan.950';
    DROP DATABASE hotel9;
                postgres    false                        2615    32894    hotel9    SCHEMA        CREATE SCHEMA hotel9;
    DROP SCHEMA hotel9;
                postgres    false            �            1259    32896    booking    TABLE     
  CREATE TABLE hotel9.booking (
    booking_id integer NOT NULL,
    guest_id integer NOT NULL,
    room_number character varying(45) NOT NULL,
    check_in_date date NOT NULL,
    check_out_date date NOT NULL,
    booking_date timestamp without time zone NOT NULL
);
    DROP TABLE hotel9.booking;
       hotel9         heap    postgres    false    5            �            1259    32895    booking_booking_id_seq    SEQUENCE     �   CREATE SEQUENCE hotel9.booking_booking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE hotel9.booking_booking_id_seq;
       hotel9          postgres    false    216    5                       0    0    booking_booking_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE hotel9.booking_booking_id_seq OWNED BY hotel9.booking.booking_id;
          hotel9          postgres    false    215            �            1259    32943    booking_has_guest    TABLE     x   CREATE TABLE hotel9.booking_has_guest (
    booking_booking_id integer NOT NULL,
    guest_guest_id integer NOT NULL
);
 %   DROP TABLE hotel9.booking_has_guest;
       hotel9         heap    postgres    false    5            �            1259    32941 (   booking_has_guest_booking_booking_id_seq    SEQUENCE     �   CREATE SEQUENCE hotel9.booking_has_guest_booking_booking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ?   DROP SEQUENCE hotel9.booking_has_guest_booking_booking_id_seq;
       hotel9          postgres    false    225    5                       0    0 (   booking_has_guest_booking_booking_id_seq    SEQUENCE OWNED BY     u   ALTER SEQUENCE hotel9.booking_has_guest_booking_booking_id_seq OWNED BY hotel9.booking_has_guest.booking_booking_id;
          hotel9          postgres    false    223            �            1259    32942 $   booking_has_guest_guest_guest_id_seq    SEQUENCE     �   CREATE SEQUENCE hotel9.booking_has_guest_guest_guest_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE hotel9.booking_has_guest_guest_guest_id_seq;
       hotel9          postgres    false    5    225                        0    0 $   booking_has_guest_guest_guest_id_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE hotel9.booking_has_guest_guest_guest_id_seq OWNED BY hotel9.booking_has_guest.guest_guest_id;
          hotel9          postgres    false    224            �            1259    32925    booking_has_room    TABLE     �   CREATE TABLE hotel9.booking_has_room (
    booking_booking_id integer NOT NULL,
    room_room_number character varying(4) NOT NULL
);
 $   DROP TABLE hotel9.booking_has_room;
       hotel9         heap    postgres    false    5            �            1259    32924 '   booking_has_room_booking_booking_id_seq    SEQUENCE     �   CREATE SEQUENCE hotel9.booking_has_room_booking_booking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE hotel9.booking_has_room_booking_booking_id_seq;
       hotel9          postgres    false    5    222            !           0    0 '   booking_has_room_booking_booking_id_seq    SEQUENCE OWNED BY     s   ALTER SEQUENCE hotel9.booking_has_room_booking_booking_id_seq OWNED BY hotel9.booking_has_room.booking_booking_id;
          hotel9          postgres    false    221            �            1259    32903    guest    TABLE     �   CREATE TABLE hotel9.guest (
    guest_id integer NOT NULL,
    guest_name character varying(45) NOT NULL,
    contact_info character varying(45) NOT NULL
);
    DROP TABLE hotel9.guest;
       hotel9         heap    postgres    false    5            �            1259    32902    guest_guest_id_seq    SEQUENCE     �   CREATE SEQUENCE hotel9.guest_guest_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE hotel9.guest_guest_id_seq;
       hotel9          postgres    false    5    218            "           0    0    guest_guest_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE hotel9.guest_guest_id_seq OWNED BY hotel9.guest.guest_id;
          hotel9          postgres    false    217            �            1259    32914    room    TABLE     z   CREATE TABLE hotel9.room (
    room_number character varying(4) NOT NULL,
    room_type character varying(20) NOT NULL
);
    DROP TABLE hotel9.room;
       hotel9         heap    postgres    false    5            �            1259    32909 	   room_type    TABLE     �   CREATE TABLE hotel9.room_type (
    room_type character varying(20) NOT NULL,
    price_per_night character varying(45) NOT NULL
);
    DROP TABLE hotel9.room_type;
       hotel9         heap    postgres    false    5            h           2604    32899    booking booking_id    DEFAULT     x   ALTER TABLE ONLY hotel9.booking ALTER COLUMN booking_id SET DEFAULT nextval('hotel9.booking_booking_id_seq'::regclass);
 A   ALTER TABLE hotel9.booking ALTER COLUMN booking_id DROP DEFAULT;
       hotel9          postgres    false    216    215    216            k           2604    32946 $   booking_has_guest booking_booking_id    DEFAULT     �   ALTER TABLE ONLY hotel9.booking_has_guest ALTER COLUMN booking_booking_id SET DEFAULT nextval('hotel9.booking_has_guest_booking_booking_id_seq'::regclass);
 S   ALTER TABLE hotel9.booking_has_guest ALTER COLUMN booking_booking_id DROP DEFAULT;
       hotel9          postgres    false    225    223    225            l           2604    32947     booking_has_guest guest_guest_id    DEFAULT     �   ALTER TABLE ONLY hotel9.booking_has_guest ALTER COLUMN guest_guest_id SET DEFAULT nextval('hotel9.booking_has_guest_guest_guest_id_seq'::regclass);
 O   ALTER TABLE hotel9.booking_has_guest ALTER COLUMN guest_guest_id DROP DEFAULT;
       hotel9          postgres    false    224    225    225            j           2604    32928 #   booking_has_room booking_booking_id    DEFAULT     �   ALTER TABLE ONLY hotel9.booking_has_room ALTER COLUMN booking_booking_id SET DEFAULT nextval('hotel9.booking_has_room_booking_booking_id_seq'::regclass);
 R   ALTER TABLE hotel9.booking_has_room ALTER COLUMN booking_booking_id DROP DEFAULT;
       hotel9          postgres    false    222    221    222            i           2604    32906    guest guest_id    DEFAULT     p   ALTER TABLE ONLY hotel9.guest ALTER COLUMN guest_id SET DEFAULT nextval('hotel9.guest_guest_id_seq'::regclass);
 =   ALTER TABLE hotel9.guest ALTER COLUMN guest_id DROP DEFAULT;
       hotel9          postgres    false    217    218    218                      0    32896    booking 
   TABLE DATA           q   COPY hotel9.booking (booking_id, guest_id, room_number, check_in_date, check_out_date, booking_date) FROM stdin;
    hotel9          postgres    false    216   H:                 0    32943    booking_has_guest 
   TABLE DATA           O   COPY hotel9.booking_has_guest (booking_booking_id, guest_guest_id) FROM stdin;
    hotel9          postgres    false    225   e:                 0    32925    booking_has_room 
   TABLE DATA           P   COPY hotel9.booking_has_room (booking_booking_id, room_room_number) FROM stdin;
    hotel9          postgres    false    222   �:                 0    32903    guest 
   TABLE DATA           C   COPY hotel9.guest (guest_id, guest_name, contact_info) FROM stdin;
    hotel9          postgres    false    218   �:                 0    32914    room 
   TABLE DATA           6   COPY hotel9.room (room_number, room_type) FROM stdin;
    hotel9          postgres    false    220   �:                 0    32909 	   room_type 
   TABLE DATA           ?   COPY hotel9.room_type (room_type, price_per_night) FROM stdin;
    hotel9          postgres    false    219   O;       #           0    0    booking_booking_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('hotel9.booking_booking_id_seq', 1, false);
          hotel9          postgres    false    215            $           0    0 (   booking_has_guest_booking_booking_id_seq    SEQUENCE SET     W   SELECT pg_catalog.setval('hotel9.booking_has_guest_booking_booking_id_seq', 1, false);
          hotel9          postgres    false    223            %           0    0 $   booking_has_guest_guest_guest_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('hotel9.booking_has_guest_guest_guest_id_seq', 1, false);
          hotel9          postgres    false    224            &           0    0 '   booking_has_room_booking_booking_id_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('hotel9.booking_has_room_booking_booking_id_seq', 1, false);
          hotel9          postgres    false    221            '           0    0    guest_guest_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('hotel9.guest_guest_id_seq', 1, false);
          hotel9          postgres    false    217            x           2606    32949 (   booking_has_guest booking_has_guest_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY hotel9.booking_has_guest
    ADD CONSTRAINT booking_has_guest_pkey PRIMARY KEY (booking_booking_id, guest_guest_id);
 R   ALTER TABLE ONLY hotel9.booking_has_guest DROP CONSTRAINT booking_has_guest_pkey;
       hotel9            postgres    false    225    225            v           2606    32930 &   booking_has_room booking_has_room_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY hotel9.booking_has_room
    ADD CONSTRAINT booking_has_room_pkey PRIMARY KEY (booking_booking_id, room_room_number);
 P   ALTER TABLE ONLY hotel9.booking_has_room DROP CONSTRAINT booking_has_room_pkey;
       hotel9            postgres    false    222    222            n           2606    32901    booking booking_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY hotel9.booking
    ADD CONSTRAINT booking_pkey PRIMARY KEY (booking_id);
 >   ALTER TABLE ONLY hotel9.booking DROP CONSTRAINT booking_pkey;
       hotel9            postgres    false    216            p           2606    32908    guest guest_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY hotel9.guest
    ADD CONSTRAINT guest_pkey PRIMARY KEY (guest_id);
 :   ALTER TABLE ONLY hotel9.guest DROP CONSTRAINT guest_pkey;
       hotel9            postgres    false    218            t           2606    32918    room room_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY hotel9.room
    ADD CONSTRAINT room_pkey PRIMARY KEY (room_number);
 8   ALTER TABLE ONLY hotel9.room DROP CONSTRAINT room_pkey;
       hotel9            postgres    false    220            r           2606    32913    room_type room_type_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY hotel9.room_type
    ADD CONSTRAINT room_type_pkey PRIMARY KEY (room_type);
 B   ALTER TABLE ONLY hotel9.room_type DROP CONSTRAINT room_type_pkey;
       hotel9            postgres    false    219            |           2606    32950 ;   booking_has_guest booking_has_guest_booking_booking_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY hotel9.booking_has_guest
    ADD CONSTRAINT booking_has_guest_booking_booking_id_fkey FOREIGN KEY (booking_booking_id) REFERENCES hotel9.booking(booking_id);
 e   ALTER TABLE ONLY hotel9.booking_has_guest DROP CONSTRAINT booking_has_guest_booking_booking_id_fkey;
       hotel9          postgres    false    225    4718    216            }           2606    32955 7   booking_has_guest booking_has_guest_guest_guest_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY hotel9.booking_has_guest
    ADD CONSTRAINT booking_has_guest_guest_guest_id_fkey FOREIGN KEY (guest_guest_id) REFERENCES hotel9.guest(guest_id);
 a   ALTER TABLE ONLY hotel9.booking_has_guest DROP CONSTRAINT booking_has_guest_guest_guest_id_fkey;
       hotel9          postgres    false    225    4720    218            z           2606    32931 9   booking_has_room booking_has_room_booking_booking_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY hotel9.booking_has_room
    ADD CONSTRAINT booking_has_room_booking_booking_id_fkey FOREIGN KEY (booking_booking_id) REFERENCES hotel9.booking(booking_id);
 c   ALTER TABLE ONLY hotel9.booking_has_room DROP CONSTRAINT booking_has_room_booking_booking_id_fkey;
       hotel9          postgres    false    4718    216    222            {           2606    32936 7   booking_has_room booking_has_room_room_room_number_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY hotel9.booking_has_room
    ADD CONSTRAINT booking_has_room_room_room_number_fkey FOREIGN KEY (room_room_number) REFERENCES hotel9.room(room_number);
 a   ALTER TABLE ONLY hotel9.booking_has_room DROP CONSTRAINT booking_has_room_room_room_number_fkey;
       hotel9          postgres    false    4724    222    220            y           2606    32919 "   room room_room_type_room_type_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY hotel9.room
    ADD CONSTRAINT room_room_type_room_type_fkey FOREIGN KEY (room_type) REFERENCES hotel9.room_type(room_type);
 L   ALTER TABLE ONLY hotel9.room DROP CONSTRAINT room_room_type_room_type_fkey;
       hotel9          postgres    false    220    4722    219                  x������ � �            x������ � �            x������ � �            x������ � �         �   x�Eα
1E�:�I&�$��Y-ZZ	A�������μ�t�R��<���{
&0�����1��E�%y8>�ۏ&0����g,���vH}GT�,�y�}��)�؝dUPU��{����VTF��׃���ce         @   x���K�I�44 .���$��	)�̃2KSS�l�����<�(� �������� *^-     