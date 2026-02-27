# ========================================== # DEVELOPPED BY : A S T R A  # PROJECT : NEXUSLINK PRO - SÉCURISÉ & ILLIMITÉ # ==========================================

from flask import Flask, render_template_string, request, Response, stream_with_context

app = Flask(__name__)

HTML_TEMPLATE = """ <!DOCTYPE html> <html lang="fr"> <head>     <meta charset="UTF-8">     <meta name="viewport" content="width=device-width, initial-scale=1.0">     <title>ASTRA - NexusLink Pro</title>     <style>         :root { --astra-blue: #003366; --astra-green: #00FF7F; --astra-orange: #FF8C00; --astra-dark: #0a0a0a; }         body { background: var(--astra-dark); color: white; font-family: 'Segoe UI', sans-serif; text-align: center; margin: 0; overflow-x: hidden; }                  /* LOGO ASTRA */         .astra-logo-container {             width: 100px; height: 100px; background: radial-gradient(circle, var(--astra-blue), #001122);             border-radius: 50%; display: flex; align-items: center; justify-content: center;             margin: 30px auto; box-shadow: 0 0 20px var(--astra-green);         }         .logo-a { width: 60px; fill: var(--astra-green); }

        .screen { display: none; padding: 20px; animation: fadeIn 0.5s; }         .active { display: block; }         @keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }

        .btn-orange { background: var(--astra-orange); color: black; padding: 20px 40px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; font-size: 1.1rem; }         .btn-blue-tech { background: #0044ff; color: white; padding: 15px 30px; border: 2px solid #ff0000; border-radius: 5px; cursor: pointer; font-weight: bold; }                  input[type="text"] { background: #222; border: 1px solid var(--astra-green); color: white; padding: 15px; border-radius: 10px; width: 80%; margin-bottom: 20px; }                  .alert-box { color: #ff4444; font-weight: bold; border: 2px solid #ff4444; padding: 15px; border-radius: 10px; margin: 20px; display: inline-block; }         .footer-pro { margin-top: 50px; border-top: 1px solid #333; padding: 20px; font-size: 0.8rem; opacity: 0.6; }     </style> </head> <body>

    <div class="astra-logo-container" aria-label="Logo Astra">         <svg class="logo-a" viewBox="0 0 100 100">             <path d="M50 15 L20 85 H35 L50 45 L65 85 H80 Z M42 60 H58 L50 75 Z" />         </svg>     </div>

    <div id="screen-1" class="screen active">         <h1>Bienvenue sur NexusLink</h1>         <p>La plateforme sécurisée pour vos transferts de fichiers.</p>         <p style="opacity:0.8">Appuyez sur suivant pour continuer</p>         <br>         <button class="btn-orange" onclick="nextScreen(2)">SUIVANT</button>     </div>

    <div id="screen-2" class="screen">         <h2>Veuillez saisir votre prénom</h2>         <input type="text" id="user-name" placeholder="Votre prénom ici...">         <br>         <button class="btn-blue-tech" onclick="nextScreen(3)">SUIVANT</button>     </div>

    <div id="screen-3" class="screen">         <div id="no-device" class="alert-box">             AUCUN APPAREIL DÉTECTÉ : VEUILLEZ BRANCHER VOTRE APPAREIL         </div>                  <div id="device-found" style="display:none; color:var(--astra-green); margin:20px;">             ✅ APPAREIL DÉTECTÉ ET BRANCHÉ         </div>

        <div style="margin: 30px;">             <input type="file" id="file-input" style="display:none" onchange="fileSelected()">             <button id="btn-select" class="btn-orange" style="opacity:0.5; cursor:not-allowed;" onclick="triggerFile()" disabled>CHOISIR UN FICHIER</button>         </div>

        <button id="btn-transfer" class="btn-orange" style="display:none" onclick="startTransfer()">LANCER LE TRANSFERT</button>                  <div class="footer-pro">             <p>Publicités | Contrat de Licence | Avis ★★★★★ (Fichiers illimités)</p>         </div>     </div>

    <div id="screen-4" class="screen">         <h2 id="transfer-status">TRANSFERT EN COURS...</h2>         <p id="file-display"></p>         <br>         <button class="btn-orange" onclick="nextScreen(3)">RETOUR</button>     </div>

    <script>         const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

        function playBip() {             const osc = audioCtx.createOscillator();             const g = audioCtx.createGain();             osc.frequency.value = 600;             osc.connect(g); g.connect(audioCtx.destination);             osc.start(); osc.stop(audioCtx.currentTime + 0.1);         }

        function playVictory() {             [523, 659, 783, 1046].forEach((f, i) => {                 setTimeout(() => {                     const o = audioCtx.createOscillator();                     const g = audioCtx.createGain();                     o.frequency.value = f; o.connect(g); g.connect(audioCtx.destination);                     o.start(); o.stop(audioCtx.currentTime + 0.2);                 }, i * 150);             });         }

        function nextScreen(num) {             playBip();             document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));             document.getElementById('screen-' + num).classList.add('active');                          if(num === 3) {                 // Simulation détection câble après 2 sec                 setTimeout(() => {                     document.getElementById('no-device').style.display = 'none';                     document.getElementById('device-found').style.display = 'block';                     document.getElementById('btn-select').style.opacity = '1';                     document.getElementById('btn-select').style.cursor = 'pointer';                     document.getElementById('btn-select').disabled = false;                 }, 2000);             }         }

        function triggerFile() {             playBip();             document.getElementById('file-input').click();         }

        function fileSelected() {             document.getElementById('btn-transfer').style.display = 'inline-block';             alert("Fichier prêt pour l'envoi illimité.");         }

        function startTransfer() {             playBip();             const file = document.getElementById('file-input').files[0];             nextScreen(4);             document.getElementById('file-display').innerText = "Fichier : " + file.name + " (" + (file.size/1000000).toFixed(2) + " Mo)";                          setTimeout(() => {                 playVictory();                 document.getElementById('transfer-status').innerHTML = "✅ VICTOIRE ! TRANSFERT TERMINÉ.";                 alert("Le fichier a été enregistré sur votre appareil.");             }, 3000);         }     </script> </body> </html> """

@app.route('/') def index():     return render_template_string(HTML_TEMPLATE)

# MOTEUR DE STREAMING SANS LIMITE (CHUNKS) @app.route('/transfer', methods=['POST']) def transfer():     def generate():         while True:             data = request.stream.read(1024 * 1024) # Lecture par blocs de 1Mo             if not data: break             yield data     return Response(stream_with_context(generate()))

if __name__ == '__main__':     app.run(host='0.0.0.0', port=8080)
