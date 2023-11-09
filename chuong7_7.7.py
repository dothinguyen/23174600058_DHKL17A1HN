def doi_tien(so_tien):
    to_500000 = so_tien // 500000
    so_tien %= 500000

    to_200000 = so_tien // 200000
    so_tien %= 200000

    to_100000 = so_tien // 100000
    so_tien %= 100000

    to_50000 = so_tien // 50000
    so_tien %= 50000

    return (to_500000, to_200000, to_100000, to_50000, so_tien)

so_tien_muon_doi = int(input("Nhập số tiền muốn đổi: "))
so_to_500000, so_to_200000, so_to_100000, so_to_50000, so_tien_con_lai = doi_tien(so_tien_muon_doi)

print("Số tờ 500,000: ", so_to_500000)
print("Số tờ 200,000: ", so_to_200000)
print("Số tờ 100,000: ", so_to_100000)
print("Số tờ 50,000: ", so_to_50000)
print("Số tiền còn lại: ", so_tien_con_lai)
