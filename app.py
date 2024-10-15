
# 3. Creación del Backend con FastAPI #
""" Vamos a implementar una API básica en FastAPI para recibir un enlace y utilizar el código que descargaste. 
Este endpoint tomará una URL y ejecutará el proceso de descarga."""


from flask import Flask, request, jsonify
from main import descargar_video # Importa la función que descarga canciones

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')
    if url:
        try:
            descargar_video(url)  # Aquí ejecutamos la lógica para descargar la canción
            return jsonify({'status': 'success', 'message': 'Canción descargada correctamente'}), 200
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)}), 500
    return jsonify({'status': 'error', 'message': 'URL no proporcionada'}), 400

if __name__ == '__main__':
    app.run(debug=True)
