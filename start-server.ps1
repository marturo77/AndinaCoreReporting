# Este script inicia un servidor HTTP simple en el puerto 8080 usando Python
# Abre el navegador automáticamente en http://localhost:8080/index.html

$port = 8080
$index = "index.html"

# Verifica si Python está instalado
$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    Write-Host "Python no está instalado. Por favor, instala Python para usar este script."
    exit 1
}

Start-Process "python" -ArgumentList "-m http.server $port" -WindowStyle Hidden
Start-Sleep -Seconds 2
Start-Process "http://localhost:$port/$index"
