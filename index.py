import brython

@brython.module
def main():
    # IP adresi veritabanı
    ip_database = {}

    # Bir tuval oluşturun
    data = {
        "width": 100,
        "height": 100,
        "background_color": "#ffffff",
    }
    response = requests.post("https://api.reddit.com/place/canvas_pixel", json=data)

    # Tuvalin bir kopyasını alın
    canvas = response.json()

    # Bir döngüde, IP adreslerinden tuvali boyamaya çalışanları takip edin
    while True:
        # Kullanıcıların tuvali boyamasını bekleyin
        time.sleep(1)

        # Tuvalin bir kopyasını alın
        canvas = response.json()

        # IP adreslerini takip edin
        for pixel in canvas["pixels"]:
            ip = pixel["ip_address"]

            # Kullanıcıyı veritabanında bulun
            if ip not in ip_database:
                ip_database[ip] = 0

            # Kullanıcının puanını artırın
            ip_database[ip] += 1

        # En yüksek puana sahip IP adresini bulun
        winner = max(ip_database, key=ip_database.get)

        # Kazananı yazdırın
        print(f"Kazanan: {winner}")

if __name__ == "__main__":
    brython.start_server(main)
