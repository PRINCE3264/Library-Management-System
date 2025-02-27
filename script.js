
document.getElementById('phishingForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;


    document.getElementById('phishingAlert').innerHTML = `
        <div class="alert alert-danger">
            Phishing attempt detected! Username: ${username}, Password: ${password}
        </div>
    `;


    console.log(`Captured credentials: Username - ${username}, Password - ${password}`);
});


document.getElementById('encryptionForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const passwordToEncrypt = document.getElementById('passwordToEncrypt').value;
    if (passwordToEncrypt) {
        const encryptedPassword = btoa(passwordToEncrypt);
        document.getElementById('encryptedPassword').innerHTML = `
            <strong>Encrypted Password:</strong> ${encryptedPassword}
        `;
    }
});


document.getElementById('decryptionForm').addEventListener('submit', function (e) {
    e.preventDefault();

    const passwordToDecrypt = document.getElementById('passwordToDecrypt').value;
    if (passwordToDecrypt) {
        const decryptedPassword = atob(passwordToDecrypt);
        document.getElementById('decryptedPassword').innerHTML = `
            <strong>Decrypted Password:</strong> ${decryptedPassword}
        `;
    }
});
