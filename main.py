import argparse

import requests

BASE_URL = "http://giaothong.hochiminhcity.gov.vn:8007/Render/CameraHandler.ashx?id="

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip",
    "Accept-Language": "en-US",
    "Connection": "keep-alive",
    "Cookie": ".VDMS=CC6872AB90FB4A651A2615F11BDB29602B58C9FC8FD588357660F2506A6F5A7FA1D34E11CA405C0E6FB3F4C312D0C749F1545536C7D463CB9E90C6E927F1659BEF418D17EA399E159A6C74B108F8A41401D8769276E9B0F3AAA058A8BE31C845C00FA7D3D2469648DD19601A3FC71563C86FBDB1; ASP.NET_SessionId=e5bdgyd0a51rn2rnnydl1i10; _frontend=!lFq+1yibrtBxZ8Yk6kBz84d1gt+W5rl5eDKl6kbrG3J0YJRHDGpjVfjQ1rc56VO2pTYpo/Bvt24mcnQ=; CurrentLanguage=vi",
    "Host": "giaothong.hochiminhcity.gov.vn:8007",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0",
}

locations = {
    "quang_trung_ba_trieu": "5a6061868576340017d06611",
    "nguyen_bieu_cau_chu_y": "5a82439f5058170011f6eaa9",
    "nguyen_van_cu_tran_hung_dao_2": "5b0b7bbe0e517b00119fd806",
    "nut_giao_nga_sau_cong_hoa": "5deb576d1dc17d7c5515acf7",
    "nut_giao_cong_truong_dan_chu": "5deb576d1dc17d7c5515acf9",
}


def download_image(input, output):
    location = ""
    with open(input, "r") as f:
        location = f.read().strip()

    if location == "" or location not in locations:
        print("wrong location")

    id = locations[location]
    url = BASE_URL + id
    print("url", url)

    rsp = requests.get(url, headers=HEADERS)

    if rsp.status_code == 200:
        with open(output, "wb") as f:
            f.write(rsp.content)
    else:
        print("god bless you")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="input filename")
    parser.add_argument("output_without_ext", help="output filename without extension")
    args = parser.parse_args()

    output = args.output_without_ext + ".jpg"
    print("output", output)
    download_image(args.input, output)


if __name__ == "__main__":
    main()

