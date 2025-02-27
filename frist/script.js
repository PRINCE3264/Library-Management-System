// Phishing Simulation (Capture Credentials)
document.getElementById('phishingForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simulating phishing attack - capturing credentials
    document.getElementById('phishingAlert').innerHTML = `
        <div class="alert alert-danger">
            Phishing attempt detected! Username: ${username}, Password: ${password}
        </div>
    `;

    // Simulate sending the captured data to the attacker
    console.log(`Captured credentials: Username - ${username}, Password - ${password}`);
});

// Simple Password Encryption (using Base64 for simulation)
document.getElementById('encryptionForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const passwordToEncrypt = document.getElementById('passwordToEncrypt').value;
    if (passwordToEncrypt) {
        const encryptedPassword = btoa(passwordToEncrypt);  // Base64 Encoding (Simulated Encryption)
        document.getElementById('encryptedPassword').innerHTML = `
            <strong>Encrypted Password:</strong> ${encryptedPassword}
        `;
    }
});

// Password Decryption (Base64 Decoding)
document.getElementById('decryptionForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const passwordToDecrypt = document.getElementById('passwordToDecrypt').value;
    if (passwordToDecrypt) {
        const decryptedPassword = atob(passwordToDecrypt);  // Base64 Decoding (Simulated Decryption)
        document.getElementById('decryptedPassword').innerHTML = `
            <strong>Decrypted Password:</strong> ${decryptedPassword}
        `;
    }
});
