# def bubbleSort(n, status):
#     if status == "Terkecil":
#         for i in range(n):
#             for j in range(0, n - i - 1):
#                 if harga_merch[j][1] > harga_merch[j + 1][1]:
#                     harga_merch[j], harga_merch[j + 1] = harga_merch[j + 1], harga_merch[j]
#     else:
#         for i in range(n):
#             for j in range(0, n - i - 1):
#                 if harga_merch[j][1] < harga_merch[j + 1][1]:
#                     harga_merch[j], harga_merch[j + 1] = harga_merch[j + 1], harga_merch[j]

# harga_merch = [
#     ("Alhaitham", 210000),
#     ("Furina", 300000),
#     ("Odette", 180000),
#     ("Nahida", 290000),
#     ("Flins", 250000)]

# print("══════════════ PENGURUTAN HARGA MERCHANDISE GENSHIN (BUBBLE SORT) ══════════════")

# print("\nMerchandise Genshin sebelum diurutkan berdasarkan harga:")
# for nama, harga in harga_merch:
#     print(nama, "-", f"Rp{harga:,}".replace(",", "."))

# print("\nMerchandise setelah diurutkan berdasarkan harga terkecil ke terbesar:")
# bubbleSort(len(harga_merch), "Terkecil")
# for nama, harga in harga_merch:
#     print(nama, "-", f"Rp{harga:,}".replace(",", "."))

# print("\nMerchandise setelah diurutkan berdasarkan harga terbesar ke terkecil:")
# bubbleSort(len(harga_merch), "Terbesar")
# for nama, harga in harga_merch:
#     print(nama, "-", f"Rp{harga:,}".replace(",", "."))

# print("\n════════════════════════════ PENGURUTAN SELESAI ════════════════════════════")


def heapify(n, i, status):
    if status == "Terkecil":
        terbesar = i
        kiri = 2 * i + 1
        kanan = 2 * i + 2
        if kiri < n and harga_merch[kiri][1] > harga_merch[terbesar][1]:
            terbesar = kiri
        if kanan < n and harga_merch[kanan][1] > harga_merch[terbesar][1]:
            terbesar = kanan
        if terbesar != i:
            harga_merch[i], harga_merch[terbesar] = harga_merch[terbesar], harga_merch[i]
            heapify(n, terbesar, status)
    else:
        terkecil = i
        kiri = 2 * i + 1
        kanan = 2 * i + 2
        if kiri < n and harga_merch[kiri][1] < harga_merch[terkecil][1]:
            terkecil = kiri
        if kanan < n and harga_merch[kanan][1] < harga_merch[terkecil][1]:
            terkecil = kanan
        if terkecil != i:
            harga_merch[i], harga_merch[terkecil] = harga_merch[terkecil], harga_merch[i]
            heapify(n, terkecil, status)

def heapSort(n, status):
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i, status)
    for i in range(n - 1, 0, -1):
        harga_merch[0], harga_merch[i] = harga_merch[i], harga_merch[0]
        heapify(i, 0, status)

harga_merch = [
    ("Alhaitham", 210000),
    ("Furina", 300000),
    ("Odette", 180000),
    ("Nahida", 290000),
    ("Flins", 250000)]

print("══════════════ PENGURUTAN HARGA MERCHANDISE GENSHIN (HEAP SORT) ══════════════")

print("\nMerchandise Genshin sebelum diurutkan berdasarkan harga:")
for nama, harga in harga_merch:
    print(nama, "-", f"Rp{harga:,}".replace(",", "."))

print("\nMerchandise setelah diurutkan berdasarkan harga terkecil ke terbesar:")
heapSort(len(harga_merch), "Terkecil")
for nama, harga in harga_merch:
    print(nama, "-", f"Rp{harga:,}".replace(",", "."))

print("\nMerchandise setelah diurutkan berdasarkan harga terbesar ke terkecil:")
heapSort(len(harga_merch), "Terbesar")
for nama, harga in harga_merch:
    print(nama, "-", f"Rp{harga:,}".replace(",", "."))

print("\n════════════════════════════ PENGURUTAN SELESAI ════════════════════════════")