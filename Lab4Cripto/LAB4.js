// ==UserScript==
// @name         Lab 4 Cripto
// @namespace    https://cripto.tiiny.site/
// @version      0.1
// @description  Este código permite obtener la llave para el descifrado de los mensajecultos en la página web
// @author       Felipe M.
// @match        https://cripto.tiiny.site/
// @icon         https://www.google.com/s2/favicons?sz=64&domain=tiiny.site
// @grant        none
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// ==/UserScript==

function getSecretKey() {
    var bodyText = document.body.innerText; // Se obtiene el texto de la etiqueta body
    var upperCaseChars = bodyText.match(/[A-Z]/g);
    if (upperCaseChars) {
        var secretKey = upperCaseChars.join("");
    }
    return secretKey;
}

function getCipheredMessageIds() {
    var ids = [];
    var elements = document.querySelectorAll('[class*="M"]'); // Se obtienen elementos que contienen M en su clase (ejemplo: M1)
    elements.forEach(function(element) {
        ids.push(element.id); // Se guarda el ID del elemento (mensaje cifrado)
    });
    return ids;
}

function displayInfo() {
    var ids = getCipheredMessageIds();
    console.log("La llave es: " + getSecretKey());
    console.log("Los mensajes cifrados son: " + ids.length);
}

function printHtml(text) {
    var body = document.body;
    var newParagraph = document.createElement('p');
    newParagraph.textContent = text;
    body.appendChild(newParagraph);
}

function decryptMessages() {
    var ids = getCipheredMessageIds();
    var secretKey = getSecretKey();
    var plainText = [];
    var keyWordArray = CryptoJS.enc.Utf8.parse(secretKey); // Convertir la clave a formato WordArray
    for (var i = 0; i < ids.length; i++) {
        var bytesId = CryptoJS.enc.Base64.parse(ids[i]);
        var TripleDES = CryptoJS.TripleDES.decrypt({ ciphertext: bytesId }, keyWordArray, { mode: CryptoJS.mode.ECB }).toString(CryptoJS.enc.Utf8);
        printHtml(TripleDES);
        console.log(ids[i] + " " + TripleDES);
    }
}

(function() {
    displayInfo();
    decryptMessages();
})();
