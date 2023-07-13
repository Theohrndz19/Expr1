meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "LMAO":"Tanggapan Terhadap Hal yang sangat Lucu"
            "KYS": "Pernyataan yang digunakan sebagai cara untuk memberitahu seseorang untuk bunuh diri"
            "N Word":"Pernyataan Yang Digunakan Kepada Orang Hitam"
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")
 
if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
    break
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print('Mohon maaf Kami tidak mengerti apa yang Anda maksud!')    
