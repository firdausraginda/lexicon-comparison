# tanpa custom lex, akurasi lvl dokumen 90% tapi lvl kalimat rendah
# lexCustom = []

# akurasi lvl dokumen 90% dan lvl kalimat lebih tinggi
# lexCustom = [['tidak ada', 0], ['ga ada', 0], ['masukkan', -1], ['masukan', -1]]
# lexCustom = [['tidak ada', 0], ['ga ada', 0], ['masukkan', -1], ['masukan', -1], ['mata kuliah', 2], ['mengajar', 3], ['ajar', 3], ['sulit', -3], ['mengeluh', -3], ['contek', -5], ['putus asa', -5], ['suara', 0], ['metode', 0]]
lexCustom = [['tidak ada', 0], ['ga ada', 0], ['masukkan', -1], ['masukan', -1], ['mata kuliah', 0], ['mengajar', 0], ['ajar', 0], ['sulit', -3], ['mengeluh', -3], ['contek', -5], ['putus asa', -5]]

# paksain akurasi lvl kalimat naik, tp lvl dokumen turun jadi 72%
# lexCustom = [['tidak ada', 0], ['ga ada', 0], ['bagus', 2], ['keren', 2], ['sangat baik', 4], ['sangat bagus', 4], ['sangat menyenangkan', 3], ['cukup', 1], ['masukkan', -1], ['masukan', -1], ['sulit', -3], ['contek', -5]]

# ga ada = tidak ada = 0
# masukkan dan masukan = saran = -1