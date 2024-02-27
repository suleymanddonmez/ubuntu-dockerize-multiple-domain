# Multiple Domain With LetsEncript SSL
- AWS ubuntu server üzerinde önce docker kurulup docker compose ile multiple domain yönetilmiştir.

# docker kurulumu
- sudo apt-get update -y
- sudo apt-get upgrade -y
- sudo apt-get install ca-certificates curl gnupg lsb-release
- curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg –dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
- echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
- sudo apt-get update
- sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
- sudo apt-get install docker-compose
- apt-cache madison docker-ce

# docker containerler
- sudo docker ps

# docker images
- sudo docker images

# ssl kurulumu
- sudo apt update && sudo apt install certbot -y
- sudo certbot certonly --standalone -d service1.reiland.xyz -m <email-address> --agree-tos
- sertifika oluşturulduktan sonra compose içerisine sertifikaların bulunduğu klasor mount edilir ve nginx.conf dosyası buna göre düzenlenir.
- örnek olarak buradaki compose ve nginx.conf dikkate alınabilir.

