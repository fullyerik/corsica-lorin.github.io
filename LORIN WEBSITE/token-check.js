document.addEventListener("DOMContentLoaded", function() {
    const validTokens = ["geheimerToken123", "zweiterToken456"]; // Hier gültige Tokens eintragen
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get("token");

    if (!token || !validTokens.includes(token)) {
        document.body.innerHTML = '<div class="error">Zugriff verweigert! Ungültiger oder fehlender Token.</div>';
    }
});
